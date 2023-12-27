import machine
import time
import math

potPin=28
myPot=machine.ADC(potPin)
prevVal = 0
currVal = 0


while True:
    currVal = math.floor(myPot.read_u16() / (2 ** 8))
    if (abs(prevVal - currVal) >= 4):
        prevVal = currVal
        print(prevVal)
        print(currVal)
