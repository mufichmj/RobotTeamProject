import mqtt_remote_method_calls as com
import robot_controller as robo
import time
import ev3dev.ev3 as ev3


class Dog(object):

    def __init__(self):
        self.robot = robo.Snatch3r()
        self.trick = False

    def doggo_stop(self):
        print("doggo stop")
        self.robot.stop()

    def zoom_forward(self, left, right):
        print("zoom forward")
        self.robot.forward(left, right)

    def doggo_bark(self):
        print("doggo barking")
        ev3.Sound.speak("Bork Bork Bork").wait()

    def check_color(self):
        while True:
            if self.robot.color_sensor.color == ev3.ColorSensor.COLOR_GREEN:
                ev3.Sound.speak("Bork Bork Bork").wait()
                self.trick = True
                time.sleep(3)
                self.trick = False
                break

            if self.robot.color_sensor.color == ev3.ColorSensor.COLOR_BLACK:
                self.robot.spin_left_degrees(90, 100, 'brake')
                self.trick = True
                time.sleep(3)
                self.trick = False
                break

            if self.robot.color_sensor.color == ev3.ColorSensor.COLOR_YELLOW:
                self.robot.spin_right_degrees(90, 100, 'brake')
                self.trick = True
                time.sleep(3)
                self.trick = False
                break

            if self.robot.color_sensor.color == ev3.ColorSensor.COLOR_RED:
                self.robot.arm_up()
                self.robot.arm_down()
                self.trick = True
                time.sleep(3)
                self.trick = False
                break




def main():
    # robot = robo.Snatch3r()
    elon = Dog()
    mqtt_client = com.MqttClient(elon)
    mqtt_client.connect_to_pc()

    while True:
        time.sleep(.05)
        if elon.trick == True:
            mqtt_client.send_message('bone')
main()
