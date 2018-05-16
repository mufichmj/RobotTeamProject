import time

import mqtt_remote_method_calls as com
import robot_controller as robo


class Robot(object):
    def __init__(self):
        self.robot = robo.Snatch3r()


    def loop_forever(self):
        self.robot.loop_forever()


    def go_through_cones(self, number_cones):
        for k in range(number_cones):
            self.robot.forward(400, 400)
            time.sleep(1)
            self.robot.stop()
            self.robot.spin_left_degrees(90)
            self.robot.forward(400, 400)
            time.sleep(1)
            self.robot.stop()
            self.robot.spin_right_degrees(90)
            self.robot.forward(400, 400)
            time.sleep(1)
            self.robot.stop()
            self.robot.spin_right_degrees(90)
            self.robot.forward(400, 400)
            time.sleep(1)
            self.robot.stop()
            self.robot.spin_left_degrees(90)



def main():
    delegate = Robot()
    mqtt_client = com.MqttClient(delegate)
    mqtt_client.connect_to_pc()

    delegate.loop_forever()


main()

