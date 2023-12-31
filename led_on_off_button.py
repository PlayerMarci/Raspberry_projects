from machine import Pin
from time import sleep

ledPin = 13
myLed = Pin(ledPin, Pin.OUT)

buttPin=14
myButton=Pin(buttPin, Pin.IN, Pin.PULL_UP)

currButState = 1
prevButState = 1

LEDState = False

while True:
    currButState = myButton.value()
    if currButState == 0 and prevButState == 1:
        LEDState = not LEDState
        myLed.value(LEDState)
    if LEDState:
        print('ON', currButState)
    else:
        print('OFF', currButState)
    prevButState = currButState
    sleep(0.1) 
