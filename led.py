port board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 120, brightness=1)
for i in range(10):
    pixels.fill((255, 255, 255))
    time.sleep(5)
    pixels.fill((0, 0, 0))
    time.sleep(1) 
