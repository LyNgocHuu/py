from tkinter import *
from tkinter import messagebox
import math

def SolveQE2():
	a = int(tbxA.get())
	b = int(tbxB.get())
	c = int(tbxC.get())
	if a == 0:
		if b == 0:
			if c == 0:
				messagebox.showinfo('Result', 'Phuong trinh vo so nghiem!')
			elif c != 0:
				messagebox.showinfo('Result', 'Phuong trinh vo nghiem!')
		elif b != 0:
			messagebox.showinfo('Result', 'Phuong trinh co nghiem {}'.format(-c/b))
	elif a != 0:
		delta = b**2-4*a*c
		if delta == 0:
			messagebox.showinfo('Result', 'Phuong trinh co nghiem kep {}'.format(-b/(2*a)))
		elif delta < 0:
			messagebox.showinfo('Result', 'Phuong trinh vo nghiem')
		elif delta > 0:
			messagebox.showinfo('Result', 'Phuong trinh co 2 nghiem x1={}, x2={}'.format((-b+math.sqrt(delta))/(2*a), (-b-math.sqrt(delta))/(2*a)))	

tk = Tk()
tk.title('Solve quadratic equation 2')

# Label
lblA = Label(tk, text='A:', font=('consolas', 14, 'bold'))
lblA.grid(row=0, column=0)

lblB = Label(tk, text='B:', font=('consolas', 14, 'bold'))
lblB.grid(row=1, column=0)

lblC = Label(tk, text='C:', font=('consolas', 14, 'bold'))
lblC.grid(row=2, column=0)

# Textbox
tbxA = Entry(tk)
tbxA.grid(row=0, column=1)

tbxB = Entry(tk)
tbxB.grid(row=1, column=1)

tbxC = Entry(tk)
tbxC.grid(row=2, column=1)

btn = Button(tk, text='Solve', font=('consolas', 14, 'bold'), command=SolveQE2)
btn.grid(columnspan=2)

tk.mainloop()