import turtle
import random
t = turtle.Turtle()
turtle.bgcolor('white')
t.color('white')
t.speed(0)
# t.forward(200)
# t.right(90)
# t.forward(200)
# t.right(90)
# t.forward(200)
# t.right(90)
# t.forward(200)
for i in range(200):
    t.color(random.choice(['red','green','blue','purple']))
    t.forward(i)
    t.right(91)



turtle.exitonclick()