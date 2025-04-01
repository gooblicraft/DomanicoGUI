from tkinter import *

calculation = ""

def let_calculate(sign):
    global calculation
    calculation += str(sign)
    input_result.delete(1.0,'end')
    input_result.insert(1.0,calculation)

def let_eval_calculation():
    global calculation
    try:
        calculation_result = str(eval(calculation))
        input_result.delete(1.0, 'end')
        input_result.insert(1.0, calculation_result)
    except:
        input_result.delete(1.0, 'end')
        input_result.insert(1.0, "INVALID")

def let_del_calculation():
    global calculation
    calculation = ""
    calculation.delete(1.0, 'end')

mainWindow = Tk()
mainWindow.geometry('300x300')
mainWindow.title("Calculator")
mainWindow.resizable(FALSE, FALSE) #Fix window, cannot be resize

#Widgets Where the thing is clicked will be shown
input_result = Text(mainWindow, font=('Bold',20), height=2, width=20)
input_result.grid(columnspan=5)

#Wdigets where the buttons are
button1 = Button(mainWindow, text="1", command=lambda: let_calculate(1), width = 5, height=2)
button1.grid(row=1, column=0)
button2 = Button(mainWindow, text="2", command=lambda: let_calculate(2), width = 5, height=2)
button2.grid(row=1, column=1)
button3 = Button(mainWindow, text="3", command=lambda: let_calculate(3), width = 5, height=2)
button3.grid(row=1, column=2)

mainWindow.mainloop()