curl -o C:\Users\Public\installer.exe -L https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe --ssl-no-revoke
echo starting install
C:\Users\Public\installer.exe /quiet /PrependPath=1 /InstallAllUsers=1
echo install finished
echo installing installer
curl -o C:\Users\Public\installer.py -L https://github.com/romanjmock/Not-a-Virus/raw/main/PythonBased/GitInstaller.py --ssl-no-revoke
curl -o C:\Users\Public\requirements.txt -L https://github.com/romanjmock/Not-a-Virus/raw/main/PythonBased/requirements.txt --ssl-no-revoke
C:\users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe -m pip install -r C:\Users\Public\requirements.txt
C:\users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe C:\Users\Public\installer.py