#coding=utf-8
import random

#生成一个4*4的矩阵
matix=[[0 for i in range(4)] for j in range(4) ]

#notzero函数的作用：游戏界面上非零的时候才显示，当0时，让其显示空
def notzero(s):
	return s if s!=0 else ''

def display():
	print("\r\
	|----|----|----|----|\n\
	|%4s|%4s|%4s|%4s|\n\
	|----|----|----|----|\n\
	|%4s|%4s|%4s|%4s|\n\
	|----|----|----|----|\n\
	|%4s|%4s|%4s|%4s|\n\
	|----|----|----|----|\n\
	|%4s|%4s|%4s|%4s|\n\
	|----|----|----|----|\n\
	"\
	%(notzero(matix[0][0]),notzero(matix[0][1]),notzero(matix[0][2]),notzero(matix[0][3]),\
	  notzero(matix[1][0]),notzero(matix[1][1]),notzero(matix[1][2]),notzero(matix[1][3]),\
	  notzero(matix[2][0]),notzero(matix[2][1]),notzero(matix[2][2]),notzero(matix[2][3]),\
	  notzero(matix[3][0]),notzero(matix[3][1]),notzero(matix[3][2]),notzero(matix[3][3])))


#初始化随机生成矩阵
def init():
	init_flag = 0
	while 1:
		k =  2 if random.randint(1,10) > 4 else 4
		s = divmod(random.randint(0,15) , 4) #不能到16 因为会出现4 下标为4就越界了
		if matix[s[0]][s[1]] == 0:
			matix[s[0]][s[1]] = k
			init_flag += 1 
			if init_flag == 2:
				break

#移动 每次移动之后在空白位置生成一个2或者4
def add_random_Number(): 
	init_flag = 0
	while 1:
		k = 2 if random.randint(1,10) > 4 else 4
		s = divmod(random.randint(0,15),4)
		if matix[s[0]][s[1]] == 0:
			matix[s[0]][s[1]] = k
			init_flag += 1
			if init_flag == 1:
				break
	display()


def move_Up():
	for i in range(4):
		for j in range(3):
			for k in range(j+1,4):
				if matix[k][i] > 0:
					if matix[k][i] ==matix[j][i]:
						matix[j][i] *= 2
						matix[k][i] = 0
					elif matix[j][i] == 0:
						matix[j][i] = matix[k][i]
						matix[k][i] = 0
					break
	add_random_Number()

def move_Down():
	for i in range(4): #处理列
		for j in range(3,0,-1): #3 2 1
			for k in range(j - 1,-1,-1): # 2 1 0  1 0 0
				if matix[k][i] > 0:
					if matix[k][i] == matix[j][i]:
						matix[k][i] = 0
						matix[j][i] *= 2
					elif matix[j][i] == 0:
						matix[j][i] = matix[k][i]
						matix[k][i] = 0
					break #这里的break只跳出一个循环
	add_random_Number()

def move_Left():
	for i in range(4):
		for j in range(3):
			for k in range(j+1,4):
				if matix[i][k] > 0:
					if matix[i][j] == 0:
						matix[i][j] = matix[i][k]
						matix[i][k] = 0
					elif matix[i][j] == matix[i][k]:
						matix[i][j] *= 2
						matix[i][k] = 0
					break
	add_random_Number()

def move_Right():
	for i in range(4):
		for j in range(3,0,-1):
			for k in range(j-1,-1,-1):
				if matix[i][k] > 0:
					if matix[i][j] == 0:
						matix[i][j] = matix[i][k]
						matix[i][k] = 0
					elif matix[i][j] == matix[i][k]:
						matix[i][j] *= 2
						matix[i][k] = 0
					break
	add_random_Number()

def check_win():
	win_flag = 0
	for i in matix:
		for j in i:
			if j >= 2048:
				win_flag = 1
	return win_flag

def check_lose():
	lose_flag = 1
	for i in matix:
		for j in i:
			if j == 0:
				lose_flag = 0
	return lose_flag

#入口函数
def main():
	global matix
	init()
	display()
	while 1:
		flag = raw_input("Please enter the character (UP:W)(DOWN:s)(LEFT:a)(RIGHT:d)(QUIT:q)(RESTART:r): \n")
		if flag == 'w':
			move_Up()
			if check_win():
				print('YOU WIN!!!')
				break
			elif check_lose():
				print('YOU LOSE,please try again \n')
				matix=[[0 for i in range(4)] for j in range(4) ]
				init()
				display()

		elif flag == 's':
			move_Down()
			if check_win():
				print('YOU WIN!!!')
				break
			elif check_lose():
				print('YOU LOSE,please try again \n')
				matix=[[0 for i in range(4)] for j in range(4) ]
				init()
				display()

		elif flag == 'a':
			move_Left()
			if check_win():
				print('YOU WIN!!!')
				break
			elif check_lose():
				print('YOU LOSE,please try again \n')
				matix=[[0 for i in range(4)] for j in range(4) ]
				init()
				display()

		elif flag == 'd':
			move_Right()
			if check_win():
				print('YOU WIN!!!')
				break
			elif check_lose():
				print('YOU LOSE,please try again \n')
				matix=[[0 for i in range(4)] for j in range(4) ]
				init()
				display()

		elif flag == 'r':
			matix = [[0 for i in range(4)] for j in range(4) ]
			init()
			display()
			print matix

		elif flag == 'q':
			break
		
		else:
			print("invailed enter,please try again")
main()