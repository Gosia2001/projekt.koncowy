import turtle
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

t1 = turtle.Turtle()
t1.shape('turtle')
t1.color('green')
t1.forward(1000)
t1.speed(0)
t1.width(20)

if xt1.xcor() >= 250 or x <= -250:
    t1.left(180)



#t2 = turtle.Turtle()
#t2.setposition(200,0)
#t2.shape('turtle')
#t2.color('blue')
#t2.backward(200)
#t2.speed(V2)

#if t2.position == t1.position:
#    t1.backward(100)
 #   t1.speed(V1k)
  #  t2.forward(100)
   # t2.speed(V2k)

screen = turtle.getscreen()
turtle.exitonclick()