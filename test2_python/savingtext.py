from tkinter import *

root = Tk()
root.title('Test')
root.geometry('300x250')

frame = Frame(root)

def user_input():
    userInput = e_entry.get()
    e_entry.delete(0,END)

    #write into file
    with open('test.txt','a') as file:
        file.write(userInput)
        file.write('\n')


#Display
e_button = Button(frame,width = 5, height = 0, command = user_input)


#Layout
e_button.grid(row=1,column=0)

e_entry = Entry(frame)
e_entry.grid(row=0,column=0)


#loop and frame placement
frame.place(relx=0.5 ,rely=0.5 ,anchor=CENTER)
root.mainloop()
