C:
cd C:\Users\roman\AppData\Local\Programs\
:loop
echo checking file
if exist Python (goto run) else (goto loop)
:run
echo file exists
D:
python test.py