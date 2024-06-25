import turtle
from turtle import Turtle
import pandas


class CheckAnswer(Turtle):
    def __init__(self):
        super().__init__()
        self.df = pandas.read_csv("50_states.csv")
        self.score = 0
        self.screen = turtle.Screen()
        self.penup()
        self.hideturtle()
        self.input_title = "Guess the Answer"
        self.game_in_progress = True
        self.guesses = []

    def user_answer(self):
        answer_state = self.screen.textinput(title=f"{self.input_title}", prompt="What's another state's name?")
        answer_state = answer_state.title()
        return answer_state

    def plot_coor(self, answer):
        # TODO Write correct guesses onto the map
        df_answer = self.df.loc[self.df['state'] == answer]
        x_cor = df_answer.x.iloc[0]
        y_cor = df_answer.y.iloc[0]
        print(x_cor)
        print(y_cor)
        self.goto(x_cor, y_cor)
        self.write(answer)

    def compare_answer(self, answer):
        # TODO check if the guess is among the 50 states
        if answer in self.df['state'].values:
            self.plot_coor(answer)
            self.update_score()
            self.guesses.append(answer)

    def update_score(self):
        self.score += 1
        self.input_title = f"{self.score}/50 Correct Guesses"

    def finish_game(self):
        if self.score == 50:
            print("hooray you beat the game")
