# Zack Watson Final Project for pc

import robot_controller as robo
import time
import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk


class ComputerDelegate(object):

    def __init__(self, location_to_display):
        self.place_to_display = location_to_display


def main():

    root = tkinter.Tk()
    root.title('Zack Watson Final Project GUI')

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    sample_label = ttk.Label(main_frame, text="Zack Watson")
    sample_label.grid(row=0, column=0)

    display_location = ttk.Label(main_frame, text="Robot messages will display here")
    display_location.grid(row=1, column=0)
    
    cd = ComputerDelegate(display_location)
    mqtt_client = com.MqttClient(cd)
    mqtt_client.connect_to_ev3()

    root.mainloop()


main()
