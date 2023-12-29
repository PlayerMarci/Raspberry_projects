from machine import PWM, Pin
from time import sleep
outPin = 16
analogOut = PWM(Pin(outPin))
analogOut.freq(1000) #in ms
analogOut.duty_u16(0)

while True:
    for i in range(6):
        # ranges for linear: 33 for exponential: 6 
        #myVoltage = float(input("What Voltage would you like?"))
        myVoltage = (2 ** i) / 10
        #myVoltage = (i + 1) / 10
        pwmVal = (65550 / 3.3) * myVoltage
        analogOut.duty_u16(int(pwmVal))
        sleep(0.1) 
