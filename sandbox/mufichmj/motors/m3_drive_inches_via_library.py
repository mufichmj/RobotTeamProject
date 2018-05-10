#!/usr/bin/env python3
"""
This module lets you practice refactoring code to use a shared library.  The code in this file is already finished.
The team should work together and pick one team member to type code into libs/robot_controller.py to create a
constructor and a method called drive_inches.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. On your computer right click on the libs folder in PyCharm, select Mark Directory as... Sources Root
#   That should fix the error on the import robot_controller as robo line below (expand the imports below)
#   Marking that folder as a Source Root will allow any module in that folder to be used globally in this project.
#   Note, when that folder is uploaded to the EV3, it wil be in the folder /home/robot/csse120/libs
#   That folder path is special on your robot because it is set as the PYTHONPATH (done within the .bashrc file)
#   Normally you can't just use a module in some random folder, but the libs folder has been setup special.

# TODO: 3. Have everyone talk about this problem together then pick one team member to modify libs/robot_controller.py
# as necessary to make the code below perform the same task as the prior module. As mentioned in the top doc-string for
# the file, you may not modify the code below.  Warning, make sure you UPLOAD the library to the robot before running
# this module.
#
# Once the code has been tested and shown to work, then have that person commit their work.  All other team members need
#  to do a VCS --> Update project...
# Once the library is implemented each team member should be able to run their version of this code on the robot.

# TODO: 4. Formally test your work. When you think you have the problem complete run these tests:
#   500 dps 24 inches
#   500 dps -24 inches
#   Should work exactly as before with these tests and more.  It should beep after the movement is over.

# TODO: 5. Call over a TA or instructor to sign your team's checkoff sheet and do a code review of your library.
#
# Observations you should make, you are a TEAM and making great library methods will make life easier for everyone.

import ev3dev.ev3 as ev3
import robot_controller as robo
from PIL import Image

def main():
    # --------------------------------------------------------------
    # We have already implemented this module for you.
    # There are no TODOs in the code.  Do NOT modify it.
    # You are not allowed to make any changes to this code.
    # --------------------------------------------------------------
    print("--------------------------------------------")
    print(" Drive inches")
    print("--------------------------------------------")
    ev3.Sound.speak("Drive inches").wait()
    robot = robo.Snatch3r()

    while True:
        speed_deg_per_second = int(input("Speed (0 to 900 dps): "))
        if speed_deg_per_second == 0:
            break
        inches_target = int(input("Distance (inches): "))
        if inches_target == 0:
            break

        robot.forward(inches_target, speed_deg_per_second)
        ev3.Sound.beep().wait()  # Fun little beep

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()

def show_leds():

    button = ev3.Button
    led = ev3.Led
    while True:
        if button.left:
            led.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        if button.right:
            led.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
        if button.up:
            led.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER)
        if button.down:
            led.set_color(ev3.Leds.all_off())
        if button.backspace:
                break

def make_sounds():

    rc3 = ev3.RemoteControl(channel=3)
    assert rc3.connected

    while True:
        if rc3.red_up:
            ev3.Sound.beep().wait()
        if rc3.red_down:
            ev3.Sound.speak('Rose-Hulman Institute of Technology').wait()
        if rc3.blue_up:
            ev3.Sound.play("/home/robot/csse120/assets/sounds/awesome_pcm.wav").wait()
        if rc3.blue_down:
            break

def make_image():

    lcd_screen = ev3.Screen()

    image = Image.open("/home/robot/csse120/assets/images/ev3_lego/eyes_angry.bmp")

    x_location = 0
    y_location = 0
    lcd_screen.image.paste(image,(x_location, y_location))
    lcd_screen.update()



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
