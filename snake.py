from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
# writing COORDINATES in snake form means it is a constant value
FORWARD_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):

        self.list = []
        self.turtle_()
        self.head = self.list[0]

    def turtle_(self):
        for position in COORDINATES:
            self.add_turtle(position)

    def add_turtle(self, position):
        tim = Turtle("square")
        tim.color("green")
        tim.penup()
        tim.goto(position)
        self.list.append(tim)

    def reset(self):
        for segments in self.list:
            segments.goto(1000, 1000)
        self.list.clear()
        self.turtle_()
        self.head = self.list[0]

    def extend(self):
        self.add_turtle(self.list[-1].position())

    def move(self):
        for num in range(len(self.list) - 1, 0, -1):
            new_x = self.list[num - 1].xcor()
            new_y = self.list[num - 1].ycor()
            self.list[num].goto(new_x, new_y)
        self.head.forward(FORWARD_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            pass

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            pass

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            pass

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            pass
