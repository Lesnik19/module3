import random
from tkinter import *
from random import choice



class Ball:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = choice(colors)
        self.vx = 50
        self.vy = 50

        self.ball_id = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=self.color)
        self.move()

    def move(self):
        self.x1, self.y1, self.x2, self.y2 = canvas.coords(self.ball_id)
        if self.x1 <= 0 or self.x2 >= 600:
            self.vx = -self.vx
        if self.y1 <= 0 or self.y2 >= 500:
            self.vy = -self.vy
        canvas.move(self.ball_id, self.vx, self.vy)
        canvas.after(50, self.move)


colors = ['red', 'yellow', 'orange', 'blue', 'green', 'purple', 'white', 'black']

window = Tk()
window.geometry('600x500')

canvas = Canvas(window, width=600, height=500, background='lightblue')
canvas.pack()

ball1 = Ball(50, 50, 100, 100)
ball2 = Ball(400, 400, 425, 425)
ball3 = Ball(250, 250, 350, 350)
ball4 = Ball(450, 100, 500, 150)
ball5 = Ball(10, 300, 110, 400)
ball6 = Ball(250, 50, 350, 150)

window.mainloop()
