import threading
import board
import neopixel
import math
import time

current_milli_time = lambda: round(time.time() * 1000)

class lightAdapter:
   pixels = None
   pixelBuffer = None
   running = False
   thread = None

   def __init__(self):
      self.pixels = neopixel.NeoPixel(board.D18, 30, brightness=1.0, auto_write=False, pixel_order=neopixel.GRB)

   def run(self):
      print("Started")
      self.running = True
      while(self.running):
#         try:
         now = current_milli_time()
         for pixel in range(0,30):
            red = 255
            blue = 255
            green = 0
#            red = int(math.sin(pixel*100+now/500)*128.00+128)
#            blue = int(0.6*(math.sin(-pixel/20-(now/500.000))*128.00+128))
#            green = int(0.3*(math.tan((pixel%15)/100)*128.00+128))
            self.pixels[pixel] = (red, blue, green)
         self.pixels.show()
 #        except:
 #           print("MAYDAY MAYDAY, SHUTTING DOWN: ")
 #           self.pixels.fill((0,0,0))
 #           self.pixels.show()
 #           exit()
      print("Stopped")

   def stop(self):
      self.running = False
      self.pixels.fill((0,0,0))
      self.pixels.show()

   def start(self):
      self.thread = threading.Thread(target=self.run)
      self.thread.start()
