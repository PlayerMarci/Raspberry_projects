import machine
import utime

led0 = machine.Pin(10, machine.Pin.OUT)
led1 = machine.Pin(11, machine.Pin.OUT)
led2 = machine.Pin(12, machine.Pin.OUT)
led3 = machine.Pin(13, machine.Pin.OUT)

bin_digits = []

def dec_to_bin(num):
     for i in range(4):
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
    for i in range(16):
        led0.value(0)
        led1.value(0)
        led2.value(0)
        led3.value(0)
        
        utime.sleep(1)
        
        dec_to_bin(i)
        
        led0.value(bin_digits[3])
        led1.value(bin_digits[2])
        led2.value(bin_digits[1])
        led3.value(bin_digits[0])
        
        utime.sleep(1)
