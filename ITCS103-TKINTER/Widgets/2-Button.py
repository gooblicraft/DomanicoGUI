# Button
from tkinter import *

window = Tk()
window.title("Widget 2 - Button")
window.geometry("200x200")

# My Button, it close the window
button1 = Button(window, text="Click Me", width=10, command=window.destroy)
button1.pack()

# My button that changes the color when clicked
def changeButtonColor():
    button2.configure(bg="green", fg= "white", text="Already Changed the Color")
    
button2 = Button()
button2.configure(text = "Change Color", padx = 25,fg= "red", command = changeButtonColor)
button2.pack()

window.mainloop()