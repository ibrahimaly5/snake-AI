from tkinter import *
import sys

root = Tk()

def key(event):
    print("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

def callback2():
	root.destroy()

frame = Frame(root, width=600, height=400)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)

quitButton = Button(root,command = callback2, text="Exit", background = "blue", highlightthickness=1)
quitButton.place(x=550, y=300)

frame.pack()

root.mainloop()


'''
class Game(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)


	frame = Frame(self, width=600, height=400)
	frame.bind("<Key>", key)
	frame.bind("<Button-1>", callback)

	quitButton = Button(self,command = callback2, text="Exit", background = "blue", highlightthickness=1)
	quitButton.place(x=550, y=300)

	frame.pack()

	self.mainloop()


def main():

    snake_game = Game()


if __name__ == '__main__':
    while True:
        main()
'''


