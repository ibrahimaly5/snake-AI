# snake-AI

I think this will hopefully be our 274 project. Currently working on creating the background, which is already done.

Will be done via tkinter mainly based on the repo below. I've tried to not copy anything, instead just using the ideas of how the game was created, etc. So far, I think the game mechanics could be fundamentally different based on the classes we will create.

https://github.com/chuyangliu/Snake


Will start by botch coding the initial positions of the snake and the "apple" right now, then try to create unit tests based on how much time I will have.

Depending on how quickly we'll finish creating the actual game mechanics, the project could pivot to a different kind of snake game. We could create a 2-player snake game, with the bigger snake eating the smaller snake.

One of the harder tasks will be getting the computer to control the snake (probably?)

The main focus will be to train the computer to play python using either a Greedy/Hamilton algorithm depending on the time we will put into it, once we get all the aforementioned steps done, we will write our own greedy algorithm for that.

Progress so far:
Created background, key bindings, and food

Goals by the end of the week (21 Nov 18):
Build snake and game physics around it. This will include how to actually design the snake, program snake collisions with food, walls, and itself. Program snake's movements per second, what happens when it turns right, left, etc. generating more food as it's being eaten and figure out what the most efficient way of generating a new position for the food is, and start the game.

#-In a list:
  -create snake
  -create snake collision physics
  -create snake movements

Goals for next week (30 Nov 18):
Create a button for either a human playing the game or AI playing the game, will create two separate classes for it. Start looking into the algorithms for the AI playing the game.
