from lightAdapter import *
from lightBuffer import *
from time import sleep

hal = lightAdapter()
buffer = lightBuffer()

buffer.tween((0,0,0),(0,255,0),10)
buffer.tween((0,255,0),(0,250,0),10)
buffer.tween((0,250,0),(0,250,0),10)
buffer.tween((0,250,0),(0,0,0),10)

try:
    hal.start()
    while(1):
        hal.loopBuffer(buffer.getBuffer())
        buffer.rotate(-1)
        sleep(0.04)
except KeyboardInterrupt:
    hal.stop()
