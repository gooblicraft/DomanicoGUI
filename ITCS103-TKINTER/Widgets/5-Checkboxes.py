#Checkboxes

from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Widget 5 - Checkboxes")

#Gawa ng variables for checkboxes (container)
variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()

#Gawa ng checkboxes
checkBox1 = Checkbutton(window, text="Ed", variable=variable1, justify=CENTER)
checkBox2 = Checkbutton(window, text="Jayvee", variable=variable2, justify=LEFT)
checkBox3 = Checkbutton(window, text="Liam", variable=variable3, justify=LEFT)
checkBox4 = Checkbutton(window, text="Janfyke", variable=variable4, justify=LEFT)

#Papack-U
checkBox1.grid(row=0, column=0)
checkBox2.grid(row=0, column=1)
checkBox3.grid(row=0, column=2)
checkBox4.grid(row=0, column=3)

window.mainloop()