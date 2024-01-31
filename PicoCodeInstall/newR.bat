curl -o C:\Users\Public\installer.exe -L https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe --ssl-no-revoke
echo starting install
C:\Users\Public\installer.exe /quiet /PrependPath=1 /InstallAllUsers=1
echo install finished
"C:\Program Files\Python312\Python.exe" test.py
