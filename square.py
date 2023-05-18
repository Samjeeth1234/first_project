import turtle
wn=turtle.Screen()
wn.bgcolor("black")
turtle.speed(0)
turtle.begin_fill()
turtle.fillcolor("blue")
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
    turtle.hideturtle()
turtle.end_fill()
