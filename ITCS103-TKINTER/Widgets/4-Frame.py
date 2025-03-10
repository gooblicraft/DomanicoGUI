from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Widget 4 - Frame")

frame1 = Frame(window)
frame1.pack()

label1 = Label(frame1, text="Hello World", justify=LEFT)
label1.pack()

window.mainloop()