# Zack Watson Final Project for ev3

import ev3dev as ev3
import robot_controller as robo
import time
import mqtt_remote_method_calls as com


class RobotDelegate(object):

    def __init__(self):
        self.robot = robo.Snatch3r()

    def loop_forever(self):
        self.robot.loop_forever()


def main():
    rd = RobotDelegate()
    mqtt_client = com.MqttClient(rd)
    mqtt_client.connect_to_pc()
    rd.loop_forever()


main()
