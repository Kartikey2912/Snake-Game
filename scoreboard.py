from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.num = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.score()
    def score(self):
        self.clear()
        self.write(f"Score = {self.num} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.num > int(self.high_score):
            self.high_score = self.num
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.num = 0
        self.score()
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER !!", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.num += 1
        self.score()