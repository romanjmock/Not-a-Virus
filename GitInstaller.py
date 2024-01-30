import requests
import shutil

alienWarning = 'https://github.com/romanjmock/Not-a-Virus/blob/main/DistributePackage/AlienWarning.png?raw=true'
bsod = 'https://github.com/romanjmock/Not-a-Virus/blob/main/DistributePackage/Bsod.png?raw=true'
bullet = 'https://github.com/romanjmock/Not-a-Virus/blob/main/DistributePackage/Bullet.png?raw=true'
alienWarning = 'https://github.com/romanjmock/Not-a-Virus/blob/main/DistributePackage/AlienWarning.png?raw=true'
alienWarning = 'https://github.com/romanjmock/Not-a-Virus/blob/main/DistributePackage/AlienWarning.png?raw=true'
alienWarning = 'https://github.com/romanjmock/Not-a-Virus/blob/main/DistributePackage/AlienWarning.png?raw=true'
alienWarning = 'https://github.com/romanjmock/Not-a-Virus/blob/main/DistributePackage/AlienWarning.png?raw=true'
alienWarning = 'https://github.com/romanjmock/Not-a-Virus/blob/main/DistributePackage/AlienWarning.png?raw=true'
alienWarning = 'https://github.com/romanjmock/Not-a-Virus/blob/main/DistributePackage/AlienWarning.png?raw=true'
file = requests.get(url, stream = True)
print(file.text)
newFile = open('coolPicture.png', 'wb')
newFile.write(file.content)
