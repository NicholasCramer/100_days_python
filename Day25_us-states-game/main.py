import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
congrats = "congrats.gif"
screen.addshape(image)
screen.addshape(congrats)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
ls_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Name a state").title()
    # check if answer_state is one of the states from the data file
    if answer_state == "Exit":
        states_to_learn = [state for state in ls_states if state not in guessed_states]
        # Generate a csv file on exit that contains states that were not guessed by the user
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv", header=False, index=False)
        break
    if answer_state in ls_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        if answer_state not in guessed_states:
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())
            guessed_states.append(answer_state)

if len(guessed_states) == 50:
    screen.clear()
    turtle.shape(congrats)
    screen.exitonclick()
