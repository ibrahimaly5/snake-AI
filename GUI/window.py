import tkinter
from time import sleep
import sys



class GameBoard(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)


        self.init_bkg()
        
        self.init_canvas()
        
        self.init_directions()

        self.init_food()
        

        self._canvas.pack()        


    def init_bkg(self):
        self.title("python snake")
        self.geometry("600x400")
        self.configure(background="black")
        self.resizable(width=False, height=False)

    def init_canvas(self):
        self._canvas = tkinter.Canvas(self, height= 600, width = 400, bg ="black", highlightthickness=0)

    def init_food(self):
        pass

    def init_directions(self):
        self.snake_dir = "up"
        self.snakeX = 0
        self.snakeY = 0
        self.bind("w",self.turn_up)
        self.bind("s",self.turn_down)
        self.bind("d",self.turn_right)  
        self.bind("a",self.turn_left)
        
    def turn_up(self,event):
        if (self.snake_dir=="left" or self.snake_dir=="right"):
            self.snake_dir = "up"
            self.snakeY += 1
        else: pass

    def turn_down(self,event):
        if (self.snake_dir=="left" or self.snake_dir=="right"):
            self.snake_dir = "down"
            self.snakeY -= 1
        else: pass

    def turn_right(self,event):
        if (self.snake_dir=="up" or self.snake_dir=="down"):
            self.snake_dir = "right"
            self.snakeX += 1
        else: pass
        
    def turn_left(self,event):
        if (self.snake_dir=="up" or self.snake_dir=="down"):
            self.snake_dir = "left"
            self.snakeX -= 1
        else: pass
        





    def run_board(self):
        self.mainloop()
        
