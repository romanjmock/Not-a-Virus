## NOT A VIRUS
## Description
The following program does not replicate itself, and is therefore not a virus... technically... still wouldn't recommend installing it on a strangers computer, only a friend
## Deployment
using a Raspberyy pi Pico with CircuitPython installed, copy the PicoInstall files onto it, once you plug it into a computer, it will simulate keyboard strokes to install itself
## Removal
start by press Windows Key + R, and typing "shell:startup", then delete the file "runOnStart.bat".  Next go to C:/Users/Public, and delete Kernal46, Installer.py, Installer.exe, and requirements.txt.  It's not required to, however you may also uninstall python (which was installed during the deployment process) from your computer
