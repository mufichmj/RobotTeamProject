import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com

import ev3dev.ev3 as ev3
import time

ir_sensor = ev3.InfraredSensor()
print(ir_sensor.proximity)

