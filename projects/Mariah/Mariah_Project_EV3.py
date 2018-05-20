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
        for k in range(10):
            self.robot.pixy.mode = "SIG2"
            print("(X, Y)=({}, {}) Width={} Height={}".format(
                self.robot.pixy.value(1), self.robot.pixy.value(2), self.robot.pixy.value(3),
                self.robot.pixy.value(4)))
            time.sleep(1)


def main():
    delegate = Robot()
    mqtt_client = com.MqttClient(delegate)
    mqtt_client.connect_to_pc()
    delegate.loop_forever()


main()
