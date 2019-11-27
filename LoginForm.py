from tkinter import *
from tkinter import messagebox

def btn_Click():
	username = tbxUsername.get()
	password = tbxPassword.get()
	if(username == 'huu'):
		if(password == '123'):
			messagebox.showinfo('Notification', 'Login successful!')
		else:
			messagebox.showerror('Notification', 'Password wrong!')
	else:
		messagebox.showerror('Notification', 'Username wrong!')
		

fmLogin = Tk()
fmLogin.title('Login Form')

lbl1 = Label(fmLogin, text='Login form', font=('consolas', 18, 'bold'), fg='white', bg='red', justify=CENTER)
lbl1.grid(columnspan=2)

lblUsername = Label(fmLogin, text='Username:', font=('consolas', 14))
lblUsername.grid(row=1, column=0)

tbxUsername = Entry(fmLogin, width=30, font=('consolas', 14))
tbxUsername.grid(row=1, column=1)

lblPassword = Label(fmLogin, text='Password:', font=('consolas', 14))
lblPassword.grid(row=2, column=0)

tbxPassword = Entry(fmLogin, width=30, font=('consolas', 14), show='*')
tbxPassword.grid(row=2, column=1)

btnLogin = Button(fmLogin, text='Dang Nhap', font=('consolas', 14), fg='white', bg='blue', command = btn_Click)
btnLogin.grid(row=3, columnspan=2)

fmLogin.mainloop()