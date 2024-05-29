from tkinter import *
from random import choice

def change_color(event):
    for a in range(16):
        color = choice(colors)
        canvas.itemconfig('ball' + str(a), fill=color, outline=color)
        canvas.update()
        canvas.after(50)


# конструктор окна
window = Tk()
# размер окна
window.geometry('500x500')
# название окна
window.title('Гирлянда')

# создание холста
canvas = Canvas(window, width=500, height=500, background='lightblue')

canvas.create_line(0, 99, 500, 99)
colors = ['red', 'blue', 'green', 'yellow', 'purple']

for i in range(16):
    color = choice(colors)
    canvas.create_oval(20 + i * 30, 100, 40 + i * 30, 120, fill=color, outline=color, tags=('ball' + str(i)))

window.bind('<Button-1>', change_color)

# размещение холста на окне
canvas.pack()

window.mainloop()
