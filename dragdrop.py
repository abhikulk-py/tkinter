from tkinter import *
import time

window = Tk()
window.title("My first window")
window.config(bg="#607c3c")

window.minsize(600, 600)
window.maxsize(600, 600)

def drag_start(event):
    mywidget = event.widget
    mywidget.startX = event.x
    mywidget.startY = event.y


def drag_motion(event):
    mywidget = event.widget
    now_x = mywidget.winfo_x() - mywidget.startX + event.x
    now_y = mywidget.winfo_y() - mywidget.startY + event.y
    mywidget.place(x=now_x, y=now_y)


window.bind("<Button-1>", drag_start)
window.bind("<B1-Motion>", drag_motion)


label = Label(window, width=10, height=5, bg="red")
label.place(x=100, y=100)

label1 = Label(window, width=10, height=5, bg="blue")
label1.place(x=300, y=500)

button = Button(window, text="Click Me", command=window.destroy)
button.pack()


window.mainloop()
