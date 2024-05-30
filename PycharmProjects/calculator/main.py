# from kivy.core.window import Window
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

window = Tk()
window.title("Sich.Calculator")
window.config(padx=50, pady=50, bg=GREEN)

int_1 = float
int_2 = float
result = float
# TO DO 1 functions +, -, *, / ___________________________________________________________________

def plus():
    result = int_1 + int_2
    return result

def minus():
    result = int_1 - int_2
    return result

def division():
    result = int_1 / int_2
    return result

def multiplication():
    result = int_1 * int_2
    return result

#TO DO Inputs and main function.....  ___________________________________________________________________

def calculation():
    inp_1 = input()
    inp_2 = input()
    func = input()
    if func == "+":
        plus()
    elif func == "-":
        minus()
    elif func == "/":
        division()
    elif func == "*":
        multiplication()
    print(result)

calculation()

# TO DO 2 "buttons" ___________________________________________________________________
#Display
password_entry = Entry(text=" ", width=21)
password_entry.grid(column=1, row=1, columnspan=4)

#Digits_Buttons
button1 = Button(text="1")
button1.grid(column=0, row=5)

button2 = Button(text="2")
button2.grid(column=1, row=5)

button3 = Button(text="3")
button3.grid(column=2, row=5)

button4 = Button(text="4")
button4.grid(column=0, row=4)

button5 = Button(text="5")
button5.grid(column=1, row=4)

button6 = Button(text="6")
button6.grid(column=2, row=4)

button7 = Button(text="7")
button7.grid(column=0, row=3)

button8 = Button(text="8")
button8.grid(column=1, row=3)

button9 = Button(text="9")
button9.grid(column=2, row=3)

button0 = Button(text="0")
button0.grid(column=1, row=6)

# button1 = Button(text="1")
# button1.grid(column=1, row=1)
#
# button1 = Button(text="1")
# button1.grid(column=1, row=1)

# TO DO 3 Interface ___________________________________________________________________

window.mainloop()