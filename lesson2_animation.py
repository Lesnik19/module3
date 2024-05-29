from tkinter import *

def move_ball():
    global speed
    canvas.move(rectangle, speed, 0)
    canvas.move(rectangle2, speed, 0)
    canvas.move(rectangle3, speed, 0)
    if canvas.coords(rectangle3)[2] >= 500 or canvas.coords(rectangle2)[0] <= 0:
        speed = -speed
    canvas.after(50, move_ball)


speed = 5

window = Tk()
window.geometry('500x500')

canvas = Canvas(window, width=500, height=500, background='lightblue')
canvas.pack()

rectangle = canvas.create_rectangle(75, 100, 175, 150)
rectangle2 = canvas.create_rectangle(25, 150, 225, 225)
rectangle3 = canvas.create_rectangle(150, 115, 250, 135)

move_ball()

window.mainloop()
