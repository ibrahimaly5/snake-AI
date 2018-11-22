import tkinter
import random
import sys



class GameBoard(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)

        self.food_exists = False
        self.snake_dir = "up"
        

        self.init_bkg()
        
        self.init_canvas()
        self._canvas.pack()        

        if not self.food_exists:
           self.generate_food()
           pass
        
        self.create_snake()

        self.init_directions()        


    def init_bkg(self):
        self.title("python snake")
        self.geometry("600x400")
        self.configure(background="black")
        self.resizable(width=False, height=False)


    def init_canvas(self):
        self._canvas = tkinter.Canvas(self, height= 400, width = 600, bg ="black", highlightthickness=0)


    def generate_food(self):
        self.food_x = 0
        self.food_y = 0
        while not (self.food_x % 25) and not(self.food_y % 25):
            self.food_x = round(600 * random.random())
            self.food_y = round(400 * random.random())

        '''
        while check_food_collision(self.food_x):
            self._canvas.food_x = 600 * random.random()

        while check_food_collision(self.food_y):
            self._canvas.food_y = 400 * random.random()
        '''
        self._canvas.create_rectangle(self.food_x, 
            self.food_y, (self.food_x+25), 
            (self.food_y+25), fill="light green")


        self.food_exists = True

        
    def init_directions(self):
        self.bind("w",self.turn_up)
        self.bind("s",self.turn_down)
        self.bind("d",self.turn_right)  
        self.bind("a",self.turn_left)
        self.bind("<Escape>", self.exit_game)
        
    def turn_up(self,event):
        if (self.snake_dir=="left" or self.snake_dir=="right"):
            self.snake_dir = "up"
            #self.snakeY += 1
            print("pressed", repr(event.char))

        else: pass

    def turn_down(self,event):
        if (self.snake_dir=="left" or self.snake_dir=="right"):
            self.snake_dir = "down"
            #self.snakeY -= 1
            print("pressed", repr(event.char))

        else: pass

    def turn_right(self,event):
        if (self.snake_dir=="up" or self.snake_dir=="down"):
            self.snake_dir = "right"
            #self.snakeX += 1
            print("pressed", repr(event.char))

        else: pass
        
    def turn_left(self,event):
        if (self.snake_dir=="up" or self.snake_dir=="down"):
            self.snake_dir = "left"
            #self.snakeX -= 1
            print("pressed", repr(event.char))

        else: pass
    
    def create_snake(self):

        self.headX = 0
        self.headY = 0

        self._canvas.create_rectangle(self.headX, 
            self.headY, (self.headX+25), 
            (self.headY+25), fill="green")

    def move_snake(self):
        pass
    def grow_snake(self):
        pass

    def exit_game(self,event):
        self.destroy()
        sys.exit()

    def run_game(self):
        self.mainloop()
        
