from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 18, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 18, "normal"))

    def game_over(self):
        self.clear()
        self.write("GAME OVER", align="center", font=("Courier", 18, "normal"))


