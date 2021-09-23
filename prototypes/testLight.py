import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 6, brightness=1.0, auto_write=True, pixel_order=neopixel.GRB)

pixels[0] = (255, 0, 0)
pixels[1] = (0, 255, 0)
pixels[2] = (0, 0, 255)
pixels[3] = (255, 0, 255)
pixels[4] = (0, 255, 255)
pixels[5] = (255, 255, 0)

