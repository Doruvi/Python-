from tkinter import *

root = Tk()
root.title('Log In')
root.geometry('400x300')

frame = Frame(root)

#Display
userName = Label(frame, text = 'UserName')
userName_entry = Entry(frame)

password = Label (frame, text = 'Password')
password_entry = Entry(frame)

CheckButton = Checkbutton(frame, text = 'I agree to the terms & conditions')
heading = Label(frame, text = "App", font = ('Arial Bold',16))


#layout

heading.grid(row=0,column=0,columnspan=2, pady=(0,20))

userName.grid(row=1,column=0,sticky = W)
userName_entry.grid(row=1,column=1)


password.grid(row=2,column=0,sticky = W)
password_entry.grid(row=2,column=1)

CheckButton.grid(row=3,column=0,columnspan=3,sticky = W)

frame.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()



