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
            time.sleep(4)
            self.robot.stop()
            self.robot.spin_left_degrees(90)
            self.robot.forward(400, 400)
            time.sleep(4)
            self.robot.stop()
            self.robot.spin_right_degrees(90)
            self.robot.forward(400, 400)
            time.sleep(4)
            self.robot.stop()
            self.robot.spin_right_degrees(90)
            self.robot.forward(400, 400)
            time.sleep(4)
            self.robot.stop()
            self.robot.spin_left_degrees(90)

    def forward(self, left, right):
        self.robot.forward(left, right)

    def left(self, left, right):
        self.forward(left, right)

    def right(self, left, right):
        self.forward(left, right)

    def backward(self, left, right):
        self.forward(left, right)

    def arm_up(self):
        self.robot.arm_up()

    def arm_down(self):
        self.robot.arm_down()

    def stop(self):
        self.robot.stop()

    def shutdown(self):
        self.robot.shutdown()

    def shoot_soccer_ball(self):
        self.robot.pixy.mode = "SIG2"
        while True:
            if self.robot.pixy.value(1) > 140 and self.robot.pixy.value(1) < 160:
                self.robot.forward(600, 600)
                time.sleep(6)
                self.robot.stop()
                break
            else:
                self.robot.spin_left_degrees(5)
            time.sleep(0.1)


def main():
    delegate = Robot()
    mqtt_client = com.MqttClient(delegate)
    mqtt_client.connect_to_pc()
    delegate.loop_forever()


main()
