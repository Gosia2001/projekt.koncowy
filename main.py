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

M3 = int(input())
wn = turtle.Screen()
wn.bgcolor("lightblue")

#ściany
mypen = turtle.Turtle()
mypen.penup()
mypen.pencolor('black')
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range (4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Żółw 1
player = turtle.Turtle()
player.penup()
player.setposition(200,0)
player.setheading(180)
player.color("purple")
player.shape("turtle")
player.speed(V1)

#Żółw 2
player2 = turtle.Turtle()
player2.penup()
player2.setposition(-200,0)
player2.color("orange")
player2.shape("turtle")
player2.speed(V2)

#Żółw 3
player3 = turtle.Turtle()
player3.penup()
player3.setposition(0,0)
player3.color("pink")
player3.shape("turtle")
V3= int(input())
player3.speed(V3)

i = 1
while True:
    player.forward(player.speed())
    player2.forward(player2.speed())
    player3.forward(player3.speed())

    #Zderzenia
    if player2.xcor() > (player3.xcor() - 10 ):
        Vk1 = abs(V2 * (M2 - M3) / (M2 + M3) + V3 * (2 * M3) / (M2 + M3))
        Vk2 = abs(V2 * (2 * M2) / (M2 + M3) + V3 * (M3 - M1) / (M1 + M3))
        player3.setheading(180)
        player3.left(180)
        player3.speed(Vk1)
        player2.right(180)
        player2.speed(Vk2)
        print('Zderzenie:', i)
        print('Wartość prędkości końcowej pomarańczowego żółwia wynosi:', Vk2)
        print('Wartość prędkości końcowej różowego żółwia wynosi:', Vk1)
        V3 = Vk2
        V2 = Vk1
        i += 1
    elif player3.xcor() > (player.xcor() - 10):
        V1k = abs(V1 * (M1 - M3) / (M1 + M3) + V3 * (2 * M3) / (M1 + M3))
        V2k = abs(V1 * (2 * M1) / (M1 + M3) + V3 * (M3 - M1) / (M1 + M3))
        player.left(180)
        player.speed(V1k)
        player3.right(180)
        player3.speed(V2k)
        print('Zderzenie:', i)
        print('Wartość prędkości końcowej fioletowego żółwia wynosi:', V1k)
        print('Wartość prędkości końcowej różowego żółwia wynosi:', V2k)
        V3 = V2k
        V1 = V1k
        i += 1

    #Od ścian
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    if player2.xcor() > 300 or player2.xcor() < -300:
        player2.right(180)