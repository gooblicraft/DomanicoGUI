#Menu
from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Widget 9 - Menu")

#Menu
menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="label", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

window.mainloop()