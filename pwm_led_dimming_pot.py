from machine import PWM, Pin, ADC
from time import sleep
outPin = 16
analogOut = PWM(Pin(outPin))
analogOut.freq(1000) #in ms
analogOut.duty_u16(0)

potPin = 28
myPot = machine.ADC(potPin)

while True:
    potVal = myPot.read_u16()
    pwmVal = potVal
    analogOut.duty_u16(int(pwmVal))
    sleep(0.1)
