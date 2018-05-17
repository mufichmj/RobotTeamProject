"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""


import ev3dev.ev3 as ev3
import math
import time


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    def __init__(self):

        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.touch_sensor = ev3.TouchSensor()
        self.color_sensor = ev3.ColorSensor()
        self.ir_sensor = ev3.InfraredSensor()
        self.pixy = ev3.Sensor(driver_name="pixy-lego")
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.buttons = ev3.Button()
        self.remote1 = ev3.RemoteControl(channel=1)
        self.running = False

        assert self.left_motor
        assert self.right_motor
        assert self.arm_motor
        assert self.touch_sensor
        assert self.color_sensor
        assert self.ir_sensor
        assert self.pixy
        assert self.buttons
        assert self.remote1

    def forward_inches(self, inches, speed=100, stop_action='brake'):

        k = 360 / 4.1
        degrees_motor = k * inches
        self.left_motor.run_to_rel_pos(position_sp=degrees_motor, speed_sp=8*speed, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=degrees_motor, speed_sp=8*speed, stop_action=stop_action)
        self.left_motor.wait_while('running')
        self.right_motor.wait_while('running')

    def backward_inches(self, inches, speed=100, stop_action='brake'):

        self.forward_inches(inches, -speed, stop_action)

    def spin_left_degrees(self, degrees, speed=100, stop_action='brake'):

        k = 4.15
        new_degrees = (k * degrees)
        self.left_motor.run_to_rel_pos(speed_sp=-speed*8, position_sp=-new_degrees, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(speed_sp=speed*8, position_sp=new_degrees, stop_action=stop_action)
        self.left_motor.wait_while('running')
        self.right_motor.wait_while('running')

    def spin_right_degrees(self, degrees, speed=100, stop_action='brake'):

        k = 4.15
        new_degrees = (k * degrees)
        self.left_motor.run_to_rel_pos(speed_sp=speed*8, position_sp=new_degrees, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(speed_sp=-speed*8, position_sp=-new_degrees, stop_action=stop_action)
        self.left_motor.wait_while('running')
        self.right_motor.wait_while('running')

    def turn_left_degrees(self, degrees, speed=100, stop_action='brake'):
        
        self.right_motor.run_forever(speed_sp=speed * 8)
        time.sleep((1 / ((abs(speed) * 8) * (1 / 90))) * ((abs(degrees) * math.pi) / 36))
        self.right_motor.stop(stop_action=stop_action)

    def turn_right_degrees(self, degrees, speed=100, stop_action='brake'):

        self.turn_left_degrees(degrees, -speed, stop_action)

    def loop_forever(self):
        # This is a convenience method that I don't really recommend for most programs other than m5.
        #   This method is only useful if the only input to the robot is coming via mqtt.
        #   MQTT messages will still call methods, but no other input or output happens.
        # This method is given here since the concept might be confusing.
        self.running = True
        while self.running:
            time.sleep(0.1)  # Do nothing (except receive MQTT messages) until an MQTT message calls shutdown.

    def shutdown(self):
        # Modify a variable that will allow the loop_forever method to end. Additionally stop motors and set LEDs green.
        # The most important part of this method is given here, but you should add a bit more to stop motors, etc.
        self.arm_motor.stop(stop_action='brake')
        self.left_motor.stop(stop_action='brake')
        self.right_motor.stop(stop_action='brake')
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        if self.touch_sensor.is_pressed:
            self.arm_down()
        self.running = False

    def forward(self, left, right):
        self.left_motor.run_forever(speed_sp=left)
        self.right_motor.run_forever(speed_sp=right)

    def backward(self, left, right):
        self.forward(-left, -right)

    def stop(self):
        self.left_motor.stop(stop_action='brake')
        self.right_motor.stop(stop_action='brake')

    def left(self, left, right):
        self.forward(-left, right)

    def right(self, left, right):
        self.forward(left, -right)

    def arm_up(self):
        self.arm_motor.run_forever(speed_sp=900)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action='brake')

    def arm_down(self):
        if self.touch_sensor.is_pressed:
            self.arm_motor.run_to_rel_pos(position_sp=-14.2*360, speed_sp=900, stop_action='brake')





    def seek_beacon(self):




    def shoot_soccer_ball(self, left_speed_entry, right_speed_entry):
        self.forward(left_speed_entry, right_speed_entry)
        while True:
            self.pixy.mode = ""