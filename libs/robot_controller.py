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

        assert self.left_motor.connected
        assert self.right_motor.connected

    def forward(self, inches, speed=100, stop_action='brake'):

        k = 360 / 4.1
        degrees_motor = k * inches
        self.left_motor.run_to_rel_pos(position_sp=degrees_motor, speed_sp=8*speed, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=degrees_motor, speed_sp=8*speed, stop_action=stop_action)
        self.left_motor.wait_while('running')
        self.right_motor.wait_while('running')

    def backward(self, inches, speed=100, stop_action='brake'):

        self.forward(inches, -speed, stop_action)

    def spin_left(self, degrees, speed=100, stop_action='brake'):
        
        k = 4
        new_degrees = (k * degrees)
        self.left_motor.run_to_rel_pos(speed_sp=-speed*8, position_sp=-new_degrees, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(speed_sp=speed*8, position_sp=new_degrees, stop_action=stop_action)
        self.left_motor.wait_while('running')
        self.right_motor.wait_while('running')

    def spin_right(self, degrees, speed=100, stop_action='brake'):

        self.spin_left(degrees, -speed, stop_action)

    def turn_left(self, degrees, speed=100, stop_action='brake'):

        pass

    def turn_right(self, degrees, speed=100, stop_action='brake'):

        self.turn_left(degrees, -speed, stop_action)
