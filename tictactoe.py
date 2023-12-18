import random

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board_n : list[int] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lst = {}
pc_lst = []
c = 0

while c < 9:

	def list_update(board_n: list,lst: dict) -> list:
		for k,v in lst.items():
		    if k == 1:
		    	board_n[0][0] = v
		    if k == 2:
		    	board_n[0][1] = v
		    if k == 3:
		    	board_n[0][2] = v
		    if k == 4:
		    	board_n[1][0] = v
		    if k == 5:
		    	board_n[1][1] = v
		    if k == 6:
		    	board_n[1][2] = v
		    if k == 7:
		    	board_n[2][0] = v
		    if k == 8:
		    	board_n[2][1] = v
		    if k == 9:
		    	board_n[2][2] = v

	def winer(board_n: lst) -> bool:
		#VERTICAL WINNER (X)
		if board_n[0][0] == "X" and board_n[0][1] == "X" and board_n[0][2] == "X":
			print("THE WINNER IS X")
			return True
		elif board_n[1][0] == "X" and board_n[1][1] == "X" and board_n[1][2] == "X":
			print("THE WINNER IS X")
			return True
		elif board_n[2][0] == "X" and board_n[2][1] == "X" and board_n[2][2] == "X":
			print("THE WINNER IS X")
			return True
		#VERTICAL WINNER (O)
		elif board_n[0][0] == "O" and board_n[0][1] == "O" and board_n[0][2] == "O":
			print("THE WINNER IS O")
			return True
		elif board_n[1][0] == "O" and board_n[1][1] == "O" and board_n[1][2] == "O":
			print("THE WINNER IS O")
			return True
		elif board_n[2][0] == "O" and board_n[2][1] == "O" and board_n[2][2] == "O":
			print("THE WINNER IS O")
			return True
		#HORIZONTAL WINNER (X)
		elif board_n[0][0] == "X" and board_n[1][0] == "X" and board_n[2][0] == "X":
			print("THE WINNER IS X")
			return True
		elif board_n[0][1] == "X" and board_n[1][1] == "X" and board_n[2][1] == "X":
			print("THE WINNER IS X")
			return True
		elif board_n[0][2] == "X" and board_n[1][2] == "X" and board_n[2][2] == "X":
			print("THE WINNER IS X")
			return True
		#HORIZONTAL WINNER (O)
		elif board_n[0][0] == "O" and board_n[1][0] == "O" and board_n[2][0] == "O":
			print("THE WINNER IS O")
			return True
		elif board_n[0][1] == "O" and board_n[1][1] == "O" and board_n[2][1] == "O":
			print("THE WINNER IS O")
			return True
		elif board_n[0][2] == "O" and board_n[1][2] == "O" and board_n[2][2] == "O":
			print("THE WINNER IS O")
			return True
		#DIAGONAL WINER (X)
		elif board_n[0][2] == "X" and board_n[1][1] == "X" and board_n[2][0] == "X":
			print("THE WINNER IS X")
			return True
		elif board_n[2][2] == "X" and board_n[1][1] == "X" and board_n[0][0] == "X":
			print("THE WINNER IS X")
			return True
		#DIAGONAL WINNER (O)
		elif board_n[0][2] == "O" and board_n[1][1] == "O" and board_n[2][0] == "O":
			print("THE WINNER IS O")
			return True
		elif board_n[2][2] == "O" and board_n[1][1] == "O" and board_n[0][0] == "O":
			print("THE WINNER IS O")
			return True
		else:
			return False
	def board_frame(board_n : list[int]):
		for i in range(3):
			print('\n*---*---*---*')
			print("|",end="")
			for j in range(3):
				print("",board_n[i][j],end=" |")
		print('\n*---*---*---*')
	list_update(board_n,lst)
	board_frame(board_n)
	result = winer(board_n)
	if result == True:
		break
	else:
		if c % 2 == 0:
			player_1 = int(input("X: "))
			lst.update({player_1:"X"})
			pc_lst.append(player_1)
		else:
			player_2 = (random.choice([x for x in numbers if x not in pc_lst]))
			lst.update({player_2:"O"})
			pc_lst.append(player_2)
			print(f"O: {player_2}")
		c+=1
		continue
	
