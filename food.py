from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5) # it changes its size to half the orignal(20/20) to (10/10)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-270, 270))