import turtle
from turtle import Turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create our dataframe from csv file
states_df = pd.read_csv("50_states.csv")
all_states = states_df.state.to_list()

# Make new turtle for drawing state names
state_turtle = Turtle()

correct_guesses = 0
correct_list = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_guesses}/50 Guess the state", prompt="What's another state's name?")

    # Convert the guess to title state (uppercase first letters)
    title_guess = answer_state.title()

    # Exit the game
    if title_guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_list:
                missing_states.append(state)
        print(missing_states)
        missing_csv = pd.DataFrame(missing_states).to_csv("missing_states.csv")
        break

    # Check to see if the guess is actually one of the 50 states
    if title_guess in set(states_df['state']) and title_guess not in correct_list:
        # Write correct guesses on the map
        x_coor = int(states_df[states_df["state"] == title_guess]["x"].iloc[0])
        y_coor = int(states_df[states_df["state"] == title_guess]["y"].iloc[0])
        print(x_coor)
        print(y_coor)
        state_turtle.penup()
        state_turtle.goto(x_coor,y_coor)
        state_turtle.write(title_guess)
        state_turtle.hideturtle()
        correct_guesses += 1
        correct_list.append(title_guess)
    else:
        print("Try again")

