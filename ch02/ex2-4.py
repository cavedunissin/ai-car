
from Tkinter import *
from Adafruit_PWM_Servo_Driver import PWM
import time
import os
import random

# Initialise the PWM device using the default address
pwm = PWM(0x40)
pwm.setPWMFreq(50)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

shortdelay=1
DELAY = 0.2

def setServoPulse(channel, angle):

    pulse = 700+ (angle*9.45)
    
    if pulse > 2400:
        pulse =2400
    elif pulse <700:
        pulse =700

    print ("pulse = %d " % (pulse))
    output_duty_cycle = int(pulse) * 4096 / 20000
    print ("output_duty_cycle = %d per 12bits" % (output_duty_cycle))
    pwm.setPWM(channel, 0, output_duty_cycle)

class App:		

    def __init__(self, master):	
        frame = Frame(master)	
        frame.pack()
        scale = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.servo1)	
        scale.grid(row=0)				

        scale = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.servo2)	
        scale.grid(row=1)				

        scale = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.servo3)	
        scale.grid(row=2)				

        scale = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.servo4)
        scale.grid(row=3)


    def servo1(self, angle):
        print ("Servo %d angle:  %d" % (0, int(angle)))
        setServoPulse(0, int(angle))

    def servo2(self, angle):
        print ("Servo %d angle:  %d" % (1, int(angle)))
        setServoPulse(1, int(angle))

    def servo3(self, angle):
        print ("Servo %d angle:  %d" % (2, int(angle)))
        setServoPulse(2, int(angle))

    def servo4(self, angle):
        print ("Servo %d angle:  %d" % (3, int(angle)))
        setServoPulse(3, int(angle))


root = Tk()						
root.wm_title('Servo Control')				
app = App(root)						
root.geometry("200x200+0+0")				
root.mainloop()						
