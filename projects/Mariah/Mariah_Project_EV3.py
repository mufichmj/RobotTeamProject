import time

import mqtt_remote_method_calls as com
import robot_controller as robo


class Robot(object):
    def __init__(self):
        self.robot = robo.Snatch3r()
        self.pixy = ev3.Sensor(driver_name="pixy_lego")
        self.pixy.mode = "SIG1"
        print("(X, Y)=({}, {}) Width={} Height={}".format(
            pixy.value(1), pixy.value(2), pixy.value(3),
            pixy.value(4)))



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
        self.left_motor.run_forever(speed_sp=left)
        self.right_motor.run_forever(speed_sp=right)


    def left(self):


    def right(self):


    def backward(self):


    def up(self):


    def down(self):



    def shoot_soccer_ball(self, left_speed_entry, right_speed_entry):
        self.forward(left_speed_entry, right_speed_entry)
        while True:
            self.pixy.mode = ""



def main():
    delegate = Robot()
    mqtt_client = com.MqttClient(delegate)
    mqtt_client.connect_to_pc()
    delegate.loop_forever()


main()

