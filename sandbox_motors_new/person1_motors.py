"""
Functions for moving the robot FORWARD and BACKWARD.
Authors: David Fisher, David Mutchler and Mariah Mufich.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implment forward_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for forward_by_time.
#   Then repeat for forward_by_encoders.
#   Then repeat for the backward functions.

import ev3dev.ev3 as ev3
import time


def test_forward_backward():
    """
    Tests the forward and backward functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets inches and runs forward_by_time.
      3. Same as #2, but runs forward_by_encoders.
      4. Same as #1, 2, 3, but tests the BACKWARD functions.
    """
    print()
    print('Testing turn_left_seconds')

    while True:
        time_s = float(input("Enter a time to move forward (seconds): "))
        if time_s == 0:
            break
        speed_percent = float(input("Enter a speed percentage (0 to 100%): "))
        stop_act = str(input("Enter a stop action (brake, coast, or hold): "))
        forward_seconds(time_s, speed_percent, stop_act)

    print()
    print('--------------------------------------')
    print('Testing turn_left_by_time')

    while True:
        degrees = float(input("Enter inches to move forward: "))
        if degrees == 0:
            break
        speed_percent = float(input("Enter a speed percentage (0 to 100 %): "))
        stop_act = str(input("Enter a stop action (brake, coast, or hold): "))
        forward_by_time(degrees, speed_percent, stop_act)

    print()
    print('--------------------------------------')
    print('Testing turn_left_by_encoders')

    while True:
        degrees = float(input("Enter inches to move forward: "))
        if degrees == 0:
            break
        speed_percent = float(input("Enter a speed percentage (0 to 100 %): "))
        stop_act = str(input("Enter a stop action (brake, coast, or hold): "))
        forward_by_encoders(degrees, speed_percent, stop_act)
        print()

    print()
    print('--------------------------------------')
    print('Testing turn_right_seconds')

    while True:
        time_s = float(input("Enter a time to move backward (seconds): "))
        if time_s == 0:
            break
        speed_percent = float(input("Enter a speed percentage (0 to 100 %): "))
        stop_act = str(input("Enter a stop action (brake, coast, or hold): "))
        backward_seconds(time_s, speed_percent, stop_act)

    print()
    print('--------------------------------------')
    print('Testing turn_right_by_time')

    while True:
        degrees = float(input("Enter inches to move backward: "))
        if degrees == 0:
            break
        speed_percent = float(input("Enter a speed percentage (0 to 100 %): "))
        stop_act = str(input("Enter a stop action (brake, coast, or hold): "))
        backward_by_time(degrees, speed_percent, stop_act)

    print()
    print('--------------------------------------')
    print('Testing turn_right_by_encoders')

    while True:
        degrees = float(input("Enter inches to move backward: "))
        if degrees == 0:
            break
        speed_percent = float(input("Enter a speed percentage (0 to 100 %): "))
        stop_act = str(input("Enter a stop action (brake, coast, or hold): "))
        backward_by_encoders(degrees, speed_percent, stop_act)

    print()
    print('--------------------------------------')



def forward_seconds(seconds, speed, stop_action):
    """
    Makes the robot move forward for the given number of seconds at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the given stop_action.
    """
    # Connect two large motors on output ports B and C
    left_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_B)

    # Check that the motors are actually connected
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp=speed*8, stop_action=stop_action)
    right_motor.run_forever(speed_sp=speed * 8, stop_action=stop_action)
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop()


def forward_by_time(inches, speed, stop_action):
    """
    Makes the robot move forward the given number of inches at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp=speed * 8, stop_action=stop_action)
    right_motor.run_forever(speed_sp=speed * 8, stop_action=stop_action)
    time.sleep(inches/(abs(speed)*0.085))
    left_motor.stop()
    right_motor.stop()


def forward_by_encoders(inches, speed, stop_action):
    """
    Makes the robot move forward the given number of inches at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should spin to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp=speed * 8, stop_action=stop_action)
    right_motor.run_forever(speed_sp=speed * 8, stop_action=stop_action)
    time.sleep(inches/(abs(speed)*.085))
    left_motor.stop()
    right_motor.stop()

def backward_seconds(seconds, speed, stop_action):
    """ Calls forward_seconds with negative speeds to achieve backward motion. """

    forward_seconds(seconds, -speed, stop_action)

def backward_by_time(inches, speed, stop_action):
    """ Calls forward_by_time with negative speeds to achieve backward motion. """

    forward_by_time(inches, -speed, stop_action)

def backward_by_encoders(inches, speed, stop_action):
    """ Calls forward_by_encoders with negative speeds to achieve backward motion. """

    forward_by_encoders(inches, -speed, stop_action)

test_forward_backward()