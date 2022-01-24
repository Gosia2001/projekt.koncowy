import turtle
from tkinter import *


def zolw(V1, V2, V3, M1, M2, M3):
    wn = turtle.Screen()
    wn.bgcolor("lightblue")

    # ściany
    mypen = turtle.Turtle()
    mypen.penup()
    mypen.pencolor('black')
    mypen.setposition(-300, -300)
    mypen.pendown()
    mypen.pensize(3)
    for side in range(4):
        mypen.forward(600)
        mypen.left(90)
    mypen.hideturtle()

    # Żółw 1
    player = turtle.Turtle()
    player.penup()
    player.setposition(200, 0)
    player.setheading(180)
    player.color("purple")
    player.shape("turtle")
    player.speed(V1)

    # Żółw 2
    player2 = turtle.Turtle()
    player2.penup()
    player2.setposition(-200, 0)
    player2.color("orange")
    player2.shape("turtle")
    player2.speed(V2)

    # Żółw 3
    player3 = turtle.Turtle()
    player3.penup()
    player3.setposition(0, 0)
    player3.color("pink")
    player3.shape("turtle")
    player3.speed(V3)

    i = 1
    while True:
        player.forward(player.speed())
        player2.forward(player2.speed())
        player3.forward(player3.speed())
        # Zderzenia
        if player2.xcor() > (player3.xcor() - 10):
            Vk1 = abs(V2 * (M2 - M3) / (M2 + M3) + V3 * (2 * M3) / (M2 + M3))
            Vk2 = abs(V2 * (2 * M2) / (M2 + M3) + V3 * (M3 - M1) / (M1 + M3))
            if player3.heading() != player2.heading():
                if player2.heading() == 0:
                    player3.setheading(180)
                    player3.left(180)
                    player3.speed(Vk1)
                    player2.right(180)
                    player2.speed(Vk2)
            elif player2.speed() > player3.speed():
                player2.left(180)
                player3.speed(Vk1)
                player2.speed(Vk2)
            elif player2.speed() < player3.speed():
                player3.left(180)
                player3.speed(Vk1)
                player2.speed(Vk2)
            print('Zderzenie:', i)
            print('Wartość prędkości końcowej pomarańczowego żółwia wynosi:', Vk2, "m/s")
            print('Wartość prędkości końcowej różowego żółwia wynosi:', Vk1, "m/s")
            V3 = Vk2
            V2 = Vk1
            i += 1
        if player3.xcor() > (player.xcor() - 10):
            V1k = abs(V1 * (M1 - M3) / (M1 + M3) + V3 * (2 * M3) / (M1 + M3))
            V2k = abs(V1 * (2 * M1) / (M1 + M3) + V3 * (M3 - M1) / (M1 + M3))
            if player3.heading() != player.heading():
                if player.heading() == 180:
                    player.left(180)
                    player.speed(V1k)
                    player3.right(180)
                    player3.speed(V2k)
            elif player.speed() > player3.speed():
                player.left(180)
                player.speed(V1k)
                player3.speed(V2k)
            elif player.speed() < player3.speed():
                player3.left(180)
                player.speed(V1k)
                player3.speed(V2k)
            print('Zderzenie:', i)
            print('Wartość prędkości końcowej fioletowego żółwia wynosi:', V1k, "m/s")
            print('Wartość prędkości końcowej różowego żółwia wynosi:', V2k, "m/s")
            V3 = V2k
            V1 = V1k
            i += 1

        # Od ścian
        if player.xcor() > 300 or player.xcor() < -300:
            player.right(180)
        if player2.xcor() > 300 or player2.xcor() < -300:
            player2.right(180)


if __name__ == '__main__':
    root_window = Tk()  # Creates window
    root_window.title("Wartości prędkości i masy")
    root_window.geometry("500x500")

    Label(root_window, text="masa pierwszego żółwia (kg):").pack()
    masa1Entry = Scale(root_window, from_=1, to=5, orient=HORIZONTAL)
    masa1Entry.pack()
    Label(root_window, text="masa drugiego żółwia (kg):").pack()
    masa2Entry = Scale(root_window, from_=1, to=5, orient=HORIZONTAL)
    masa2Entry.pack()
    Label(root_window, text="masa trzeciego żółwia (kg):").pack()
    masa3Entry = Scale(root_window, from_=1, to=5, orient=HORIZONTAL)
    masa3Entry.pack()

    Label(root_window, text="Wartość prędkości pierwszego żółwia (m/s):").pack()
    predkosc1Entry = Scale(root_window, from_=0, to=10, orient=HORIZONTAL)
    predkosc1Entry.pack()
    Label(root_window, text="Wartość prędkości drugiego żółwia (m/s):").pack()
    predkosc2Entry = Scale(root_window, from_=0, to=10, orient=HORIZONTAL)
    predkosc2Entry.pack()
    Label(root_window, text="Wartość prędkości trzeciego żółwia (m/s):").pack()
    predkosc3Entry = Scale(root_window, from_=0, to=10, orient=HORIZONTAL)
    predkosc3Entry.pack()

    # funCall = lambda: (submittepredkosc1, submittepredkosc2, submittepredkosc3, submittedmasa1, submittedmasa2, submittedmasa3)
    Button(root_window, text="Gotowe",
           command=lambda: zolw(int(predkosc1Entry.get()), int(predkosc2Entry.get()), int(predkosc3Entry.get()),
                                int(masa1Entry.get()), int(masa2Entry.get()),
                                int(masa3Entry.get()))).pack()
    root_window.mainloop()