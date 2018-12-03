from src.window import GameBoard
import random
from time import sleep
from tkinter import *
import sys

root = Tk()

root.title("python snake")
root.geometry("600x400")
root.configure(background="black")
root.resizable(width=False, height=False)


def callback1():
	root.destroy()
	sys.exit(-1)

def callback2():
	root.destroy()
	game_class = GameBoard()

	game_class.run_game()

def callback3():	
	root.destroy()


def main():

	frame = Frame(root, width=600, height=400, bg = "black")
	
	humanButton = Button(root,command = callback2, text="Single Player", background = "blue", highlightthickness=1)
	humanButton.place(x=300, y=150)

	aiButton = Button(root,command = callback3, text="AI", background = "blue", highlightthickness=1)
	aiButton.place(x=300, y=200)

	quitButton = Button(root,command = callback1, text="Quit", background = "blue", highlightthickness=1)
	quitButton.place(x=300, y=250)

	frame.pack()

	root.mainloop()





if __name__ == '__main__':
    main()
