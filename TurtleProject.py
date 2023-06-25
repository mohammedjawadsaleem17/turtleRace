import turtle
from turtle import Turtle,Screen


screen = Screen()
screen.setup(width=500,height=400)

isRaceOn = False
userInput = screen.textinput(title="Make your guess",prompt="Which turtle will win the race? Enter a color: ")

#Chossing colors
colors = ["red","orange","yellow","green","blue","purple"]
allTurtle = []
import random

yPosition =  [-70,-40,-10,20,50,80]


#Turtle 1
for turtle_index in range(0,6):
    var = random.randint(0,125)
    newTurtle = Turtle(shape="turtle")
    newTurtle.penup()
    newTurtle.goto(-230, yPosition[turtle_index])
    newTurtle.color(colors[turtle_index])
    allTurtle.append(newTurtle)

print(allTurtle)

if userInput:
    isRaceOn=True

while isRaceOn:
    for turtle in allTurtle:
        if turtle.xcor()>230:
            isRaceOn=False
            winningColour = turtle.pencolor()
            if winningColour==userInput:
                print(f"You've Won! The {winningColour} turtle is the winner")
            else:
                print(f"You've lost! The {winningColour} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

# #Turtle 2
# tim2 = Turtle(shape="turtle")
# tim2.penup()
# tim2.goto(-230,-75)
# tim2.color(colors[1])
#
# #Turtle 3
# tim3 = Turtle(shape="turtle")
# tim3.penup()
# tim3.goto(-230,-50)
# tim3.color(colors[2])
#
# #Turtle 4
# tim4 = Turtle(shape="turtle")
# tim4.penup()
# tim4.goto(-230,-25)
# tim4.color(colors[3])
#
# #Turtle 5
# tim5 = Turtle(shape="turtle")
# tim5.penup()
# tim5.goto(-230,-0)
# tim5.color(colors[4])
#
# #Turtle 2
# tim6 = Turtle(shape="turtle")
# tim6.penup()
# tim6.goto(-230,-125)
# tim6.color(colors[5])





screen.exitonclick()
