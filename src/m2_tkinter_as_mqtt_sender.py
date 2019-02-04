"""
Using a fake robot as the receiver of messages.
"""

# DONE: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.

# DONE: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.


import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time


def main():
    """ Constructs a GUI that will be used MUCH later to control EV3. """
    # -------------------------------------------------------------------------
    # DONE: 2. DO NOT follow along with the video to make a remote control GUI
    # For every grid() method call you will add a row and a column argument
    # -------------------------------------------------------------------------
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    # LEFT ENTRY
    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=1, column=1)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=2, column=1)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=1, column=3)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=2, column=3)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=3, column=2)

    forward_button['command'] = lambda: forward(left_speed_entry, right_speed_entry, mqtt_client)
    root.bind('<Up>', lambda event: print("Forward key"))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=4, column=1)
    left_button['command'] = lambda: print("Left button")
    root.bind('<Left>', lambda event: print("Left key"))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=4, column=2)
    stop_button['command'] = lambda: stop(mqtt_client)
    root.bind('<space>', lambda event: print("Stop key"))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=4, column=3)
    right_button['command'] = lambda: print("Right button")
    root.bind('<Right>', lambda event: print("Right key"))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=5, column=2)
    back_button['command'] = lambda: backward(left_speed_entry, right_speed_entry, mqtt_client)
    root.bind('<Down>', lambda event: print("Back key"))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=6, column=1)
    up_button['command'] = lambda: print("Up button")
    root.bind('<u>', lambda event: print("Up key"))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=7, column=1)
    down_button['command'] = lambda: print("Down button")
    root.bind('<j>', lambda event: print("Down key"))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=6, column=3)
    q_button['command'] = lambda: print("Quit button")

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=7, column=3)
    e_button['command'] = lambda: exit()

    root.mainloop()


def forward(left_speed_entry, right_speed_entry, client):
    left_speed = left_speed_entry.get()
    right_speed = right_speed_entry.get()
    client.send_message("forward", [left_speed, right_speed])


def backward(left_speed_entry, right_speed_entry, client):
    left_speed = - left_speed_entry.get()
    right_speed = - right_speed_entry.get()
    client.send_message("backward", [left_speed, right_speed])


def stop(client):
    client.send_message("stop")

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------


main()
