# Brief
Raspberry pi (Master) communicates with Arduino (Slave) via I2C. 
Raspi subscribes to MQTT topic, interfaces with Identifying Algorithm

Raspberry Pi is configured as I2C Master and Arduino as a Slave.

Raspi subscribes to a topic for status of the sorting machine (ON/OFF).
It will then put the Arduino in the respective state.
[ Either START or STOP ]
Arduino will be put into deep sleep state on STOP state.

Raspi also gets the decision (as an integer) from the same topic. 
The integer determines the position of one of the 4 slots where the 
card is to be dropped. The first three will be identified cards and
the last slot would hold the unidentified cards. 

The Raspi then writes the integer to I2C bus (to Arduino)
Arduino performs necessary action, puts the card to the respective box.

The Arduino, on the other hand, sends a command when the card the suction system 
takes a card on top of the camera

.

