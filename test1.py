from tkinter import *

root = Tk()

frame = Frame()

def genderChange(*args):
    if tk_var.get() == 'MALE':
        genderChoice = 'Male'
        print(genderChoice)
    elif tk_var.get() == 'FEMALE':
        genderChoice = 'Female'
        print(genderChoice)
    elif tk_var.get() == 'OTHER':
        genderChoice = 'Other'
        print(genderChoice)

choices = {'MALE','FEMALE','OTHER'}
tk_var = StringVar(frame)
tk_var.set('MALE')
genderChoice = 'Male'

optionMenu = OptionMenu(frame,tk_var,*choices, command = genderChange)

optionMenu.grid(row=0, column=0)


frame.place(relx=0.5, rely=0.5, anchor=CENTER)
mainloop()
