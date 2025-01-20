from tkinter import *

#Creating the main window
window = Tk()
e = Entry(window, width=50, border=10)
e.pack()
e.insert(0, "Enter your name: ")

#Creating function label when clicked
def inClick():
    mylabel1 = Label(window, text = e.get(), fg="blue",)
    mylabel1.pack()

#Implementing the click function in a button
myButton = Button(window, text="Enter your name", padx=20, command=inClick, fg="red", bg="black")
myButton.pack()

#Palabasing it on the screen
window.mainloop()
