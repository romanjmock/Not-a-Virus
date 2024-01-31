import board
import digitalio
from time import sleep
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


keyboard = Keyboard(usb_hid.devices)
write = KeyboardLayoutUS(keyboard)

startTime = time.monotonic_ns()
currentTime = 0
print(startTime)

def writeMessage(message):
    for x in range (len(message)):
        current = message[x]
        keycodes = write.keycodes(current)
        for k in keycodes:
            keyboard.press(k)
        for k in keycodes:
            keyboard.release(k)

#sleep(3)

keyboard.press(Keycode.WINDOWS)
keyboard.press(Keycode.R)
keyboard.release(Keycode.WINDOWS)
keyboard.release(Keycode.R)

sleep(.3)

writeMessage('cmd')
sleep(.1)
keyboard.press(Keycode.ENTER)
keyboard.release(Keycode.ENTER)

sleep(1)

writeMessage('D:')
# sleep(.1)
# keyboard.press(Keycode.ENTER)
# keyboard.release(Keycode.ENTER)
# sleep(.1)
#writeMessage('python3 testFile.py')
writeMessage('r.bat')
sleep(.1)
keyboard.press(Keycode.ENTER)
keyboard.release(Keycode.ENTER)

sleep(.1)

writeMessage('exit')
sleep(.1)
keyboard.press(Keycode.ENTER)
keyboard.release(Keycode.ENTER)
# sleep(.5)
# 
# writeMessage('exit')
# keyboard.press(Keycode.ENTER)
# keyboard.release(Keycode.ENTER)
# 
# #cmdccmdcmdcmccmdcmc

# while currentTime < 5000:
#     #keyboard.press(Keycode.K)
#     #sleep(.15)
#     #keyboard.release(Keycode.K)
#     
#     currentTime = (time.monotonic_ns() - startTime) / 1000000.0
#     print(currentTime, startTime)
#     sleep(.1)

# while True:
#     Check if button is pressed and if it is, to press the Macros and toggle LED
#     if mute.value:  
#         print(" mute button Pressed")
#         keyboard.press(Keycode.F14)
#     time.sleep(0.1)
#