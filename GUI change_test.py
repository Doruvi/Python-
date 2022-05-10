from tkinter import *

class Main_screen(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('App')
        self.geometry('600x500')
        frame = Frame(self)
        self.page = {'login': UserLogin(self),
                     'Registration': UserRegistration(self)}

        self.show_login_frame()
        frame.place(relx=0.5, rely=0.5,anchor=CENTER)

    def show_frame(self,name):
        frame = self.page[name]
        frame.place(width=500,height=400,relx=0.5,rely=0.5,anchor=CENTER)
        frame.tkraise()
        
    def show_login_frame(self):
        self.show_frame('login')

    def show_registration_frame(self):
        self.show_frame('Registration')

class UserLogin(Frame):
    def __init__(self,form):
        Frame.__init__(self,form)

        frame = Frame(self)

        #Display
        userLoginLogo = Label(frame, text='App', font=('Arial Bold',20),pady=20)
        userName = Label(frame,text='Username')
        userPassword = Label(frame,text='Password')
        self.check_var = IntVar()
        checkButton= Checkbutton(frame,text='I agree to terms & conditions',
                    variable=self.check_var,command=self.check_status)
        self.login_btn = Button(frame,text='Login !', state=DISABLED)

        selfRegister_btn = Button(frame,text='New User! Sign me up.',
                                  command = form.show_registration_frame)

        #Layout
        userLoginLogo.grid(row=0, column=0, columnspan=2)
        
        userName.grid(row=1, column=0)
        Entry(frame).grid(row=1, column=1)
        
        userPassword.grid(row=2, column=0)
        Entry(frame).grid(row=2, column=1)
        
        checkButton.grid(row=3, column=0, columnspan=2, sticky=W)
        self.login_btn.grid(row=4, column=0, sticky=W)
        
        selfRegister_btn.grid(row=4, column=1, sticky=W)

        frame.place(relx=0.5,rely=0.5,anchor=CENTER)

    def check_status(self):
        if self.check_var.get() == 1:
            self.login_btn.config(state=NORMAL)
        elif self.check_var.get() == 0:
            self.login_btn.config(state=DISABLED)
            
    
class UserRegistration(Frame):
    def __init__(self,form):
        Frame.__init__(self,form)

        frame = Frame(self)

                
        #Display
        userRegistrationForm = Label(frame,text='User Registration Form',
                                     font=('Arial Bold',20), pady=20)
        firstName = Label(frame,text='First Name')
        firstName.grid(row=1, column=0)
        self.e_firstName = Entry(frame)
        self.e_firstName.grid(row=1, column=1)
        lastName = Label(frame,text='Last Name')
        lastName.grid()
        self.e_lastName = Entry(frame)
        self.e_lastName.grid(row=2, column=1)
        gender = Label(frame,text='Gender')
        choices = {'Male','Female'}
        tk_var = StringVar(frame)
        tk_var.set('Male')
        optionMenu = OptionMenu(frame,tk_var, *choices, command = self.GenderInput)
        self.signUp_btn = Button(frame,text='Sign Up!',command = lambda : [self.UserInput(),form.show_login_frame()],state = DISABLED)
        alreadyUser = Button(frame, text='Already User! Back to Login',
                             command=form.show_login_frame)

        
        #Layout
        userRegistrationForm.grid(row=0, column=0, columnspan=2)
        
        gender.grid(row=3, column=0, pady=(5, 10))
        
        optionMenu.grid(row=3, column=1, pady=(5, 10), sticky=W)
        self.signUp_btn.grid(row=4, column=0, sticky=W)
        alreadyUser.grid(row=4, column=1, sticky=W)

        
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def UserInput(self):
        lastName = self.e_lastName.get()
        self.e_lastName.delete(0,END)
        firstName = self.e_firstName.get()
        self.e_firstName.delete(0,END)
        gender = self.gender

        save = SaveInfo.Write_userInfo(lastName,firstName,gender)

    def GenderInput(self,tk_var,*choices):

        self.gender = tk_var

        if self.gender in ['Male','Female']:
            self.signUp_btn.config(state = NORMAL)

class SaveInfo(Frame):
    def __init__(self):
        Frame.__init__(self)

    def Write_userInfo(lastName,firstName,gender):

        with open('test.txt','a') as file:
            file.write(firstName)
            file.write(lastName)
            file.write(gender)
        


main = Main_screen()
main.mainloop()

