import tkinter
from time import sleep
import sys



class GameBoard(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)

        self.init_bkg()
        self.init_canvas()
        self.init_objects()
        


    def init_objects(self):
        self._ingame = True
        self.snake_init_x = 400
        self.snake_init_y = 200


    def init_bkg(self):
        self.title("python snake")
        self.geometry("600x400")
        self.configure(background="black")
        self.resizable(width=False, height=False)

    def init_canvas(self):
        self._canvas = tkinter.Canvas(self, height= 600, width = 400, bg ="black", highlightthickness=0)
        self._canvas.pack()


def main():
    plot_game = True

    game_class = GameBoard()
    if plot_game:
        game_class.mainloop()
if __name__ == '__main__':
    main()