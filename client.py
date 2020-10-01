from lightAdapter import *
from time import sleep
from collections import deque

hal = lightAdapter()

hal.start()

buffer = [
   (255, 200, 0),
   (200, 255, 0),
   (225, 225, 0),
   (125, 125, 0),
]

#hal.loopBuffer(buffer)

try:
   while(1):
      hal.loopBuffer(buffer)
      tmp = deque(buffer)
      tmp.rotate(1)
      buffer = list(tmp)
      sleep(0.25)
except KeyboardInterrupt:
   hal.stop()
