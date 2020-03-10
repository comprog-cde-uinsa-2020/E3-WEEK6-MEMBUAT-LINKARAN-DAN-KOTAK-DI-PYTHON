S=input("S= ")
S=int(S)


import turtle
t = turtle.Turtle()
t.color("white")
wn = turtle.Screen()
wn.bgcolor("blue")
t.begin_fill()
t.fillcolor("red")

for i in range(4):
    t.forward(S)
    t.right(90)

N=input("N= ")
N=int(N)

turtle.shape()
turtle.pencolor('red')
turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.goto(200,0)
turtle.circle(N)
turtle.down()

t.end_fill()
t.hideturtle()
