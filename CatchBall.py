from tkinter import *
import time
import random

canvas_width = 400
canvas_height = 500
speed_game = 3
start = [-speed_game, speed_game]
score = 0

class Ball:
	def __init__(self, cv, color):
		self.canvas = cv
		self.id = cv.create_oval(210, 110, 225, 125, fill=color)
		random.shuffle(start)
		self.x = start[0]
		self.y = -speed_game
		self.over = False
	def move(self, pos_bar):
		global score
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = speed_game
		if pos[3] >= canvas_height:
			self.over = True
		if pos[0] <= 0:
			self.x = speed_game
		if pos[2] >= canvas_width:
			self.x = -speed_game
		if pos[3] == pos_bar[1] and pos[2] >= pos_bar[0] and pos[2] <= pos_bar[2]:
			self.y = -speed_game
			score += 1

class Bar:
	def __init__(self, cv, color):
		self.canvas = cv
		self.id = cv.create_rectangle(100, canvas_height-15, 200, canvas_height, fill=color)
		self.x = 0
		self.y = 0
		self.canvas.bind_all('<KeyPress>', self.KeyPress)
	def move(self):
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x = speed_game
		if pos[2] >= canvas_width:
			self.x = -speed_game
	def KeyPress(self, event):
		if event.keysym == 'Left':
			self.x = -speed_game
		elif event.keysym == 'Right':
			self.x = speed_game

def makecenter(fm):
	fm.update_idletasks()
	width = fm.winfo_width()
	height = fm.winfo_height()
	x = (fm.winfo_screenwidth() // 2) - (width // 2)
	y = (fm.winfo_screenheight() // 2) - (height // 2)
	fm.geometry('{}x{}+{}+{}'.format(width, height, x, y))

tk = Tk()
tk.title('Catch ball')
tk.resizable(0, 0)

cv = Canvas(tk, width=canvas_width, height=canvas_height)
cv.pack()

ball = Ball(cv, 'red')
bar = Bar(cv, 'blue')

#makecenter(tk)
while 1:
	if ball.over == False:
		try:			
			ball.move(bar.canvas.coords(bar.id))
			bar.move()
			tk.update_idletasks()
			tk.update()
			time.sleep(0.01)
		except:
			break
	else:
		break

lblScore = Label(tk, text='Score: {}'.format(score), font=('consolas', 14, 'bold'))
lblScore.pack()

tk.mainloop()