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
    input_result.delete(1.0, 'end')

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
button4 = Button(mainWindow, text="4", command=lambda: let_calculate(4), width = 5, height=2)
button4.grid(row=2, column=0)
button5 = Button(mainWindow, text="5", command=lambda: let_calculate(5), width = 5, height=2)
button5.grid(row=2, column=1)
button6 = Button(mainWindow, text="6", command=lambda: let_calculate(6), width = 5, height=2)
button6.grid(row=2, column=2)
button7 = Button(mainWindow, text="7", command=lambda: let_calculate(7), width = 5, height=2)
button7.grid(row=3, column=0)
button8 = Button(mainWindow, text="8", command=lambda: let_calculate(8), width = 5, height=2)
button8.grid(row=3, column=1)
button9 = Button(mainWindow, text="9", command=lambda: let_calculate(9), width = 5, height=2)
button9.grid(row=3, column=2)
button0 = Button(mainWindow, text="0", command=lambda: let_calculate(0), width = 5, height=2)
button0.grid(row=4, column=1)
buttonDel = Button(mainWindow, text="Del", command=let_del_calculation, width = 5, height=2)
buttonDel.grid(row=4, column=0)

mainWindow.mainloop()