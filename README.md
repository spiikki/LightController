# LightController

(c) Nalleperhe 2020

This system listen for MQTT-messages and sets lighting to desired state.

## System

RaspberryPi, NeoPixel led-strip

## Usage

Copy settings.py.dist to settings.py and configure your mqtt broker settings.
Topics used in client require settings for light and sauna. 

### Setting lighting scene

Topic 'light/1'
'''
{
  "cmd": "set",
  "buffer": [
    [0, 0, 255],
    [255, 0, 0]
  ],
  "rotation" : {
    "enable": "True",
    "speed": 0.2
  }
}
'''
Set rotating two color tween over whole strip


'''
{ "cmd" : "sauna" }
'''
Set sauna-mode on.

