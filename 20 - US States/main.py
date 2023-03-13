import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

coordinate_data = pandas.read_csv("50_states.csv")
state_list = coordinate_data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state name:").title()

    if answer_state == "Exit":
        missing_states = []

        for state in state_list:
            if state not in guessed_state:
                missing_states.append(state)

        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")

        break

    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = coordinate_data[coordinate_data.state == answer_state]

        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

        guessed_state.append(answer_state)

screen.exitonclick()