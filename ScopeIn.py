import tkinter
from PIL import Image, ImageTk
from pynput import mouse
import screeninfo

window = tkinter.Tk()
width = screeninfo.get_monitors()[0].width
height = screeninfo.get_monitors()[0].height
#width = window.winfo_screenwidth()
#height = window.winfo_screenheight()
window.geometry((str)(width) + 'x' + (str)(height))
window.geometry('+0+0')

window.overrideredirect(True)
window.wm_attributes('-transparentcolor', '#202020')
window.wm_attributes('-topmost', True)
window.config(
    bg = '#202020'
)

c = tkinter.Canvas(
    window,
    width = width,
    height = height,
    bg = '#202020',
    highlightthickness = 0
)
c.place(
    x = 0,
    y = 0
)
bulletDamage = Image.open('bulletDamage.png')
bulletDamage = bulletDamage.resize((200, 200), False)
bulletDamage = ImageTk.PhotoImage(bulletDamage)
bullets = []
bulletX = 0
bulletY = 0
shotTime = -10
def onClick(mx, my, key, click):
    global bulletDamage, shotTime, bulletX, bulletY
    print(mx, my, key, click, width, height)
    if ((str)(key) == "Button.left" or (str)(key) == "Button.right"):
        if (click == True):
            shotTime = time
            bulletX = mx
            bulletY = my
            pass

m = mouse.Controller()
m1 = mouse.Listener(on_click = onClick)
m1.start()

sniper = Image.open('Sniper.png')
sniper = sniper.resize((400, 400))
sniper = ImageTk.PhotoImage(sniper)

sign = Image.open('HuntingSeason.png')
sign = sign.crop((0, 70, 400, 330))
sign = sign.resize((500, 300))
sign = ImageTk.PhotoImage(sign)

time = 0
def printImage():
    global width, height, time
    x, y = m.position
    x += 5
    y += 5
    c.delete(tkinter.ALL)
    for j in range (len(bullets)):
        i = c.create_image(
            bullets[j][0],
            bullets[j][1],
            image = bulletDamage
        )
        label = tkinter.Label(image = bulletDamage)
        label.image = bulletDamage
    s = c.create_image(
        x + 3,
        y + 3,
        image = sniper
    )
    r = c.create_rectangle(0, 0, x + 3 - 200, height, fill = '#000000')
    r1 = c.create_rectangle(x + 3 + 200, 0, width, height, fill = '#000000')
    r2 = c.create_rectangle(x + 3 - 200, 0, x + 3 + 200, y + 3 - 200, fill = '#000000')
    r3 = c.create_rectangle(x + 3 - 200, y + 3 + 200, x + 3 + 200, height, fill = '#000000')

    s1 = c.create_image(
        width / 2,
        120,
        image = sign
    )
    time += 1
    if time == shotTime + 3:
        m.release(mouse.Button.left)
        m.move(0, -50)
        bullets.append((bulletX, bulletY))
    if time == 1000:
        exit(0)
    window.after(10, printImage)

printImage()
window.mainloop()