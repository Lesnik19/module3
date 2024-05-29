# анимация на Tkinter

from tkinter import *

def change_color(event):
    print(event.x, event.y)
    canvas.itemconfig('rect', fill='blue', outline='blue')
    canvas.update()
    canvas.after(500)
    canvas.itemconfig('rect', fill='red', outline='red')


# конструктор окна
window = Tk()
# размер окна
window.geometry('500x500')
# название окна
window.title('Анимация')

# создание холста
canvas = Canvas(window, width=500, height=500, background='green')

rect_id = canvas.create_rectangle(150, 150, 350, 350, fill='red', outline='red', tags=('rect'))
rect_id2 = canvas.create_rectangle(10, 10, 100, 100, fill='red', outline='red', tags=('rect', 'red'))
rect_id3 = canvas.create_rectangle(400, 400, 490, 490, fill='red', outline='red', tags=('rect', 'red'))

canvas.itemconfig('red', outline='yellow', width=3)

canvas.tag_bind('rect', '<Button-1>', change_color)

# размещение холста на окне
canvas.pack()

window.mainloop()
