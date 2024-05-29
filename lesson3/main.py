from tkinter import *


def move(event):
    x, y = event.x, event.y
    if y <= 25:
        canvas.coords(bird, x - 25, 0, x + 25, y + 25)
    elif y >= 600 - 25:
        canvas.coords(bird, x - 25, y - 25, x + 25, 600)
    elif x <= 25:
        canvas.coords(bird, 0, y - 25, x + 25, y + 25)
    elif x >= 800 - 25:
        canvas.coords(bird, x - 25, y - 25, 800, y + 25)
    else:
        canvas.coords(bird, x-25, y-25, x+25, y+25)


def key_move(event):
    if event.keycode == 65 or event.keycode == 37:  # A
        if canvas.coords(bird)[0] > 10:
            canvas.move(bird, -10, 0)
    elif event.keycode == 68 or event.keycode == 39:  # D
        if canvas.coords(bird)[0] + image.width() < 800-10:
            canvas.move(bird, 10, 0)
    elif event.keycode == 87 or event.keycode == 38:  # W
        if canvas.coords(bird)[1] > 10:
            canvas.move(bird, 0, -10)
    elif event.keycode == 83 or event.keycode == 40:  # S
        if canvas.coords(bird)[1] + image.height() < 600-10:
            canvas.move(bird, 0, 10)

    if 600 < canvas.coords(bird)[0] < 800 and 100 < canvas.coords(bird)[1] <200:
        canvas.itemconfig(text, text='Птичка на веточке')
    else:
        canvas.itemconfig(text, text='')


window = Tk()
window.geometry('800x600')


canvas = Canvas(window, width=800, height=600, background='lightblue')
canvas.pack()

image = PhotoImage(file='hummingbird.png')
bird = canvas.create_image(50, 450, image=image, anchor=NW)

text = canvas.create_text(20, 20, text='', anchor=NW)
image_branch = PhotoImage(file='branch.png')
branch = canvas.create_image(600, 200, image=image_branch, anchor=NW)

# canvas.bind('<Motion>', move)
window.bind('<KeyPress>', key_move)
window.mainloop()
