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

t1 = turtle.Turtle()
t1.shape('turtle')
t1.color('green')
t1.forward(100)
t1.speed(1)


t2 = turtle.Turtle()
t2.setposition(200,0)
t2.shape('turtle')
t2.color('blue')
t2.backward(500)
t2.speed(1)

if t2.position == t1.position :
    t1.backward(100)
    t2.forward(100)

screen = turtle.getscreen()
turtle.exitonclick()