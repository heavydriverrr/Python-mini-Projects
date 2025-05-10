import turtle
import random
from turtle import Screen,Turtle


is_race = False
screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color: ")
color = ["purple","orange","yellow","brown","blue","red"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    tim = Turtle("turtle")
    tim.color(color[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(tim)

if user_bet:
    is_race = True

while is_race:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the Winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the Winner")
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)


screen.exitonclick()