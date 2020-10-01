import threading
import board
import neopixel
import math
import time

current_milli_time = lambda: round(time.time() * 1000)

class lightAdapter:
   pixels = None
   pixelBuffer = []
   running = False
   thread = None
   pixelsAmount = 30

   def __init__(self):
      self.pixels = neopixel.NeoPixel(board.D18, self.pixelsAmount, brightness=1.0, auto_write=False, pixel_order=neopixel.GRB)
      for i in range(0, self.pixelsAmount):
          self.pixelBuffer.append((0,0,0))
      print(len(self.pixelBuffer))

   def run(self):
      print("Started")
      self.running = True
      while(self.running):
         now = current_milli_time()
         for pixel in range(0, self.pixelsAmount):
            self.pixels[pixel] = self.pixelBuffer[pixel] #(red, blue, green)
         self.pixels.show()
      print("Stopped")

   def stop(self):
      self.running = False
      self.thread.join()
      self.pixels.fill((0,0,0))
      self.pixels.show()

   def start(self):
      self.thread = threading.Thread(target=self.run)
      self.thread.start()

   def fillBuffer(self, pattern):
      increment = len(pattern) / self.pixelsAmount
      for i in range(0, self.pixelsAmount):
         self.pixelBuffer[i] = pattern[int(i*increment)]

   def loopBuffer(self, pattern):
      for i in range(0, self.pixelsAmount):
         self.pixelBuffer[i] = pattern[i%len(pattern)]
