import board
import neopixel
import math
import time

current_milli_time = lambda: round(time.time() * 1000)

pixels = neopixel.NeoPixel(board.D18, 30, brightness=1.0, auto_write=False, pixel_order=neopixel.GRB)

while(1):
   try:
      now = current_milli_time()
      for pixel in range(0,30):
         red = int(math.sin(pixel*10+now/500)*128.00+128)
         blue = int(0.6*(math.sin(-pixel/10-(now/1000.000))*128.00+128))

         # print(red)
         pixels[pixel] = (red, blue, 0)
      pixels.show()
   except:
      pixels.fill((0,0,0))
      pixels.show()
      exit()
