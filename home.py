#!/usr/bin/python -u

from bottle import route, run, template, get, post, request, static_file
import paho.mqtt.client as mqtt
import time

def on_publish(mosq, userdata, mid):
	mosq.disconnect()
print "home.py running at ", time.asctime(time.localtime(time.time()))
client = mqtt.Client()
client.on_publish = on_publish

@route('/')
def index():
	print("serving index.html...")
	return template("/bem/index.html")

@route('/<filename>')
def server_static(filename):
	return static_file(filename, root='/bem/')

@post('/takepic')
def takepic():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if username.lower() == usernamecred and password == passwordcred:	# paste in the actual login credentials
		client.connect(serveripcred)		# paste in the IP of MQTT server (this device)
		client.publish("takepic", "1")
		time.sleep(5)							# Time delay so we dont serve up old pics
		return template("/bem/pic.html")
	else:
		return "<p>Login failed.</p>"

# get credentials
with open("credentials.txt","r") as f:
	serveripcred = f.readline().rstrip()
	usernamecred = f.readline().rstrip()
	passwordcred = f.readline().rstrip()

# run command blocks everything below it
print("about to execute run()")
run(host = '0.0.0.0', port = 80)
