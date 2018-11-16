from microbit import *
import math

boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")
#display.show(boat)
display.clear()

hollow_heart = Image.HEART - Image.HEART_SMALL
steps = 500
i = 0


def show_image(fraction):
    level = math.floor(4.5+0.5+fraction*4.5)
    display.show(hollow_heart+Image.HEART_SMALL*(0.5+0.5*fraction))
#    display.set_pixel(0, 0, level)
#    display.set_pixel(0, 1, level)
#    display.set_pixel(1, 0, level)
#    display.set_pixel(1, 1, level)
    
while True:
    fract = math.cos(i*2*math.pi/float(steps))
    show_image(fract)
    i = (i+1)%steps