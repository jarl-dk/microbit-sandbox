from microbit import *
import math

steps = 500

hollow_heart = Image.HEART - Image.HEART_SMALL
def show_image(fraction):
    display.show(hollow_heart + Image.HEART_SMALL*(fraction))
    
i = 0
display.clear()
while True:
    if(button_a.is_pressed()):
        fract = (steps/2-abs(i-steps/2))/(steps/2)
    else:
        fract = 0.5+0.5*-math.cos(i*2*math.pi/steps)
    show_image(fract)
    i = (i+1) % steps