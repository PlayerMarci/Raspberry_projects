from machine import Pin
from time import sleep

leds = [12, 11, 10]

Leds = [Pin(leds[2], Pin.OUT), Pin(leds[1], Pin.OUT), Pin(leds[0], Pin.OUT)]

buts = [15, 14, 13]

ButtonR = Pin(buts[2], Pin.IN, Pin.PULL_UP)
ButtonG = Pin(buts[1], Pin.IN, Pin.PULL_UP)
ButtonB = Pin(buts[0], Pin.IN, Pin.PULL_UP)


currButStates = [1,1,1]
prevButStates = [1,1,1]

LEDStates = [False, False, False]

while True:
    currButStates[0] = ButtonR.value()
    if currButStates[0] == 0 and prevButStates[0] == 1:
        LEDStates[0] = not LEDStates[0]
        Leds[0].value(LEDStates[0])
    prevButStates[0] = currButStates[0]
    
    currButStates[1] = ButtonG.value()
    if currButStates[1] == 0 and prevButStates[1] == 1:
        LEDStates[1] = not LEDStates[1]
        Leds[1].value(LEDStates[1])
    prevButStates[1] = currButStates[1]
    
    currButStates[2] = ButtonB.value()
    if currButStates[2] == 0 and prevButStates[2] == 1:
        LEDStates[2] = not LEDStates[2]
        Leds[2].value(LEDStates[2])
    prevButStates[2] = currButStates[2]
    
    sleep(0.1)


