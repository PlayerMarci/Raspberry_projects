from machine import Pin
from time import sleep

leds = [12, 11, 10]

Leds = [Pin(leds[2], Pin.OUT), Pin(leds[1], Pin.OUT), Pin(leds[0], Pin.OUT)]

buts = [15, 14, 13]

Butts = []

ButtonR = Pin(buts[2], Pin.IN, Pin.PULL_UP)
ButtonG = Pin(buts[1], Pin.IN, Pin.PULL_UP)
ButtonB = Pin(buts[0], Pin.IN, Pin.PULL_UP)

Butts.append(ButtonR)
Butts.append(ButtonG)
Butts.append(ButtonB)

currButStates = [1,1,1]
prevButStates = [1,1,1]

LEDStates = [False, False, False]

while True:
    for i in range(0, 3, 1):        
        currButStates[i] = Butts[i].value()
        if currButStates[i] == 0 and prevButStates[i] == 1:
            LEDStates[i] = not LEDStates[i]
            Leds[i].value(LEDStates[i])
        prevButStates[i] = currButStates[i]
    sleep(0.1)
