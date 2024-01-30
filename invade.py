import tkinter
import math
from pynput import mouse
from PIL import Image, ImageTk
from time import sleep
import random
import base64

window = tkinter.Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry((str)(width) + 'x' + (str)(height))
window.geometry('+0+0')
window.overrideredirect(True)
window.attributes('-topmost', True)
window.wm_attributes('-transparentcolor', '#000001')

c = tkinter.Canvas(
    window,
    width = width,
    height = height,
    highlightthickness = 0,
    bg = '#000001'
)
c.place(
    x = 0,
    y = 0
)
x = 0
y = 0

def onMove(x1, y1):
    global x, y
    x = x1
    y = y1
def onClick(x, y, key, click):
    #print(f'clicked at {x}, {y}, {key}, {click}')
    gWidth = 400
    gHeight = 400
    if click == True and time >= 300:
        angle1 = math.atan2((height - y) + gHeight, (x - width / 2) - gWidth)
        bullets.append(Bullet(width / 2, height - 100, angle1, 50))

    pass
m = mouse.Listener(on_move = onMove, on_click = onClick)
m.start()


g = Image.open('C:/Users/Public/Kernal46/Images/Turret.png')
g = g.resize((300, 450), False)
g = g.rotate(-90)

alienShip = Image.open('C:/Users/Public/Kernal46/Images/Ship.png')

class Explosion:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.age = 0
    def update(self):
        self.age += 1
    def getAge(self):
        return self.age
    def getX(self):
        return self.x
    def getY(self):
        return self.y

class Alien:
    def __init__(self, x1, y1, speed):
        self.x = x1
        self.y = y1
        self.speed = speed
        self.angle = 0
    def update(self):
        gHeight = 400
        gWidth = 400
        angle1 = math.atan2((height - self.y), -(self.x - width / 2))
        self.x += self.speed * math.cos(angle1)
        self.y += self.speed * math.sin(angle1)
        self.angle = angle1
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getAngle(self):
        return self.angle

class Bullet:
    def __init__(self, x1, y1, angle, speed):
        self.x = x1
        self.y = y1
        self.angle = angle
        self.speed = speed
    def update(self):
        self.x += self.speed * math.cos(-self.angle)
        self.y += self.speed * math.sin(-self.angle)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getAngle(self):
        return self.angle

aliens = []
bullets = []
explosions = []
images = []
#a1 = Alien(100, 100, 10)
#b1 = Bullet(500, 500, 45, 10)

g1 = None
time = 0
damage = 0
currentSpeed = 1
ship = Image.open('C:/Users/Public/Kernal46/Images/Ship.png')
ship = ship.resize((200, 100), False)
ship = ImageTk.PhotoImage(ship)

bullet = Image.open('C:/Users/Public/Kernal46/Images/Bullet.png')
bullet = bullet.resize((100, 100), False)

#label = tkinter.Label(image = ImageTk.PhotoImage(bullet))
#label.image = ImageTk.PhotoImage(bullet)

explosionImage = Image.open('C:/Users/Public/Kernal46/Images/Explosion.png')
explosionImage = explosionImage.resize((200, 200), False)
explosionImage = ImageTk.PhotoImage(explosionImage)

warning = Image.open('C:/Users/Public/Kernal46/Images/AlienWarning.png')
warning = warning.resize((200, 200), False)
warning = ImageTk.PhotoImage(warning)

bsod = Image.open('C:/Users/Public/Kernal46/Images/Bsod.jpg')
bsod = bsod.resize((width + 10, height + 10), False)
bsod = ImageTk.PhotoImage(bsod)

signTime = 0
bsodTime = 0

#draw sign
def run():
    global x, y, width, height, g, time, g1, aliens, damage, currentSpeed, ship, bullet, explosionImage, warning, bsodTime

    c.delete(tkinter.ALL)
    if (time < 300):
        sign = c.create_image(
            width / 2,
            height / 2,
            image = warning
        )
        l = tkinter.Label(image = warning)
        l.image = warning
    elif (damage < 100):
        #print(f'{x}, {y}')
        gWidth = 400
        gHeight = 400
        angle = math.atan2((height - y) + gHeight, (x - width / 2) - gWidth)
        #print(f'{height - y}, {x - width / 2}')
        g1 = g.copy().rotate(math.degrees(angle))
        #print(math.degrees(angle))
        g1 = ImageTk.PhotoImage(g1)
        #draw gun later
        #print(math.degrees(angle))
        #print(time)
        checkTime = (int)(30 / currentSpeed)
        if checkTime == 0:
            checkTime = 1
        if time % checkTime == 0:
            x1 = (int)(random.random() * width)
            aliens.append(Alien(x1, 0, 5 * currentSpeed))
        if (time % 500) == 0:
            currentSpeed += 1
            #print('currentSpeed is now', currentSpeed)
        # for x in range (10):
        #     print('initial x', x)
        #     image = c.create_image(
        #         x * 30,
        #         y,
        #         image = ship
        #     )
        #     c.update()
        #     sleep(.1)
        #sleep(1)
        for a in aliens:
            if a.getY() > height - 50:
                aliens.remove(a)
                #print('alien hit target')
                damage += 10
            a.update()
            # r = c.create_rectangle(
            #     a.getX(),
            #     a.getY(),
            #     a.getX() + 100,
            #     a.getY() + 100,
            #     fill = '#123456'
            # )
            image = c.create_image(
                a.getX(),
                a.getY(),
                image = ship
            )
            #c.update()
            for b in bullets:
                aX = a.getX()
                aY = a.getY()
                bX = b.getX()
                bY = b.getY()
                # x1 -= 50
                # y1 -= 50
                hitBox = 90
                if bX > aX - hitBox and bX < aX + hitBox and bY > aY - hitBox and bY < aY + hitBox:
                    try:
                        aliens.remove(a)
                        bullets.remove(b)
                        explosions.append(Explosion(aX, aY))
                    except ValueError:
                        pass
                        #print('error')
                    #print('shot')
        #draw bullets
        bulletsCount = 0
        for b in bullets:
            if b.getX() > width or b.getX() < 0 or b.getY() > height or b.getY() < 0:
                bullets.remove(b)
            #print(f'{b.getX()}, {b.getY()}')
            b.update()
            currentBullet = ImageTk.PhotoImage(bullet.copy().rotate(math.degrees(b.getAngle())))

            #save image object in label, otherwise it get's deleted
            label = tkinter.Label(image = currentBullet)
            label.image = currentBullet
            
            image = c.create_image(
                b.getX(),
                b.getY(),
                image = currentBullet
            )
            #c.image = currentBullet
            #images.append(image)
            #sleep(1)
            bulletsCount += 1
            #c.update()
            #sleep(.1)
        c.update()
        #sleep(1)
        #draw explosions
        for e in explosions:
            e.update()
            if (e.getAge() > 10):
                explosions.remove(e)
            else:
                c.create_image(
                    e.getX(),
                    e.getY(),
                    image = explosionImage
                )
        #drawing gun
        image = c.create_image(
            width / 2,
            height - 100,
            image = g1
        )
        #draw bar
        bar = c.create_rectangle(
            width / 2 - 300,
            10,
            width / 2 + 300,
            50,
            fill = '#FF0000'
        )
        barFill = c.create_rectangle(
            width / 2 - 300,
            10,
            width / 2 + 300 - 600 * (damage / 100),
            50,
            fill = '#00FF00'
        )
        #drawing glitches
        for i in range (damage * 3):
            xPos = (int)(random.random() * window.winfo_screenwidth())
            yPos = (int)(random.random() * window.winfo_screenheight())
            xLength = (int)(random.random() * 20)
            #yLength = (int)(random.random() * 20)
            yLength = 3
            colorR = (int)(random.random() * 3)
            red = '#FF0000'
            green = '#00FF00'
            blue = '#0000FF'
            color = ''
            if (colorR == 0):
                color = red
            if (colorR == 1):
                color = green
            if (colorR == 2):
                color = blue
            r = c.create_rectangle(
                xPos,
                yPos,
                xPos + xLength,
                yPos + yLength,
                fill = color,
                outline = color
            )
    elif damage <= 100:
        i = c.create_image(
            width / 2,
            height / 2,
            image = bsod
        )
        bsodTime += 1
    if (bsodTime > 1000):
        window.destroy()
    c.update()
    #sleep(.01)
    time += 1
    window.after(10, run)

run()
window.mainloop()
print('done')