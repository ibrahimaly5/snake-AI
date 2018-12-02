import tkinter
import random
import sys
import time


class GameBoard(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)

        self.snake_dir = "up"
        self.snake_parts = [None, None, None]
        self.snake_length = 3


        self.init_bkg()

        self.init_canvas()


        self.create_snake()
        self.generate_food()

        self._canvas.pack()

        self.init_directions()

    def init_bkg(self):
        self.title("python snake")
        self.geometry("600x400")
        self.configure(background="black")
        self.resizable(width=False, height=False)


    def init_canvas(self):
        self._canvas = tkinter.Canvas(self, height=400, width=600, bg="black", highlightthickness=0)

       
    def generate_food(self):
        '''
        if (self.food_x == self.headX) and (self.food_y == self.headY):
            pass
        else:
            for i in range()
        '''

        self.food_x = 25 * random.randint(0, 23)
        self.food_y = 25 * random.randint(0, 15)

        
        while self.check_food_collision():
            self.food_x = 25 * random.randint(0, 23)
            self.food_y = 25 * random.randint(0, 15)


        self.food = self._canvas.create_rectangle(
            self.food_x,
            self.food_y,
            (self.food_x + 25),
            (self.food_y + 25),
            fill="light green")
        
        self.textbox = self._canvas.create_text(0,0,fill="white",font="Times 20 italic bold", anchor = "nw",
                        text = "Score: {}".format(self.snake_length+1))
        

    def check_food_collision(self):
        checking = False
        for coord in self.snake_coords:
            if (self.food_x == coord[0]) and (self.food_y == coord[1]):
                checking = True
        return checking

    def init_directions(self):
        self.bind("w", self.turn_up)
        self.bind("s", self.turn_down)
        self.bind("d", self.turn_right)
        self.bind("a", self.turn_left)
        self.bind("<Escape>", self.exit_game)

    def turn_up(self, event):
        if (self.snake_dir == "left" or self.snake_dir == "right"):
            self.snake_dir = "up"

        else:
            pass

    def turn_down(self, event):
        if (self.snake_dir == "left" or self.snake_dir == "right"):
            self.snake_dir = "down"

        else:
            pass

    def turn_right(self, event):
        if (self.snake_dir == "up" or self.snake_dir == "down"):
            self.snake_dir = "right"
            
        else:
            pass

    def turn_left(self, event):
        if (self.snake_dir == "up" or self.snake_dir == "down"):
            self.snake_dir = "left"
            
        else:
            pass

    def create_snake(self):

        self.headX = 15 * 25
        self.headY = 8 * 25

        self.tempX = 15 * 25
        self.tempY = 8 * 25

        self.snake_coords = [(15 *25, 9 *25, 15 * 25 +25, 9 *25 +25),
                             (15 *25, 10 * 25, 15 * 25 + 25, 10 * 25 + 25), 
                             (15 * 25, 11 * 25, 15 * 25 + 25, 11 * 25 + 25)]


        self.head = self._canvas.create_rectangle(
            self.headX,
            self.headY,
            (self.headX + 25),
            (self.headY + 25),
            fill="green")

        for i in range(len(self.snake_coords)):
            self.snake_parts[i] = self._canvas.create_rectangle(
                self.snake_coords[i][0],
                self.snake_coords[i][1],
                self.snake_coords[i][2],
                self.snake_coords[i][3],
                fill="green")

    def move_snake(self):
        # to find coords of rectangles
        for i in range(len(self.snake_parts)):
            self.snake_coords[i] = self._canvas.coords(self.snake_parts[i])

        self._canvas.move(self.head,
                          self.tempX - (self.headX), 
                          self.tempY - (self.headY))


        if (self.tempX == self.food_x) and (self.tempY == self.food_y):
            
            self.snake_coords.append(None)
            self.snake_parts.append(None)

            self.snake_coords[self.snake_length] = self.snake_coords[self.snake_length-1]   


        for i in range(self.snake_length):
            if i == 0:
                self._canvas.move(self.snake_parts[i],
                                  self.headX - (self.snake_coords[i][0]),
                                  self.headY - (self.snake_coords[i][1]))
            else:
                self._canvas.move(self.snake_parts[i],
                                  self.snake_coords[i - 1][0] - (self.snake_coords[i][0]),
                                  self.snake_coords[i - 1][1] - (self.snake_coords[i][1]))

        self.headX = self.tempX
        self.headY = self.tempY

        if (self.tempX == self.food_x) and (self.tempY == self.food_y):
            self.snake_parts[self.snake_length] = self._canvas.create_rectangle(
                self.snake_coords[self.snake_length][0],
                self.snake_coords[self.snake_length][1],
                self.snake_coords[self.snake_length][0]+25,
                self.snake_coords[self.snake_length][1]+25,
                fill= "green")

            self.snake_length += 1

            self._canvas.delete(self.food)
            self._canvas.delete(self.textbox)

            self.generate_food()
        
        #self.textbox = self._canvas.create_text(0,0,fill="white",font="Times 20 italic bold", anchor = "nw",
                        #text = "Score: {}".format(self.snake_length+1))
        self._canvas.pack()

    def constant_move(self):
        if (self.snake_dir == "up"):
            self.tempY = self.tempY - 25
            self.move_snake()

            if self.check_death():
                self.destroy()
                return 0

        elif (self.snake_dir == "down"):
            self.tempY = self.tempY + 25
            self.move_snake()

            if self.check_death():
                self.destroy()
                return 0

        elif (self.snake_dir == "right"):
            self.tempX = self.tempX + 25
            self.move_snake()
            
            if self.check_death():
                self.destroy()
                return 0

        elif (self.snake_dir == "left"):
            self.tempX = self.tempX - 25
            self.move_snake()

            if self.check_death():
                self.destroy()
                return 0

        self._canvas.after(250, self.constant_move)
        self._canvas.pack()

    def check_death(self):
        snake_death = False

        if (self.headX < 0) or (self.headX >= 600):
            snake_death = True
        elif (self.headY < 0) or (self.headY >= 400):
            snake_death = True
        else:
            pass

        for i in range(len(self.snake_coords)):
            if (self.headX == self.snake_coords[i][0]) and (
                    self.headY == self.snake_coords[i][1]):
                snake_death = True
            else:
                pass

        return snake_death

    def exit_game(self, event):
        sys.exit()
        self.destroy()

    def run_game(self):

        # self.check_death():
        self.constant_move()
        self.mainloop()
