from flask import Flask, request, render_template
from lightAdapter import *
from lightBuffer import *

import settings

hal = lightAdapter()
buffer = lightBuffer()
rotation_speed = 0.04
state = "light"
processing_message = False

hal.start()

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/set", methods=["POST"])
def set_buffer():
#	print(request.json["buffer"])
	tween_size = 1
	command = request.json
	if "tween_size" in command:
		tween_size=command["tween_size"]

	if len(command["buffer"]) == 1:
		print(command["buffer"][0])
		buffer.set(command["buffer"])
	else:
		if (len(command["buffer"])*tween_size) < settings.pixel_amount:
			tween_size = int(settings.pixel_amount/(len(command["buffer"])-1))+1
		print("buffer size", len(command["buffer"]), "tween size", tween_size, "settings.pixels" , settings.pixel_amount)
		buffer.clearBuffer()
		for set in range(0, len(command["buffer"])-1):
			buffer.tween(command["buffer"][set], command["buffer"][set+1], tween_size)
		print("new buffer: ", buffer)
	if "rotation" in command:
		if "enable" in command["rotation"]:
			if command["rotation"]["enable"] == "True":
				buffer.toggleRotation(True)
			else:
				buffer.toggleRotation(False)
		if "speed" in command["rotation"]:
			rotation_speed = command["rotation"]["speed"]
	hal.loopBuffer(buffer.getBuffer())
	return { "status":"200" }

@app.route("/state", methods=["GET"])
def current_status():
	return { "buffer" : [ [0,0,0], [255,0,0], [0,0,255] ] }


#@app.teardown_appcontext
#def die(exception):
#	hal.stop()
