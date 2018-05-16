import tkinter
from tkinter import ttk

import ev3dev.ev3 as ev3
import time

import mqtt_remote_method_calls as com
import robot_controller as robo


class Robot(object):
    def __init__(self):
        self.robot = robo.Snatch3r()





def main():
    delegate = Robot()
    mqtt_client = com.MqttClient(delegate)
    mqtt_client.connect_to_pc()

    robot.loop_forever()


main()

