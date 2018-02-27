
#!/usr/bin/python

from bottle import route, run, template, get, post, request, static_file
import paho.mqtt.client as mqtt
import time

def on_publish(mosq, userdata, mid):
	mosq.disconnect()

client = mqtt.Client()
client.on_publish = on_publish

@route('/')
def index():
	return template("index.html")

@route('/<filename>')
def server_static(filename):
	return static_file(filename, root='./')

@post('/takepic')
def takepic():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if username.lower() == 'USERNAME' and password == 'PASS':	# paste in the actual login credentials
		client.connect('server ip')		# paste in the IP of MQTT server (this device)
		client.publish("takepic", "1")
		time.sleep(5)							# Time delay so we dont serve up old pics
		return template("pic.html")
	else:
		return "<p>Login failed.</p>"

# run command blocks everything below it
run(host = '0.0.0.0', port = 80)
