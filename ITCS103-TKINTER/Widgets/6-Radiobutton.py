#Radiobutton
from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Widget 6 - RadioButton")

#Gawa ng variables for values ng radiobutton (container)
favouriteFood = IntVar()

#Gawa ng checkboxes
radioButton1 = Radiobutton(window, text="Apple", variable=favouriteFood, value="Apple")
radioButton2 = Radiobutton(window, text="Banana", variable=favouriteFood, value="Banana")
radioButton3 = Radiobutton(window, text="Watermelon", variable=favouriteFood, value="Watermelon")
radioButton4 = Radiobutton(window, text="Orange", variable=favouriteFood, value="Orange")

#Papack-U
radioButton1.grid(row=0, column=0)
radioButton2.grid(row=1, column=0)
radioButton3.grid(row=2, column=0)
radioButton4.grid(row=3, column=0)


window.mainloop()