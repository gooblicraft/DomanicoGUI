#Listbox
from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Widget 7 - Listbox")

#Gagawa ng listbox itself
listbox1 = Listbox(window)
listbox1.insert(1,"Apple")
listbox1.insert(2,"Banana")
listbox1.insert(3,"Watermelon")
listbox1.insert(4,"Orange")

listbox1.pack()

window.mainloop()