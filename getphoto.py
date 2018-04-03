#!/usr/bin/python -u

import time
import paho.mqtt.client as mqtt

# message callback, write image to file
def on_message(mosq, obj, msg):
	print("on_message got called")
	with open('/bem/out.jpg', 'wb') as fd:
		fd.write(msg.payload)

# set up MQTT client
print "getphoto.py running at ", time.asctime(time.localtime(time.time()))
# get server ip:
with open("credentials.txt","r") as f:
	serveripcred = f.readline().rstrip()

client = mqtt.Mosquitto("image-rec")
client.connect(serveripcred)	# paste in the IP of the MQTT server (this device)
client.subscribe("photo",0)
client.on_message = on_message

client.loop_forever()
print("getphoto.py code should never get here")

#while True:
#	client.loop(15)
#	time.sleep(2)
