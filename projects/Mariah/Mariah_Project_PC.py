
import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com




def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")
    # mqtt =
    #     connect
    #
    #
    # make a QUI
    #
    # respond to GUI
    # send messages