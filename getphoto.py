#!/usr/bin/python

import time
import paho.mqtt.client as mqtt

# message callback, write image to file
def on_message(mosq, obj, msg):
	print("on_message got called")
	with open('out.jpg', 'wb') as fd:
		fd.write(msg.payload)

# set up MQTT client
client = mqtt.Mosquitto("image-rec")
client.connect("server.ip.goes.here")	# paste in the IP of the MQTT server (this device)
client.subscribe("photo",0)
client.on_message = on_message

while True:
	client.loop(15)
	time.sleep(2)
