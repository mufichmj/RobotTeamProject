import tkinter
from tkinter import ttk

import ev3dev.ev3 as ev3
import time

import mqtt_remote_method_calls as com
import robot_controller as robo



ir_sensor = ev3.InfraredSensor()
print(ir_sensor.proximity)

def Main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()

    robot.loop_forever()
    # mqtt = .....(robot)
    #  connect
    #
    # loop
    #