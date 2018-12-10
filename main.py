from src.ai_game import ai_Game
from src.game import human_Game
import random
from tkinter import *
import sys

root = Tk()
root.title("python snake")
root.geometry("600x400")
root.configure(background="black")
root.resizable(width=False, height=False)

#exit the program
def callback1():
	root.destroy()
	sys.exit(-1)

#destroy the root, then call the new tkinter human game object
def callback2():
	root.destroy()
	game_class = human_Game()
	game_class.run_game()

#destroy the root, then call the new tkinter ai game object
def callback3():
	root.destroy()
	game_class = ai_Game()
	game_class.run_game()


def main():
	frame = Frame(root, width=600, height=400, bg = "black")
	#button for single player
	humanButton = Button(root,command = callback2, text="Single Player", background = "blue", highlightthickness=1)
	humanButton.place(x=300, y=150)
	#button for AI
	aiButton = Button(root,command = callback3, text="AI", background = "blue", highlightthickness=1)
	aiButton.place(x=300, y=200)
	#button for quitting
	quitButton = Button(root,command = callback1, text="Quit", background = "blue", highlightthickness=1)
	quitButton.place(x=300, y=250)

	frame.pack()
	root.mainloop()

if __name__ == '__main__':
    main()
