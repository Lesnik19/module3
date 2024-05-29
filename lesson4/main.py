from tkinter import *
from random import randint


def spawn_star():
    y = 0
    x = randint(10, 750)
    star = canvas.create_image(x, y, image=star_image, anchor=NW)
    stars.append(star)
    move_star(star)
    window.after(500, spawn_star)


def move_star(star):
    global score
    x, y = canvas.coords(star)
    if y + star_image.height() < 600:
        canvas.move(star, 0, 5)
        x, y = canvas.coords(star)
        if canvas.coords(cloud)[1] < y + star_image.height() < canvas.coords(cloud)[1] + cloud_image.height() \
                and canvas.coords(cloud)[0] - star_image.width() < x < canvas.coords(cloud)[0] + cloud_image.width():
            score += 1
            update_score()
            canvas.delete(star)
            stars.remove(star)
            return
        window.after(20, move_star, star)
    else:
        canvas.delete(star)
        stars.remove(star)



def move_cloud(event):
    if event.keycode == 37:  # стрелка влево
        canvas.move(cloud, -10, 0)
    if event.keycode == 39:  # стрелка вправо
        canvas.move(cloud, 10, 0)


def update_score():
    canvas.itemconfig(text, text=f'Счет: {score}')


stars = []
score = 0
window = Tk()

window.title('Звездопад')
window.geometry('800x600')
window.resizable(height=False, width=False)

star_image = PhotoImage(file='star.png')
cloud_image = PhotoImage(file='cloud.png')
night_image = PhotoImage(file='night.png')

canvas = Canvas(window, width=800, height=600, background='blue')

canvas.create_image(0, 0, image=night_image, anchor=NW)
cloud = canvas.create_image(300, 500, image=cloud_image, anchor=NW)
spawn_star()
text = canvas.create_text(10, 10, text=f'Счет: {score}', font='Arial 16', fill='white', anchor=NW)

window.bind('<KeyPress>', move_cloud)

canvas.pack()
window.mainloop()