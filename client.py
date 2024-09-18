import jsons
from lightAdapter import *
from lightBuffer import *
import paho.mqtt.client as mqtt
from time import sleep
import settings

hal = lightAdapter()
buffer = lightBuffer()
rotation_speed = 0.04
state = "sauna"

def mqtt_on_connect(client, userdata, flags, rc):
    print("Connected! : "+str(rc))
    client.subscribe(settings.mqtt_light_topic + "/#")
    client.subscribe(settings.mqtt_sauna_topic)

def mqtt_on_message(client, userdata, msg):
    global rotation_speed
    global state
    print(msg.topic + " : ")
    try:
        command = jsons.loads(msg.payload)
        print(command)
        tween_size=1
        if "cmd" in command and command["cmd"] == "set":
            state = "light"
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
                        buffer.toggleRotation(True)
                    else:
                        buffer.toggleRotation(False)
                if "speed" in command["rotation"]:
                    rotation_speed = command["rotation"]["speed"]
        if "cmd" in command and command["cmd"] == "sauna":
            state = "sauna"
        elif "sauna" in msg.topic:
            if "temperature" in command:
                # print(command["temperature"])
                green = 255-(320*(command["temperature"]/100)-17)
                if green > 255:
                    green = 255
                elif green < 0:
                    green = 0

                if state == "sauna":
                    buffer.toggleRotation(False)
                    if command["temperature"] < 6:
                        buffer.set([55, 0, 255])
                    else:
                        buffer.set([255, int(green), 0])

    except:
        print("somethings fucked! don't care! let's go!")

mqtt_client = mqtt.Client(client_id=settings.mqtt_client_id)
mqtt_client.on_connect = mqtt_on_connect
mqtt_client.on_message = mqtt_on_message
mqtt_client.username_pw_set(username=settings.mqtt_user, password=settings.mqtt_pwd)
mqtt_client.connect(settings.mqtt_host, settings.mqtt_port, 30)
mqtt_client.loop_start()

try:
    hal.start()
    while(1):
        hal.loopBuffer(buffer.getBuffer())
        buffer.rotate(-1)
        sleep(rotation_speed)
except KeyboardInterrupt:
    hal.stop()
    mqtt_client.loop_stop()
    mqtt_client.disconnect()

