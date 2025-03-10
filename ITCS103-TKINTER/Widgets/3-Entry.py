#Entry
from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Widget 3 - Entry")

#Creating Label for entry
label1 = Label(window, text="Enter Your Name")
label1.pack()

entry1 = Entry()
entry1.pack()

window.mainloop()