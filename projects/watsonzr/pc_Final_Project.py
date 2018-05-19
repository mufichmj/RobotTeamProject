# Zack Watson Final Project for pc

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk


class ComputerDelegate(object):

    def __init__(self, location_to_display):
        self.place_to_display = location_to_display


def main():

    root = tkinter.Tk()
    root.title('DancerBot 5000')

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    sample_label = ttk.Label(main_frame, text="Make me Dance!")
    sample_label.grid(row=0, column=2)

    moonwalk_button = ttk.Button(main_frame, text="Moonwalk")
    moonwalk_button.grid(row=1, column=0)
    moonwalk_button['command'] = lambda: send_moonwalk(mqtt_client)

    square_dance_button = ttk.Button(main_frame, text="Square Dance")
    square_dance_button.grid(row=1, column=1)
    square_dance_button['command'] = lambda: send_sqd(mqtt_client)

    waltz_button = ttk.Button(main_frame, text="Waltz")
    waltz_button.grid(row=1, column=2)
    waltz_button['command'] = lambda: send_waltz(mqtt_client)

    whip_nay_button = ttk.Button(main_frame, text="Whip & Nae-Nae")
    whip_nay_button.grid(row=1, column=3)
    whip_nay_button['command'] = lambda: send_silento(mqtt_client)

    hands_up_button = ttk.Button(main_frame, text="Hands Up")
    hands_up_button.grid(row=1, column=4)
    hands_up_button['command'] = lambda: send_hands_up(mqtt_client)

    arm_down_button = ttk.Button(main_frame, text="Arm Down")
    arm_down_button.grid(row=2, column=0)
    arm_down_button['command'] = lambda: send_arm_down(mqtt_client)

    display_location = ttk.Label(main_frame, text="Waiting...")
    display_location.grid(row=2, column=2)

    exit_button = ttk.Button(main_frame, text="Exit")
    exit_button.grid(row=2, column=4)
    exit_button['command'] = lambda: send_exit(mqtt_client)

    cd = ComputerDelegate(display_location)
    mqtt_client = com.MqttClient(cd)
    mqtt_client.connect_to_ev3()

    root.mainloop()


def send_moonwalk(mqtt_client):
    mqtt_client.send_message('moonwalk')


def send_waltz(mqtt_client):
    mqtt_client.send_message('waltz')


def send_sqd(mqtt_client):
    mqtt_client.send_message('square_dance')


def send_silento(mqtt_client):
    mqtt_client.send_message('whip_nae_nae')


def send_hands_up(mqtt_client):
    mqtt_client.send_message('hands_up')


def send_arm_down(mqtt_client):
    mqtt_client.send_message('arm_down')


def send_exit(mqtt_client):
    mqtt_client.send_message('exit')
    mqtt_client.close()
    exit()


main()
