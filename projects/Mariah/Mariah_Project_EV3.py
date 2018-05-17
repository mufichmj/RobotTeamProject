import time

import mqtt_remote_method_calls as com
import robot_controller as robo


class Robot(object):
    def __init__(self):
        self.robot = robo.Snatch3r()


    def loop_forever(self):
        self.robot.loop_forever()


    def go_through_cones(self, number_cones):
        for k in range(number_cones):
            self.robot.forward(400, 400)
            time.sleep(4)
            self.robot.stop()
            self.robot.spin_left_degrees(90)
            self.robot.forward(400, 400)
            time.sleep(4)
            self.robot.stop()
            self.robot.spin_right_degrees(90)
            self.robot.forward(400, 400)
            time.sleep(4)
            self.robot.stop()
            self.robot.spin_right_degrees(90)
            self.robot.forward(400, 400)
            time.sleep(4)
            self.robot.stop()
            self.robot.spin_left_degrees(90)



    def shoot_soccer_ball(self, left_speed_entry, right_speed_entry):
        self.forward(left_speed_entry, right_speed_entry)
        while True:
            self.pixy.mode = ""


    def goal(self):
        root1 = tkinter.Toplevel()

        photo = tkinter.PhotoImage(file='http://www.cbelmira.com/blog/hs-boys-soccer-late-goals-hurt-oneonta-in-3-2-state-loss/')
        button1 = ttk.Button(root1, image=photo)

        button1.image = photo
        button1.grid()
        button1['command'] = lambda: print('Goal, you win!')



    def hand_ball(self):


    def yellow_card(self):



def main():
    delegate = Robot()
    mqtt_client = com.MqttClient(delegate)
    mqtt_client.connect_to_pc()

    delegate.loop_forever()


main()

