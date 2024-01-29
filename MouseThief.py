import tkinter
from PIL import ImageTk, Image, ImageOps
import threading
from time import sleep
from pynput import mouse
import math

#sleep(5)

class MouseTheif:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.config(
            bg = '#000001'
        )
        self.caught = False
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        print(f'{self.width}, {self.height}')
        self.window.geometry((str)(self.width) + 'x' + (str)(self.height))
        #self.window.geometry((str)(width) + 'x' + (str)(height))
        self.window.geometry('+0+0')
        self.window.overrideredirect(True)
        self.window.wm_attributes('-transparentcolor', '#000001')
        self.window.wm_attributes('-topmost', True)

        self.canvas = tkinter.Canvas(
            self.window,
            width = self.width,
            height = self.height,
            highlightthickness = 0,
            bg = '#000001'
        )
        self.canvas.place(
            x = 0,
            y = 0
        )
        file = Image.open('mouse.png')
        x, y = file.size
        self.mL = ImageTk.PhotoImage(file)
        image = self.canvas.create_image(
            0,
            0,
            image = self.mL
        )
        print('image is', self.mL)
        print('image created')

        self.c = mouse.Controller()

        self.wX = 0
        self.wY = 0
        self.stealX = 0
        self.time = 0

        file = Image.open('Robber.png')
        file = file.resize((300, 300))
        self.file1 = ImageOps.mirror(ImageOps.flip(file))
        self.file = ImageOps.mirror(file)
        print('started')
    def start(self):
        self.render()
        self.window.mainloop()
    def render(self):
        self.canvas.delete(tkinter.ALL)
        x, y = self.c.position
        mI = self.canvas.create_image(self.width / 2, 85, image = self.mL)
        angle = math.atan2(y - self.wY - 150, x - self.wX - 150)
        hit = False
        if self.wX + 150 < x + 10 and self.wX + 150 > x - 10 and self.wY + 150 < y + 10 and self.wY + 150 > y - 10:
            hit = True
        else:
            #print(math.degrees(angle))
            self.wX += math.cos(angle) * 5
            self.wY += math.sin(angle) * 5
            self.wX = (int)(self.wX)
            self.wY = (int)(self.wY)
            print(f'{x}, {self.wX + 150}, {y}, {self.wY + 150}')
        #self.window.geometry('+' + (str)(self.wX) + '+' + (str)(self.wY))
        '''self.canvas.place(
            x = self.wX,
            y = self.wY
        )'''
        if math.degrees(angle) > -90 and math.degrees(angle) < 90:
            file = self.file.copy().rotate(math.degrees(-angle))
        else:
            file = self.file1.copy().rotate(math.degrees(-angle))
        img = ImageTk.PhotoImage(file)
        i = self.canvas.create_image(self.wX + 150, self.wY + 150, image = img)
        self.canvas.image = img
        if hit == False:
            self.window.after(10, self.render)
        elif hit == True:
            self.canvas.delete(tkinter.ALL)
            self.render1()
    def render1(self):
        self.caught = True
        self.c.position = (self.wX - self.stealX + 378 * (300 / 512), self.wY + 312 * (300 / 512))
        img = ImageTk.PhotoImage(self.file1.rotate(180))
        i = self.canvas.create_image(self.wX + 150 - self.stealX, self.wY + 150, image = img)
        self.canvas.image = img
        self.stealX += 1
        self.time += 1
        if self.wX - self.stealX + 300 >= 0:
            self.window.after(1, self.render1)
        else:
            print('finished')
            self.window.destroy()
    def getCtrl(self):
        return self.c

c = MouseTheif()
c.start()

print('done')