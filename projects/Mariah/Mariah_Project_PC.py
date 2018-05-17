
import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote - Soccer Practice!")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    number_of_cones_label = ttk.Label(main_frame, text="Number of Cones")
    number_of_cones_label.grid(row=0, column=1)
    number_of_cones_entry = ttk.Entry(main_frame, width=8)
    number_of_cones_entry.insert(0, "2")
    number_of_cones_entry.grid(row=1, column=0)

    cones_button = ttk.Button(main_frame, text="Run through cones")
    cones_button.grid(row=5, column=1)
    cones_button['command'] = lambda: send_cones(mqtt_client, number_of_cones_entry)
    root.bind('<space>', lambda event: send_cones(mqtt_client, number_of_cones_entry))



    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "400")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "400")
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: send_forward(mqtt_client,
                                                     left_speed_entry,
                                                     right_speed_entry)
    root.bind('<Up>', lambda event: send_forward(mqtt_client,
                                                 left_speed_entry,
                                                 right_speed_entry))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: send_left(mqtt_client,
                                               left_speed_entry,
                                               right_speed_entry)
    root.bind('<Left>', lambda event: send_left(mqtt_client, left_speed_entry,
                                                right_speed_entry))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: send_stop(mqtt_client)
    root.bind('<a>', lambda event: send_stop(mqtt_client))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: send_right(mqtt_client,
                                                 left_speed_entry,
                                                 right_speed_entry)
    root.bind('<Right>', lambda event: send_right(mqtt_client,
                                                  left_speed_entry,
                                                  right_speed_entry))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: send_back(mqtt_client,
                                               left_speed_entry,
                                               right_speed_entry)
    root.bind('<Down>', lambda event: send_back(mqtt_client,
                                                left_speed_entry,
                                                right_speed_entry))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<u>', lambda event: send_up(mqtt_client))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<j>', lambda event: send_down(mqtt_client))

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))
    root.mainloop()


def send_cones(mqtt_client, number_of_cones_entry):
    print("Lets play soccer")
    number_of_cones = number_of_cones_entry.get()
    number_of_cones = int(number_of_cones) / 2
    mqtt_client.send_message("go_through_cones", [int(number_of_cones)])


def send_left(mqtt_client, left_speed_entry, right_speed_entry):
    print("left")
    mqtt_client.send_message("shoot_soccer_ball", [-int(left_speed_entry.get()),
                                               int(right_speed_entry.get())])


def send_right(mqtt_client, left_speed_entry, right_speed_entry):
    print("right")
    mqtt_client.send_message("shoot_soccer_ball", [int(left_speed_entry.get()),
                                       -int(right_speed_entry.get())])


def send_forward(mqtt_client, left_speed_entry, right_speed_entry):
    print("forward")
    mqtt_client.send_message("shoot_soccer_ball", [int(left_speed_entry.get()),
                                           int(right_speed_entry.get())])




def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("hand_ball")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("yellow_card")





def send_back(mqtt_client, left_speed_entry, right_speed_entry):
    print("backward")
    mqtt_client.send_message("backward", [int(left_speed_entry.get()),
                                          int(right_speed_entry.get())])


def send_stop(mqtt_client):
    print("stop")
    mqtt_client.send_message("stop")


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


main()