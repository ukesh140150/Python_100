from turtle import Turtle , Screen
from snake import Snake
import time

screen = Screen()
#let these be constants to tweak the game easy ah 
starting_positions = [(0,0) , (-20,0) , (-40,0)]
move_distance = 20
segments = []



for posistion in starting_positions:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.goto(posistion)
    segments.append(segment)


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)
    def right(self):        
        self.segments[0].setheading(0)        



snake = Snake()


screen.listen()
screen.onkey(snake.move , "Up")
screen.onkey(snake.move , "Down")
screen.onkey(snake.move , "Left")
screen.onkey(snake.move , "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()