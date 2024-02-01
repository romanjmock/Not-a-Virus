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

# writeMessage('D:')
# sleep(.1)
# keyboard.press(Keycode.ENTER)
# keyboard.release(Keycode.ENTER)
# sleep(.1)
# #writeMessage('python3 testFile.py')
# #writeMessage('start /min r')
writeMessage('D:/s.lnk')
sleep(.1)
keyboard.press(Keycode.ENTER)
keyboard.release(Keycode.ENTER)

sleep(1.9)

keyboard.press(Keycode.TAB)
keyboard.release(Keycode.TAB)
keyboard.press(Keycode.TAB)
keyboard.release(Keycode.TAB)
keyboard.press(Keycode.ENTER)
keyboard.release(Keycode.ENTER)

writeMessage('exit')
sleep(.1)
keyboard.press(Keycode.ENTER)
keyboard.release(Keycode.ENTER)