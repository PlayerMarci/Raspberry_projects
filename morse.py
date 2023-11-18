import machine
import utime

#Built on Raspberry PI pico WH
#So this code asks the user for a string, and in return you get the built-in led flashing in a morse code way.
#2023. nov. 18.

led_pin = machine.Pin("LED", machine.Pin.OUT)

#point '.' for short signal
#minus '-' for long signal
dictionary = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '.......'
}

while (True):

    print("Give me a string which morse code you want to see!")

    text = input().upper()


    for ch in text:
        val = dictionary[ch]
        for _ in val:
            if (_ == '.'):
                led_pin.on()
                utime.sleep(0.125)
                led_pin.off()
                print('.')
            else:
                led_pin.on()
                utime.sleep(0.5)
                led_pin.off()
                print('-')
            utime.sleep(1.0) #delay between each short and long sign
