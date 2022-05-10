from tkinter import *
from equation import Calculate

root = Tk()
root.title("Simple calculator")

e = Entry(root, width = 40, borderwidth = 2)
e.grid(row = 0, column = 0, columnspan = 8, padx = 10, pady = 10)


def button_click(number):

    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+ str(number))
    

def button_clear():

    e.delete(0,END)

def button_add():

    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)
    
def button_subtract():

    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

    
def button_multiply():

    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_division():

    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    s_num = int(second_number)
    e.delete(0,END)
    calculate = Calculate(f_num, s_num) #hey this is a initiator 

    if math == "addition":
        e.insert(0, calculate.getAddition(f_num, s_num))
    elif math == "subtraction":
        e.insert(0, calculate.getSubtraction(f_num, s_num))
    elif math == "multiplication":
        e.insert(0, calculate.getMultiplication(f_num, s_num))
    elif math == "division":
        e.insert(0, calculate.getDivision(f_num, s_num))


    

button_1 = Button(root, text = "1",padx = 30, pady = 15,command = lambda: button_click(1))
button_2 = Button(root, text = "2",padx = 30, pady = 15,command = lambda: button_click(2))
button_3 = Button(root, text = "3",padx = 30, pady = 15,command = lambda: button_click(3))
button_x = Button(root, text = "X",padx = 29, pady = 15,command = button_multiply)

button_4 = Button(root, text = "4",padx = 30, pady = 15,command = lambda: button_click(4))
button_5 = Button(root, text = "5",padx = 30, pady = 15,command = lambda: button_click(5))
button_6 = Button(root, text = "6",padx = 30, pady = 15,command = lambda: button_click(6))
button_minus = Button(root, text = "-",padx = 30, pady = 15,command = button_subtract)

button_7 = Button(root, text = "7",padx = 30, pady = 15,command = lambda: button_click(7))
button_8 = Button(root, text = "8",padx = 30, pady = 15,command = lambda: button_click(8))
button_9 = Button(root, text = "9",padx = 30, pady = 15,command = lambda: button_click(9))
button_plus = Button(root, text = "+",padx = 29, pady = 15, command = button_add)

button_0 = Button(root, text = "0",padx = 30, pady = 15,command = lambda: button_click(0))
button_equal = Button(root, text = "=",padx = 30, pady = 15, command = button_equal)
button_division = Button(root, text = "/",padx = 30, pady = 15, command = button_division)
button_clear = Button(root, text = "C",padx = 30, pady = 15, command = button_clear)


button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_plus.grid(row = 3, column = 3)


button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_minus.grid(row = 2, column = 3)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_x.grid(row = 1, column = 3)

button_0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1)
button_equal.grid(row = 4, column = 2)
button_division.grid(row = 4, column = 3)