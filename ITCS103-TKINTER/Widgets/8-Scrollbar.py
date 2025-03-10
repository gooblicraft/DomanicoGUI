#Scrollbar
from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Widget 8 - Scrollbar")

#Scrollbar
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

#Dagdag sa listbox value
#Gagawa ng listbox itself
listbox1 = Listbox(window)
listbox1.insert(1,"Apple")
listbox1.insert(2,"Banana")
listbox1.insert(3,"Watermelon")
listbox1.insert(4,"Orange")
listbox1.configure(yscrollcommand=scrollbar.set)

for listbox in range(50):
    listbox1.insert(END,"Fruit" + str(listbox+1))
    
listbox1.pack(side=LEFT, fill=BOTH)
scrollbar.configure(command=listbox1.yview)

window.mainloop()