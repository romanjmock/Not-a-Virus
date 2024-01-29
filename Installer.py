import shutil
import os

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
os.system('distributePath/runner.exe')