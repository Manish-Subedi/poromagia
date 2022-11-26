
# Raspberry Pi as Master and Arduino as Slave (I2C)
# Raspi subscribes to a topic for status of the sorting machine (ON/OFF)
# and also gets the decision (int) from the same topic
# The Raspi then writes the integer to I2C (Arduino) 
# Arduino performs necessary action, puts the card to the respective box. 
# The Arduino, on the other hand, sends a command when the card is on top of the camera. 

# i2cmaster.py
# Author: Manish Subedi

#import time
import json
import paho.mqtt.client as mqtt
from smbus import SMBus

addr = 0x8 #bus address
bus = SMBus(1) # indicates /dev/i2c-1

# The callback for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose  the
        # connection and reconnect, subscriptions will be renewed
        client.subscribe("decision")
    else:
        print("Connection failed with "+str(rc))


# The callback for when a PUBILSH message is received from the server
def on_message(client, userdata, msg):
    # cast to string
    decision = str(msg.payload.decode())
    #decision_ = json.loads(decision)
    #int = decision["int"]
    #print(msg.topic+" "+str(msg.payload))
    print("Json "+type(decision_))
    # Only print the valid decision
    """
    0 means home
    1 means Camera location
    2 means cheap category
    3 means mid-range category
    4 means expensive category
    5 means unidentified cards
    """
    #if int(decision) <= 5 and int(decision) >= 2:
        # write the payload to i2c (Arduino)
     #   bus.write_byte(addr,int(decision))

"""

#read from arduino 
pos = bus.read_byte(addr, 0)
print(pos)
if pos == 1:
   # take picture, [ MELANY, link to the function to take picture ]


"""
# Create an instance 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#provide login credentials
client.username_pw_set(username="friends",password="Wow_manis")
# Connect to the broker
client.connect("hetkinen.ddns.net", 2048, 60)
client.tls_set()
client.loop_forever()
###### EOF ######
