import os
from time import sleep
import random
import subprocess
import psutil

path = "C:/users/%USERNAME%/AppData/Local/Programs/Python/Python312/python.exe "

invade = path + 'C:/Users/Public/Kernal46/PythonBased/Invade.py'
print('invade is now', invade)
mouseThief = path + 'C:/Users/Public/Kernal46/PythonBased/MouseThief.py'
scopeIn = path + 'C:/Users/Public/Kernal46/PythonBased/ScopeIn.py'
print(invade)

CREATE_NO_WINDOW = 0x08000000
continueRunning = True
programs = psutil.process_iter()
runners = []
for p in programs:
    if p.name() == 'Runner.exe':
        print(p.name(), ', ', p.ppid(), ', ', os.getpid())
        runners.append(p)
print('count is', len(runners))
if (len(runners) > 2):
    continueRunning = False

sleep(1)
while continueRunning:
    count = sum(1 for proc in psutil.process_iter() if proc.name() == 'Runner.exe')
    print('count is currently', count)
    r = (int)(random.random() * 3)
    r = 0
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
    sleep(1)

print('done')