from lightAdapter import *
from lightBuffer import *
from time import sleep
from collections import deque

hal = lightAdapter()
buffer = lightBuffer()

#buffer = [
#    (255, 200, 0),
#    (200, 255, 0),
#    (225, 225, 0),
#    (125, 125, 0),
#]

buffer.tween((0,0,0),(255,255,0),60)
buffer.tween((255,255,0),(0,0,0),60)

try:
    hal.start()
    while(1):
        hal.loopBuffer(buffer.getBuffer())
        buffer.rotate(-1)
        sleep(0.025)
except KeyboardInterrupt:
    hal.stop()
