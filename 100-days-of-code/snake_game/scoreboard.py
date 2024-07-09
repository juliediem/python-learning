from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 270)
        self.score = 0
        self.high_score = 0
        self.scoreboard_text()

    def scoreboard_text(self):
        self.clear()
        self.write(f"Scoreboard: {self.score} Highscore: {self.high_score}", False, align="center", font=("Courier", 16, 'normal'))

    def increase_score(self):
        self.score += 1
        self.scoreboard_text()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=("Courier", 16, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.scoreboard_text()
