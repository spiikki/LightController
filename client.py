import jsons
from lightAdapter import *
from lightBuffer import *
import paho.mqtt.client as mqtt
from time import sleep

hal = lightAdapter()
buffer = lightBuffer()
rotation = False
rotation_speed = 0.04

def mqtt_on_connect(client, userdata, flags, rc):
    print("Connected! : "+str(rc))
    client.subscribe("light/1/#")

def mqtt_on_message(client, userdata, msg):
    print(msg.topic + " : ")
    command = jsons.loads(msg.payload)
    print(command)
    tween_size=1
    if command["cmd"] == "set":
        if "tween_size" in command:
            tween_size=command["tween_size"]
        if len(command["buffer"]) < 2:
            buffer.set(command["buffer"][0])
        else:
            if (len(command["buffer"])*tween_size) < 30:
                tween_size = int(30/(len(command["buffer"])-1))+1
            buffer.clearBuffer()
            for set in range(0, len(command["buffer"])-1):
                buffer.tween(command["buffer"][set], command["buffer"][set+1], tween_size)
        if "rotation" in command:
            if "enable" in command["rotation"]:
                if command["rotation"]["enable"] == "True":
                    rotation = True
                else:
                    rotation = False
            if "speed" in command["rotation"]:
                rotation_speed = command["rotation"]["speed"]

mqtt_client = mqtt.Client()
mqtt_client.on_connect = mqtt_on_connect
mqtt_client.on_message = mqtt_on_message
mqtt_client.connect("192.168.1.148", 1883, 30)
mqtt_client.loop_start()


# buffer.tween((0,0,0),(0,255,0),10)
# buffer.tween((0,255,0),(0,250,0),10)
# buffer.tween((0,250,0),(0,250,0),10)
# buffer.tween((0,250,0),(0,0,0),10)

try:
    hal.start()
    while(1):
        hal.loopBuffer(buffer.getBuffer())
        if rotation:
            buffer.rotate(-1)
        sleep(rotation_speed)
except KeyboardInterrupt:
    hal.stop()
    mqtt_client.loop_stop()
    mqtt_client.disconnect()

