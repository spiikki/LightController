from lightAdapter import *
from time import sleep
from collections import deque

hal = lightAdapter()

hal.start()

buffer = [
   (255, 0, 0),
   (255, 155, 0),
   (255, 255, 0),
   (155, 255, 155),
   (0, 155, 255),
   (0, 0, 255),
   (0, 155, 255),
   (155, 255, 155),
   (255, 255, 0),
   (255, 155, 0),
   (255, 0, 0),
]

#hal.loopBuffer(buffer)

try:
   while(1):
      hal.fillBuffer(buffer)
      tmp = deque(buffer)
      tmp.rotate(1)
      buffer = list(tmp)
      sleep(0.25)
except KeyboardInterrupt:
   hal.stop()
