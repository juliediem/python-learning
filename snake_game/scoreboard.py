from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 270)
        self.score = 0
        self.scoreboard_text()

    def scoreboard_text(self):
        self.write(f"Scoreboard: {self.score}", False, align="center", font=("Courier", 16, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.scoreboard_text()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=("Courier", 16, 'normal'))
