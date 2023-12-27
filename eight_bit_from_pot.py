import machine
import utime
import math

led0 = machine.Pin(6, machine.Pin.OUT)
led1 = machine.Pin(7, machine.Pin.OUT)
led2 = machine.Pin(8, machine.Pin.OUT)
led3 = machine.Pin(9, machine.Pin.OUT)

led4 = machine.Pin(10, machine.Pin.OUT)
led5 = machine.Pin(11, machine.Pin.OUT)
led6 = machine.Pin(12, machine.Pin.OUT)
led7 = machine.Pin(13, machine.Pin.OUT)

bin_digits = []

potPin = 28
myPot = machine.ADC(potPin)
prevVal = 0
currVal = 0

def dec_to_bin(num):
     for i in range(8):
        if (num > 0):
            if (num % 2 == 0):
             bin_digits.insert(0, 0)
             num = num / 2
            else:
                bin_digits.insert(0, 1)
                num = num - 1
                num = num / 2
        else:
            bin_digits.insert(0, 0)
        

while True:
    currVal = math.floor(myPot.read_u16() / (2 ** 8))
    if (abs(currVal - prevVal) >= 4):
        # print the number with LED
        prevVal = currVal
        led0.value(0)
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        led6.value(0)
        led7.value(0)
        
        utime.sleep(0.0625)
        
        dec_to_bin(prevVal)
        
        led0.value(bin_digits[7])
        led1.value(bin_digits[6])
        led2.value(bin_digits[5])
        led3.value(bin_digits[4])
        led4.value(bin_digits[3])
        led5.value(bin_digits[2])
        led6.value(bin_digits[1])
        led7.value(bin_digits[0])
        
        utime.sleep(0.125)

