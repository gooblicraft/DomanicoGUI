#Canvas
from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Widget 10 - Canvas")

#Canvas
canvas = Canvas(window, width=40, height=60)
canvas.pack()
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)
canvas.create_line(0, y, canvas_width, y)

window.mainloop()