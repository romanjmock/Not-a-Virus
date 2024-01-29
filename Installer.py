import shutil
import os
import subprocess

path = "C:/Users/Public/Kernal46"
if (os.path.exists(path) == False):
    os.mkdir(path)
distributePath = os.path.join(path, 'DistributePackage')
if (os.path.exists(distributePath) == True):
    files = os.listdir(distributePath)
    for f in files:
        currentPath = os.path.join(distributePath, f)
        if (os.path.exists(currentPath)):
            os.remove(currentPath)
    os.rmdir(distributePath)

shutil.copytree('DistributePackage', distributePath)
runPath = os.path.join(distributePath, 'Runner.exe')
CREATE_NO_WINDOW = 0x08000000
subprocess.call(runPath, creationflags = CREATE_NO_WINDOW)