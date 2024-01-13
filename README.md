# LightController

(c) Nalleperhe 2020

This system listen for MQTT-messages and sets lighting to desired state.

## System

RaspberryPi, NeoPixel led-strip

## Usage

Copy settings.py.dist to settings.py and configure your mqtt broker settings.
Topics used in client require settings for light and sauna. 

### Setting lighting scene

Topic `light/1`

Set rotating two color tween over whole strip
```json
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
```

Set sauna-mode on.
```json
{ "cmd" : "sauna" }
```

### Sauna-mode

Expecting `sensor/sauna` topic to receive sauna-status in format:

```json
{ "temperature" : 22.5 }
```
