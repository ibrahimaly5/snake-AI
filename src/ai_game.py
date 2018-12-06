import tkinter
import random
import sys
from time import sleep


class ai_Game(tkinter.Tk):
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

        self.bind("<Escape>", self.exit_game)
        #self.bind("s", self.ai_snake)

        self.ai_snake()

    def init_bkg(self):
        self.title("python snake")
        self.geometry("600x400")
        self.configure(background="black")
        self.resizable(width=False, height=False)

    def init_canvas(self):
        self._canvas = tkinter.Canvas(
            self,
            height=400,
            width=600,
            bg="black",
            highlightthickness=0)

    def create_snake(self):

        self.headX = 15 * 25
        self.headY = 8 * 25

        self.tempX = 15 * 25
        self.tempY = 8 * 25

        self.snake_coords = [(15 * 25, 9 * 25, 15 * 25 + 25, 9 * 25 + 25),
                             (15 * 25, 10 * 25, 15 * 25 + 25, 10 * 25 + 25),
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

    def generate_food(self):

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

        self.textbox = self._canvas.create_text(
            0,
            0,
            fill="white",
            font="Times 20 italic bold",
            anchor="nw",
            text="Score: {}".format(
                self.snake_length +
                1))

    def check_food_collision(self):
        checking = False
        for coord in self.snake_coords:
            if (self.food_x == coord[0]) and (self.food_y == coord[1]):
                checking = True
        return checking

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

            self.snake_coords[self.snake_length] = self.snake_coords[self.snake_length - 1]

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
                self.snake_coords[self.snake_length][0] + 25,
                self.snake_coords[self.snake_length][1] + 25,
                fill="green")

            self.snake_length += 1

            self._canvas.delete(self.food)
            self._canvas.delete(self.textbox)

            self.generate_food()

            # self.ai_snake()

        # self.textbox = self._canvas.create_text(0,0,fill="white",font="Times 20 italic bold", anchor = "nw",
        #               text = "Score: {}".format(self.snake_length+1))

        self._canvas.pack()

    '''
    def constant_move(self):
        if (self.snake_dir == "up"):
            self.tempY = self.tempY - 25
            self.move_snake()

            if self.move_counter < self.y_move_req:
                self.move_counter += 1
                self._canvas.pack()
                self._canvas.after(250, self.constant_move)
            if self.check_death():
                self.destroy()
                return 0

        elif (self.snake_dir == "down"):
            self.tempY = self.tempY + 25
            self.move_snake()

            if self.move_counter < self.y_move_req:
                self.move_counter += 1
                self._canvas.pack()
                self._canvas.after(250, self.constant_move)

            if self.check_death():
                self.destroy()
                return 0

        elif (self.snake_dir == "right"):
            self.tempX = self.tempX + 25
            self.move_snake()

            if self.move_counter < self.x_move_req:
                self.move_counter += 1
                self._canvas.pack()
                self._canvas.after(250, self.constant_move)
            if self.check_death():
                self.destroy()
                return 0


        elif (self.snake_dir == "left"):
            self.tempX = self.tempX - 25
            self.move_snake()

            if self.move_counter < self.x_move_req:
                self.move_counter += 1
                self._canvas.pack()
                self._canvas.after(250, self.constant_move)

            if self.check_death():
                self.destroy()
                return 0

        self._canvas.after(250, self.constant_move)
        self._canvas.pack()
    '''

    def cross(self):
        if self.length_counter < 0:
            if abs(self.length_counter) <= self.snake_length:
                self.length_counter -= 1
                self.tempX += 25
                self.move_snake()
                self._canvas.pack()
                self._canvas.after(300, self.cross)
            else:
                self.ai_snake()
        elif self.length_counter > 0:
            if abs(self.length_counter) <= self.snake_length:
                self.length_counter += 1
                self.tempY -= 25
                self.move_snake()
                self._canvas.pack()
                self._canvas.after(300, self.cross)
            else:
                self.ai_snake()

    def shortest_path(self):
        self.x_move_req = (self.food_x - self.headX) / 25
        self.y_move_req = (self.food_y - self.headY) / 25
        print(self.food_y / 25)
        print(self.food_x / 25)
        print(self.headY / 25)
        print(self.headX / 25)
        print("")

    def move_vertically(self):

        if (self.y_move_req < 0):
            self.snake_dir = "up"
            # self.y_move_req *= -1

            if self.movey_counter < abs(self.y_move_req):
                self.tempY = self.tempY - 25
                self.move_snake()
                self._canvas.pack()
                self.movey_counter += 1
                self._canvas.after(300, self.move_vertically)
                # sleep(0.25)
            elif self.movex_counter < abs(self.x_move_req):
                self.move_horizontally()
            else:
                self.ai_snake()

        else:
            self.snake_dir = "down"
            if self.movey_counter < self.y_move_req:
                self.tempY = self.tempY + 25
                self.move_snake()
                self._canvas.pack()
                self.movey_counter += 1
                self._canvas.after(300, self.move_vertically)
                # sleep(0.25)
            elif self.movex_counter < abs(self.x_move_req):
                self.move_horizontally()
            else:
                self.ai_snake()

    def move_horizontally(self):

        if (self.x_move_req < 0):
            self.snake_dir = "left"
            # self.x_move_req *= -1
            if self.movex_counter < abs(self.x_move_req):
                self.tempX = self.tempX - 25
                self.move_snake()
                self._canvas.pack()
                self.movex_counter += 1
                self._canvas.after(300, self.move_horizontally)
                # sleep(0.25)
            elif self.movey_counter < abs(self.y_move_req):
                self.move_vertically()
            else:
                self.ai_snake()

        else:
            self.snake_dir = "right"
            if self.movex_counter < self.x_move_req:
                self.tempX = self.tempX + 25
                self.move_snake()
                self._canvas.pack()
                self.movex_counter += 1
                self._canvas.after(300, self.move_horizontally)
                # sleep(0.25)
            elif self.movey_counter < abs(self.y_move_req):
                self.move_vertically()
            else:
                self.ai_snake()

    def ai_snake(self):
        self.shortest_path()
        self.movex_counter = 0
        self.movey_counter = 0
        self.length_counter = 0
        if (self.snake_dir == "up") or (self.snake_dir == "down"):
            if self.x_move_req == 0:
                self.length_counter -= 1
                self.cross()
                return
            # ai snake left/right first

            self.move_horizontally()

            # ai snake up/down second

        elif (self.snake_dir == "right") or (self.snake_dir == "left"):
            # ai snake up/down first
            if self.y_move_req == 0:
                self.length_counter += 1
                self.cross()
                return

            self.move_vertically()
            # ai snake left/right second

        # self._canvas.after(250, self.ai_snake)

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
        self.destroy()
        sys.exit()

    def run_game(self):
        if self.check_death():
            self.destroy()

        self.mainloop()
