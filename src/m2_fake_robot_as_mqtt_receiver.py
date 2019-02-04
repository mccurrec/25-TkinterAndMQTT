# DONE: Copy the code in
#     m1e_mqtt_receiver.py
# as your starting point, pasting its code here.


import mqtt_remote_method_calls as com
import time


class Delegate(object):

    def backward(self, ):
        print('Backward', message[0], message[1])

    def forward(self, message):
        print('Forward', message[0], message[1])

def main():
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    delegate = Delegate()
    mqtt_client = com.MqttClient(delegate)
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    while True:
        time.sleep(0.01)  # Time to allow message processing


main()

# Then modify the code so that it receives messages from your
#    m2_tkinter_as_mqtt_sender.py
# module and PRINTS them.

