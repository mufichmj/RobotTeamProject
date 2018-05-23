#!/usr/bin/env python3
#Authors: Ashley Shepherd.

import ev3dev.ev3 as ev3
import time

import tkinter
from tkinter import ttk

import robot_controller as robo
import mqtt_remote_method_calls as com
import robot_controller as robot

class DataContainer(object):
    def __init__(self):
        self.running = True

def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    bark_button = ttk.Button(main_frame, text="Bark")
    bark_button.grid(row=3, column=1)
    bark_button['command'] = lambda: send_bark(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: send_bark(mqtt_client, left_speed_entry, right_speed_entry))


    forward_button = ttk.Button(main_frame, text="Go")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    forward_button['command'] = lambda: send_forward(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: send_forward(mqtt_client, left_speed_entry, right_speed_entry))


    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))
    root.bind('<q>', lambda event: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))
    root.bind('<e>', lambda event: quit_program(mqtt_client, True))

    root.mainloop()

    print("Press Back to exit this program.")

    robot = robo.Snatch3r()
    dc = DataContainer()

    btn = ev3.Button()
    btn.on_up = lambda state: check_color(state, robot)
    btn.on_backspace = lambda state: quit_program(mqtt_client, True)

    while dc.running:
        btn.process()
        time.sleep(0.01)

    print("Goodbye!")

def check_color(button_state, robot):

    while(True):
        if robot.color_sensor.color == ev3.ColorSensor.COLOR_GREEN:
            #----------------Make the robot move how you want here-----------------------
            ev3.Sound.speak("Bork Bork Bork").wait()
            robot.stop()
            continue
        if robot.color_sensor.color == ev3.ColorSensor.COLOR_BLUE:
            robot.spin_left_degrees(90, 100, 'brake')
            continue

        if robot.color_sensor.color == ev3.ColorSensor.COLOR_YELLOW:
            robot.spin_right_degrees(90, 100, 'brake')
            continue

        if robot.color_sensor.color == ev3.ColorSensor.COLOR_RED:
            robot.forward(10, 50, 'brake')
            continue


def send_forward(mqtt_client, left_speed_entry, right_speed_entry):
    print("forward")
    left_speed = left_speed_entry.get()
    right_speed = right_speed_entry.get()
    mqtt_client.send_message("forward", [left_speed_entry, right_speed_entry])

def send_bark(mqtt_client, left_speed_entry, right_speed_entry):
    print("bark")
    mqtt_client.send_message("bark")


# Arm command callbacks
def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


# Quit and Exit button callbacks
def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
