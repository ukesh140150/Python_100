import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen=turtle.Screen()
image ="blank_states_img.gif"
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

answer_state=screen.textinput(title="Guess the State", prompt="What's another state's name?").title()


