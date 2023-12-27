import machine
import time
import math

potPin=28
myPot=machine.ADC(potPin)
prevVal = 0
currVal = 0


while True:
    #because of errors min value is 320 max is 65530
    minimum = 317
    maximum = 65530
    scaleValue = 3.3
    currVal = myPot.read_u16()
    voltage = (scaleValue / maximum) * currVal - (minimum * scaleValue / maximum)
    print(voltage)
    time.sleep(1)
