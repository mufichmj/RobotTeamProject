
import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote - Mariah CSSE Project")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    number_of_cones_label = ttk.Label(main_frame, text="Number of Cones")
    number_of_cones_label.grid(row=0, column=0)
    number_of_cones_entry = ttk.Entry(main_frame, width=8)
    number_of_cones_entry.insert(0, "2")
    number_of_cones_entry.grid(row=1, column=0)

    cones_button = ttk.Button(main_frame, text="Run through cones!")
    cones_button.grid(row=2, column=0)
    cones_button['command'] = lambda: send_cones(mqtt_client, number_of_cones_entry)
    root.bind('<Up>', lambda event: send_cones(mqtt_client, number_of_cones_entry))

    root.mainloop()


def send_cones(mqtt_client, number_of_cones_entry):
    number_of_cones = number_of_cones_entry.get()
    number_of_cones = int(number_of_cones) / 2
    mqtt_client.send_message('go_through_cones', [int(number_of_cones)])


main()