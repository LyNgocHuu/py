from random import randint

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def Print_Line(a, b, c):
	print('|', board[a], '|', board[b], '|', board[c], '|')
	print('-'*13)

def Show_Board():
	Print_Line(0, 1, 2)
	Print_Line(3, 4, 5)
	Print_Line(6, 7, 8)

def Check_Empty():
	for x in range(0, 9):
		if(board[x] != 'x' and board[x] != 'o'):
			return True

def Check_One(x, a, b, c):
	if (board[a] == x and board[b] == x and board[c] == x):
		return True
	return False

def Check_All(x):
	if (Check_One(x, 0, 1, 2)):
		return True
	if (Check_One(x, 3, 4, 5)):
		return True
	if (Check_One(x, 6, 7, 8)):
		return True
	if (Check_One(x, 0, 3, 6)):
		return True	
	if (Check_One(x, 1, 4, 7)):
		return True
	if (Check_One(x, 2, 5, 8)):
		return True
	if (Check_One(x, 0, 4, 8)):
		return True
	if (Check_One(x, 2, 4, 6)):
		return True

Show_Board()
winner = 0
while Check_Empty():	
	yCell = int(input('Please enter your cell (0 -> 8): '))
	if (board[yCell] == 'x' or board[yCell] == 'o'):
		print('Your cell already exist!')
	else:
		board[yCell] = 'x'
		while Check_Empty():
			cCell = randint(0, 8)
			if (board[cCell] == 'x' or board[cCell] == 'o'):
				pass
			else:
				board[cCell] = 'o'
				break
	Show_Board()
	if (Check_All('x')):
		winner = 'You'
		break
	if (Check_All('o')):
		winner = 'Computer'
		break

if (winner == 0):
	print('Hoa!')
else:
	print(winner + ' win!')

