from src.window import GameBoard
import random
from time import sleep
from tkinter import *
import sys


def callback1(root):
	root.destroy()
	sys.exit(-1)

def callback2(root):
	root.destroy()
	game_class = GameBoard()

	game_class.run_game()

def callback3(root):	
	root.destroy()



def main():

	root = Tk()

	frame = Frame(root, width=600, height=400, bg = "black")
	
	humanButton = Button(root,command = callback2(root), text="Single Player", background = "blue", highlightthickness=1)
	humanButton.place(x=300, y=150)

	aiButton = Button(root,command = callback3(root), text="AI", background = "blue", highlightthickness=1)
	aiButton.place(x=300, y=200)

	quitButton = Button(root,command = callback1(root), text="Quit", background = "blue", highlightthickness=1)
	quitButton.place(x=300, y=250)

	frame.pack()

	root.mainloop()





if __name__ == '__main__':
	while True:
		main()
