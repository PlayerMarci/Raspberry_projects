from machine import PWM, Pin, ADC
from time import sleep

outPin = 16
analogOut = PWM(Pin(outPin))
analogOut.freq(1000) #in ms
analogOut.duty_u16(0)

potPin = 28
myPot = ADC(potPin)

steps = 256
base = 65535 ** (1 / steps)
stepPerMax = (steps / 65535)

while True:
    potVal = myPot.read_u16()    
    expVal = stepPerMax * potVal
    brightness = int(base ** expVal)
    analogOut.duty_u16(brightness)
    
    print(potVal, expVal, brightness)
    
    sleep(0.1)
