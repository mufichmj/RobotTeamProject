import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


class PicToLaptop(object):
    def bone(self):
        """Makes a tkinter window that shows a bone when the robot has done its trick. It acts as button, and when
        pressed it prints a message from the python console"""
        root = tkinter.Toplevel()

        photo = tkinter.PhotoImage(file='dog_treats')

        button = ttk.Button(root, image=photo)

        button.image = photo
        button.grid()
        button['command'] = lambda: print('Good boy!')


def main():
    ev3tocomp = PicToLaptop
    mqtt_client = com.MqttClient(ev3tocomp)
    mqtt_client.connect_to_ev3()
    root = tkinter.Tk()
    root.title("Doggo Controller")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    doggo_left_speed_label = ttk.Label(main_frame, text="Left paw zoom")
    doggo_left_speed_label.grid(row=0, column=0)
    doggo_left_speed_entry = ttk.Entry(main_frame, width=10)
    doggo_left_speed_entry.insert(0, "800")
    doggo_left_speed_entry.grid(row=1, column=0)

    doggo_right_speed_label = ttk.Label(main_frame, text="Right paw zoom")
    doggo_right_speed_label.grid(row=0, column=2)
    doggo_right_speed_entry = ttk.Entry(main_frame, width=10, justify=tkinter.RIGHT)
    doggo_right_speed_entry.insert(0, "800")
    doggo_right_speed_entry.grid(row=1, column=2)

    doggo_zoom_forward_button = ttk.Button(main_frame, text="zoomin Forward")
    doggo_zoom_forward_button.grid(row=2, column=1)
    doggo_zoom_forward_button['command'] = lambda: send_doggo_forward(mqtt_client, doggo_left_speed_entry,
                                                                      doggo_right_speed_entry)
    root.bind('<Up>', lambda event: send_doggo_forward(mqtt_client, doggo_left_speed_entry,
                                                       doggo_right_speed_entry))

    doggo_stop_button = ttk.Button(main_frame, text="Hooman said stop")
    doggo_stop_button.grid(row=3, column=1)
    doggo_stop_button['command'] = lambda: send_doggo_stop(mqtt_client)
    root.bind('<space>', lambda event: send_doggo_stop(mqtt_client))

    doggo_bark_button = ttk.Button(main_frame, text="Barking loud!")
    doggo_bark_button.grid(row=5, column=1)
    doggo_bark_button['command'] = lambda: doggo_bark(mqtt_client)
    root.bind('<Down>', lambda event: doggo_bark(mqtt_client))

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))
    root.bind('<q>', lambda event: quit_program(mqtt_client, False))

    bye_hooman_button = ttk.Button(main_frame, text="Bye")
    bye_hooman_button.grid(row=6, column=1)
    bye_hooman_button['command'] = (lambda: quit_program(mqtt_client, True))
    root.bind('<e>', lambda event: quit_program(mqtt_client, True))

    check_color_button = ttk.Button(main_frame, text="Checking color")
    check_color_button.grid(row=4, column=1)
    check_color_button['command'] = (lambda: doggo_look_at_color(mqtt_client))
    root.bind('<c>', lambda event: doggo_look_at_color(mqtt_client))

    root.mainloop()

    print("Bye hooman!")


def send_doggo_forward(mqtt_client, doggo_left_speed_entry, doggo_right_speed_entry):
    print("zoom_forward")
    left_speed = doggo_left_speed_entry.get()
    right_speed = doggo_right_speed_entry.get()
    mqtt_client.send_message("zoom_forward", [int(left_speed), int(right_speed)])

def doggo_bark(mqtt_client):
    print("doggo bark")
    mqtt_client.send_message("doggo_bark")


def send_doggo_stop(mqtt_client):
    print("doggo_stop")
    mqtt_client.send_message("doggo_stop")

# code from here up makes a GUI that sends the dog forward, stops it, and exits


def doggo_look_at_color(mqtt_client):
    print("check_color")
    mqtt_client.send_message("check_color")


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()
# code above here makes the robot see a color and do a trick


main()
