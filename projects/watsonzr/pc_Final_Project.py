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
    cd = ComputerDelegate()
    mqtt_client = com.MqttClient(cd)
    mqtt_client.connect_to_ev3()


main()
