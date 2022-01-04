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


wn = turtle.Screen()
wn.bgcolor("lightblue")

#Draw border
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

#Create player 1
player = turtle.Turtle()
player.penup()
player.setposition(200,0)
player.setheading(180)
player.color("red")
player.shape("turtle")

player.speed(V1)

#Create player 2
player2 = turtle.Turtle()
player2.penup()
player2.setposition(-200,0)
player2.color("aqua")
player2.shape("turtle")

player2.speed(V2)

def definicja(self, V1, V2):
    self.V1 = V1
    self.V2 = V2

def update(V1,V2):
    self.V1 = V1k
    self.V2 = V2k

zolwie = []
zolwie.append(player)
zolwie.append(player2)

a = 1

while True:
    player.forward(player.speed())
    player2.forward(player2.speed())

    V1k = V1 * (M1 - M2) / (M1 + M2) + V2 * (2 * M2) / (M1 + M2)
    V2k = V1 * (2 * M1) / (M1 + M2) + V2 * (M2 - M1) / (M1 + M2)


    if player2.xcor() > (player.xcor() - 10 ):
        player.left(180)
        player.speed(V1k)
        player2.right(180)
        player2.speed(V2k)
        print('Zderzenie:', a)
        print('Wartość prędkości końcowej pierwszej kulki wynosi:', V1k)
        print('Wartość prędkości końcowej drugiej kulki wynosi:', V2k)
        V1 = V1k
        V2 = V2k
        a += 1

    #Bouandary
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    #Bouandary2
    if player2.xcor() > 300 or player2.xcor() < -300:
        player2.right(180)