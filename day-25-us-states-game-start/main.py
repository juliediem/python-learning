import turtle
import pandas
from check_answer import CheckAnswer

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

check_answer = CheckAnswer()


# TODO convert the guess to Title Case
while check_answer.game_in_progress:
    answer_state = check_answer.user_answer()
    check_answer.compare_answer(answer_state)



# TODO Use a loop to allow a user to keep guessing
# TODO Record the correct guesses in a list
# TODO Keep track of the score in the input title bar





screen.exitonclick()