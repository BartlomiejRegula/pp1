import turtle
t=turtle.Turtle()
turtle.bgcolor('black')
t.color('white')
t.speed(0)

def kwadrat(a,b,x,y):
    t.speed(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.color('magenta')
    t.begin_fill()
    for i in range(4):
        t.forward(a)
        t.right(b)
    t.end_fill()
    t.color('white')

def kwadraty():
    kwadrat(100,90,-900,-300)
    kwadrat(100,90,-750,-300)
    kwadrat(100,90,-600,-300)
    kwadrat(100,90,-450,-300)
    kwadrat(100,90,-300,-300)

def trojkat(x,y,head):
    t.speed(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(head)
    t.begin_fill()
    t.left(90)
    t.forward(300)
    t.right(135)
    t.forward(424)
    t.right(135)
    t.forward(300)
    t.end_fill()

def trojkaty():
    trojkat(600,-170,0)
    trojkat(580,-190,180)
    trojkat(580,-170,90)
    trojkat(600,-190,270)

def star(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.speed(0)
    t.color('yellow')
    t.begin_fill()
    t.setheading(0)
    for i in range(5):
            t.forward(50)
            t.right(144)
    t.end_fill()

def stars():
    star(-200,-200)
    star(-200,0)
    star(-300,-100)
    star(-100,-100)
    star(-200,-100)

def ring(x,y):
    t.pensize(9)
    t.speed(0)
    t.penup()
    t.goto(x,y)
    t.pendown()

    t.setheading(90)   
    t.circle(100)
    t.penup()
    t.left(90)
    t.forward(30)
    t.pendown()
    t.right(90)
    t.circle(70)
    t.pensize(1)

def rings():
    zmienna1=200
    for i in range(4):
        ring(zmienna1,290)
        zmienna1+=240

def arrow():
    t.speed(0)
    t.color('grey')
    t.begin_fill()
    t.setheading(0)
    t.forward(150)
    t.left(90)
    t.forward(40)
    t.right(120)
    t.forward(110)
    t.right(120)
    t.forward(110)
    t.right(120)
    t.forward(40)
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.color('white')

def arrows():
    zmienna1=-700
    zmienna2=0
    for i in range(5):
        arrow(zmienna1,zmienna2)
        zmienna2+=111

def name():
    t.penup()
    t.goto(370,450)
    t.pendown()
    t.write('Bartłomiej Reguła, ZZISS1-1113', font=('Arial',30))

arrow()

turtle.exitonclick()