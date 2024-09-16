import turtle
length = 200
turtle.left(90)
for i in range(6):
    length = length - 30
    for i in range(2):
        turtle.left(90)
        turtle.forward(length)
turtle.exitonclick()