import tkinter
import random
import sys

class ai_Game(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        #initialize class, starting direction and empty list to store snake coordinates
        self.snake_dir = "up"
        self.snake_parts = [None, None, None]
        self.snake_length = 3

        #initialize background and canvas
        self.init_bkg()

        self.init_canvas()

        #create snake and generate food
        self.create_snake()
        self.generate_food()

        self._canvas.pack()

        self.bind("<Escape>", self.exit_game)

        #start snake solver
        self.ai_snake()

    def init_bkg(self):
        self.title("python snake")
        self.geometry("600x400")
        self.configure(background="black")
        self.resizable(width=False, height=False)

    def init_canvas(self):
        self._canvas = tkinter.Canvas(self, height=400,width=600,bg="black",highlightthickness=0)

    #initialize starting snake points, creates snake by putting it on a grid of 24X13 (each block has a length of 25) 
    def create_snake(self):
        self.headX = 15 * 25
        self.headY = 8 * 25

        self.tempX = 15 * 25
        self.tempY = 8 * 25

        self.snake_coords = [(15 * 25, 9 * 25, 15 * 25 + 25, 9 * 25 + 25),
                             (15 * 25, 10 * 25, 15 * 25 + 25, 10 * 25 + 25),
                             (15 * 25, 11 * 25, 15 * 25 + 25, 11 * 25 + 25)]

        self.head = self._canvas.create_rectangle(self.headX, self.headY, 
            (self.headX + 25), (self.headY + 25), fill="green")

        for i in range(len(self.snake_coords)):
            self.snake_parts[i] = self._canvas.create_rectangle(
                self.snake_coords[i][0],
                self.snake_coords[i][1],
                self.snake_coords[i][2],
                self.snake_coords[i][3],
                fill="green")

    def generate_food(self):
        #x and y coordinates of food
        self.food_x = 25 * random.randint(0, 23)
        self.food_y = 25 * random.randint(0, 15)

        #check if food was generated on a snake part
        while self.check_food_collision():
            self.food_x = 25 * random.randint(0, 23)
            self.food_y = 25 * random.randint(0, 15)

        #create food
        self.food = self._canvas.create_rectangle(
            self.food_x,
            self.food_y,
            (self.food_x + 25),
            (self.food_y + 25),
            fill="light green")

        self.textbox = self._canvas.create_text(0,0,fill="white",font="Times 20 italic bold",
            anchor="nw",
            text="Score: {}".format(self.snake_length + 1))

    #check if food was generated on snake's body
    def check_food_collision(self):
        checking = False
        for coord in self.snake_coords:
            if (self.food_x == coord[0]) and (self.food_y == coord[1]):
                checking = True
        return checking

    #function to move the snake
    def move_snake(self):
        # to find coords of rectangles
        for i in range(len(self.snake_parts)):
            self.snake_coords[i] = self._canvas.coords(self.snake_parts[i])
        #move the snake's head to the temporary variable that stores its new coordinates
        self._canvas.move(self.head,
                          self.tempX - (self.headX),
                          self.tempY - (self.headY))

        #if the snake eats the foodm make it longer by appending to the snake body's list
        if (self.tempX == self.food_x) and (self.tempY == self.food_y):

            self.snake_coords.append(None)
            self.snake_parts.append(None)
            self.snake_coords[self.snake_length] = self.snake_coords[self.snake_length - 1]

        #move the rest of the body
        for i in range(self.snake_length):
            if i == 0:
                self._canvas.move(self.snake_parts[i],
                                  self.headX - (self.snake_coords[i][0]),
                                  self.headY - (self.snake_coords[i][1]))
            else:
                self._canvas.move(self.snake_parts[i],
                                  self.snake_coords[i - 1][0] - (self.snake_coords[i][0]),
                                  self.snake_coords[i - 1][1] - (self.snake_coords[i][1]))

        #give the head values the temporary values once the whole snake has been moved
        self.headX = self.tempX
        self.headY = self.tempY

        #once the snake moved, create a new block at the end of the snake
        if (self.tempX == self.food_x) and (self.tempY == self.food_y):
            self.snake_parts[self.snake_length] = self._canvas.create_rectangle(
                self.snake_coords[self.snake_length][0],
                self.snake_coords[self.snake_length][1],
                self.snake_coords[self.snake_length][0] + 25,
                self.snake_coords[self.snake_length][1] + 25,
                fill="green")

            #add 1 to the snake's length
            self.snake_length += 1

            #delete the food and the scoreboard, then re-generate them again using generate food
            self._canvas.delete(self.food)
            self._canvas.delete(self.textbox)

            self.generate_food()

        self._canvas.pack()

        #if the snake touches itself or a wall, exit the program
        if self.check_death(self.headX, self.headY):
            self.destroy()
            sys.exit(-1)

    #find the shortest path from the snake to the food (Using simple geometry)
    def shortest_path(self):
        self.x_move_req = (self.food_x - self.headX) / 25
        self.y_move_req = (self.food_y - self.headY) / 25

    #make the snake move vertically
    def move_vertically(self):

        if (self.y_move_req < 0):
            self.snake_dir = "up"
            if self.movey_counter < abs(self.y_move_req):
                self.tempY = self.tempY - 25
                if self.check_death(self.headX, self.tempY):
                    self.tempY += 25
                    self.tempX += 25
                    if self.x_move_req > 0:
                        self.x_move_req -= 1
                    else: self.x_move_req += 1
                    if self.check_death(self.tempX, self.headY):
                        self.tempX -= 50 
                        self.x_move_req -= 2 if self.x_move_req < 0 else + 2
                    self.move_snake()
                    self._canvas.pack()
                    self._canvas.after(100, self.move_vertically)
                else:
                    self.move_snake()
                    self._canvas.pack()
                    self.movey_counter += 1
                    self._canvas.after(100, self.move_vertically)

            elif self.movex_counter < abs(self.x_move_req):
                self.move_horizontally()
            else:
                self.ai_snake()

        elif (self.y_move_req > 0):
            self.snake_dir = "down"
            if self.movey_counter < self.y_move_req:
                self.tempY = self.tempY + 25
                if self.check_death(self.headX, self.tempY):
                    self.tempY -= 25
                    self.tempX += 25
                    if self.x_move_req > 0:
                        self.x_move_req -= 1
                    else: self.x_move_req += 1
                    if self.check_death(self.tempX, self.headY):
                        self.tempX -= 50
                        self.x_move_req -= 2 if self.x_move_req < 0 else + 2
                    self.move_snake()
                    self._canvas.pack()
                    self._canvas.after(100,self.move_vertically)
                else:
                    self.move_snake()
                    self._canvas.pack()
                    self.movey_counter += 1
                    self._canvas.after(100, self.move_vertically)
            elif self.movex_counter < abs(self.x_move_req):
                self.move_horizontally()
            else:
                self.ai_snake()
        else:
            if (self.snake_dir == "right") and (self.x_move_req < 0) or (self.snake_dir == "left") and (self.x_move_req > 0):
                self.tempY += 25
                if self.check_death(self.headX, self.tempY):
                    self.y_move_req = 1
                    self.tempY -= 50
                else:
                    self.y_move_req = -1      
                self.move_snake()
                self._canvas.pack()
                  
            self.move_horizontally()

    #make the snake move horizontally
    def move_horizontally(self):

        if (self.x_move_req < 0):
            self.snake_dir = "left"
            if self.movex_counter < abs(self.x_move_req):
                self.tempX -= 25
                if self.check_death(self.tempX, self.headY):
                    self.tempX += 25
                    self.tempY += 25
                    if self.y_move_req <0:
                        self.y_move_req += 1
                    else: self.y_move_req -= 1
                    if self.check_death(self.headX, self.tempY):
                        self.tempY -= 50
                        self.y_move_req -= 2 if self.y_move_req < 0 else +2
                    self.move_snake()
                    self._canvas.pack()
                    self._canvas.after(100,self.move_horizontally)
                else:
                    self.move_snake()
                    self._canvas.pack()
                    self.movex_counter += 1
                    self._canvas.after(100, self.move_horizontally)
            elif self.movey_counter < abs(self.y_move_req):
                self.move_vertically()
            else:
                self.ai_snake()

        elif (self.x_move_req > 0):
            self.snake_dir = "right"
            if self.movex_counter < self.x_move_req:
                self.tempX += 25
                if self.check_death(self.tempX, self.headY):
                    self.tempX -= 25
                    self.tempY += 25
                    self.y_move_req += 1
                    if self.check_death(self.headX, self.tempY):
                        self.tempY -= 50
                        self.y_move_req -= 2
                    self.move_snake()
                    self._canvas.pack()
                    self._canvas.after(100,self.move_horizontally)
                else:
                    self.move_snake()
                    self._canvas.pack()
                    self.movex_counter += 1
                    self._canvas.after(100, self.move_horizontally)
            elif self.movey_counter < abs(self.y_move_req):
                self.move_vertically()
            else:
                self.ai_snake()
        else:
            if ((self.snake_dir == "down") and (self.y_move_req < 0) ) or ((self.snake_dir == "up") and (self.y_move_req > 0)):
                self.tempX += 25
                if self.check_death(self.tempX, self.headY):
                    self.x_move_req = 1
                    self.tempX -= 50
                else:
                    self.x_move_req = -1      
                self.move_snake()
                self._canvas.pack()

            self.move_vertically()

    #function that initiaites the snake's movement and sets its path to the food
    #finds the shortest path, initiates counters for how many movements the snake has moved
    #then calls the snake's move commands (vertically and horizontally)
    def ai_snake(self):
        for i in range(len(self.snake_parts)):
            self.snake_coords[i] = self._canvas.coords(self.snake_parts[i])
        self.shortest_path()
        self.movex_counter = 0
        self.movey_counter = 0
        if (self.snake_dir == "up") or (self.snake_dir == "down"):
            # ai snake left/right first
            self.move_horizontally()

            # ai snake up/down second
        elif (self.snake_dir == "right") or (self.snake_dir == "left"):
            self.move_vertically()

    #checks if x and y are past the 4 walls of the canvas, or fell on a snake's body
    #if either one of these two conditions is true, return true
    def check_death(self,x,y):
        snake_death = False
        if (x < 0) or (x >= 600):
            snake_death = True
        elif (y < 0) or (y >= 400):
            snake_death = True
        else:
            pass

        for i in range(self.snake_length):
            if (x == self.snake_coords[i][0]) and (
                    y == self.snake_coords[i][1]):
                snake_death = True
                break
        return snake_death

    #exit the game
    def exit_game(self, event):
        self.destroy()
        sys.exit()

    #run the game
    def run_game(self):
        self.mainloop()
