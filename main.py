import turtle
from turtle import TurtleScreen
from random import seed, randint
print('Podaj mase pierwszej kulki od 1 do 5 kilogramów')
M1 = int(input())

print('Podaj mase drugiej kulki od 1 do 5 kilogramów')
M2 = int(input())
if M1 < 1:
    print('Podano za małą wartość')
elif M1 > 5:
    print('Podano za dużą wartość')
else:
    print('Podano masę pierwszej kulki:', M1)

if M2 < 1:
    print('Podano za małą wartość')
elif M2 > 5:
    print('Podano za dużą wartość')
else:
    print('Podano masę drugiej kulki:', M2)

print('Podaj szybkość początkową pierwszej kulki od 1 do 10 metrów na sekundę:')
V1 = int(input())
print('Podaj szybkość początkową drugiej kulki od 1 do 10 metrów na sekundę:')
V2 = int(input())
if V1 < 0:
    print('Podano za małą prędkość')
elif V1 > 10:
    print( 'Podano za dużą wartość')
else:
    print('Podano szybkości pierwszej kulki:', V1)

if V2 < 0:
    print('Podano za małą prędkość')
elif V2 > 10:
    print( 'Podano za dużą wartość')
else:
    print('Podano szybkości drugiej kulki:', V2)
V1k = V1*(M1-M2)/(M1+M2)+V2*(2*M2)/(M1+M2)
print('Wartość prędkości końcowej pierwszej kulki wynosi:', V1k)
V2k = V1*(2*M1)/(M1+M2)+V2*(M2-M1)/(M1+M2)
print('Wartość prędkości końcowej drugiej kulki wynosi:', V2k)
# prędkość V1k powinna być na "-" ponieważ porusza się po osi X w przeciwnym kierunku

turtle.title('Zderzenia centralna')

#ściany
sciana1 = turtle.Turtle()
sciana1.color('black')
sciana1.pensize(5)
sciana1.penup()
sciana1.goto(250,-100)
sciana1.pendown()
sciana1.goto(250,100)
sciana1.hideturtle()

sciana2 = turtle.Turtle()
sciana2.color('black')
sciana2.pensize(5)
sciana2.penup()
sciana2.goto(-250,100)
sciana2.pendown()
sciana2.goto(-250,-100)
sciana2.hideturtle()

sufit = turtle.Turtle()
sufit.color('black')
sufit.pensize(5)
sufit.penup()
sufit.goto(-250,100)
sufit.pendown()
sufit.goto(250,100)
sufit.hideturtle()

podloga = turtle.Turtle()
podloga.color('black')
podloga.pensize(5)
podloga.penup()
podloga.goto(-250,-100)
podloga.pendown()
podloga.goto(250,-100)
podloga.hideturtle()

DELAY = 100
t1 = turtle.Turtle()
t1.goto(-200,0)
t1.shape('turtle')
t1.color('green')
t2 = turtle.Turtle()
t2.goto(200,0)
t2.shape('turtle')
t2.color('blue')
#kombinowanie z tym by oba sie ruszyly w tym samym czasie. ogolnie nic nie działa i wyskakują bledy, ale sklejam rzeczy
#które wyszukałam i mogą mieć jakis sens

t1.speed(V1)
t2.speed(V2)
def movet1():
    t1.forward(t1.speed())
    turtle.ontimer(movet1, DELAY)
def movet2():
    if t1.position() != t2.position():
        t2.setheading(t2.towards(t1))
        t2.forward(t2.speed())
        turtle.ontimer(movet2, DELAY)

#zderzenie na podstawie gotowego programu co ci wysłałam
t1.speed(V1k)
t2.speed(V2k)
def is_collided_with(a,b):
    abs(a.xcor() - b.xcor()) < 40
def follow_runner():
    if is_collided_with(t1, t2):
        t1.setheading(0) and t2.setheading(200)
        t1.speed(V1k) and t2.speed(V2k)
movet1()
movet2()
#follow_runner()
is_collided_with(t1, t2)

if is_collided_with(t1, t2):
    t1.backward(100)
    t1.speed(V1k)
    t2.forward(100)
    t2.speed(V2k)

screen = turtle.getscreen()
turtle.exitonclick()