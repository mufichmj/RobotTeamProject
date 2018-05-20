# Zack Watson Final Project for ev3

import robot_controller as robo
import time
import mqtt_remote_method_calls as com


class RobotDelegate(object):

    def __init__(self):
        self.robot = robo.Snatch3r()

    def moonwalk(self):
        self.robot.play_string('moonwalking')
        time.sleep(1)
        self.robot.left_motor.run_forever(speed_sp=-900)
        time.sleep(0.25)
        self.robot.stop()
        for _ in range(4):
            self.robot.right_motor.run_forever(speed_sp=-900)
            time.sleep(0.5)
            self.robot.stop()
            self.robot.left_motor.run_forever(speed_sp=-900)
            time.sleep(0.5)
            self.robot.stop()
        self.robot.right_motor.run_forever(speed_sp=-900)
        time.sleep(0.25)
        self.robot.stop()

    def waltz(self):
        self.robot.play_string('waltzing')
        time.sleep(1)
        for _ in range(3):
            self.robot.left_motor.run_forever(speed_sp=400)
            time.sleep(0.75)
            self.robot.stop()
            self.robot.right_motor.run_forever(speed_sp=400)
            time.sleep(1.25)
            self.robot.stop()
            self.robot.left_motor.run_forever(speed_sp=400)
            time.sleep(0.5)
            self.robot.stop()
            self.robot.right_motor.run_forever(speed_sp=-400)
            time.sleep(0.75)
            self.robot.stop()
            self.robot.left_motor.run_forever(speed_sp=-400)
            time.sleep(1.25)
            self.robot.stop()
            self.robot.right_motor.run_forever(speed_sp=-400)
            time.sleep(0.5)
            self.robot.stop()

    def square_dance(self):
        self.robot.play_string('square')
        time.sleep(1)
        for _ in range(4):
            self.robot.forward(500, 500)
            time.sleep(3)
            self.robot.stop()
            self.robot.turn_left_degrees(90)

    def whip_nae_nae(self):
        self.robot.play_string('silento')
        time.sleep(1)
        self.robot.left(500, 500)
        time.sleep(0.5)
        self.robot.stop()
        self.robot.arm_part_up()
        time.sleep(0.5)
        self.robot.left(500, 500)
        time.sleep(0.5)
        self.robot.right(500, 500)
        time.sleep(0.5)
        self.robot.stop()
        self.robot.arm_up()

    def hands_up(self):
        self.robot.play_string('hands_up')
        time.sleep(1)
        self.robot.arm_up()
        self.robot.backward(400, 200)
        time.sleep(0.5)
        self.robot.backward(200, 400)
        time.sleep(0.5)
        self.robot.stop()

    def arm_down(self):
        self.robot.arm_down()

    def exit(self):
        self.robot.shutdown()


def main():
    rd = RobotDelegate()
    mqtt_client = com.MqttClient(rd)
    mqtt_client.connect_to_pc()

    rd.robot.remote1.on_red_up = lambda state: handle_red_up(state, rd)
    rd.robot.remote1.on_red_down = lambda state: handle_red_down(state, rd)
    rd.robot.remote1.on_blue_up = lambda state: handle_blue_up(state, rd)
    rd.robot.remote1.on_blue_down = lambda state: handle_blue_down(state, rd)

    rd.robot.running = True
    while rd.robot.running:
        rd.robot.remote1.process()
        time.sleep(0.05)


def handle_red_up(state, rd):
    if state:
        rd.robot.left_motor.run_forever(speed_sp=900)
    else:
        rd.robot.stop()


def handle_red_down(state, rd):
    if state:
        rd.robot.left_motor.run_forever(speed_sp=-900)
    else:
        rd.robot.stop()


def handle_blue_up(state, rd):
    if state:
        rd.robot.right_motor.run_forever(speed_sp=900)
    else:
        rd.robot.stop()


def handle_blue_down(state, rd):
    if state:
        rd.robot.right_motor.run_forever(speed_sp=-900)
    else:
        rd.robot.stop()


main()
