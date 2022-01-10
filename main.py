import turtle
import tkinter
from tkinter import *
from tkinter import ttk

def velocity(a,b,m,n):
    V1k = a * (m - n) / (m + n) + b * (2 * n) / (m + n)
    V2k = a * (2 * m) / (m + n) + b * (n - m) / (m + n)
    return V1k, V2k

def zolw(v1,v2,m1,m2):
    print(v1,v2,m1,m2)
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
    V3=0
    player3.speed(V3)

    i = 1

    while True:
        player.forward(player.speed())
        player2.forward(player2.speed())
        player3.forward(player3.speed())

        #Zderzenia
        if player2.xcor() > (player3.xcor() - 10 ):
            velocity(V3,V2,M3,M2)
            player3.left(180)
            player3.speed(V1k)
            player2.right(180)
            player2.speed(V2k)
            print('Zderzenie:', i)
            print('Wartość prędkości końcowej pierwszej kulki wynosi:', V1k)
            print('Wartość prędkości końcowej drugiej kulki wynosi:', V2k)
            V3 = V1k
            V2 = V2k
            i += 1
        elif player3.xcor() > (player.xcor() - 10):
            velocity(V1, V3, M1, M3)
            player.left(180)
            player.speed(V1k)
            player3.right(180)
            player3.speed(V2k)
            print('Zderzenie:', i)
            print('Wartość prędkości końcowej pierwszej kulki wynosi:', V1k)
            print('Wartość prędkości końcowej drugiej kulki wynosi:', V2k)
            V3 = V1k
            V2 = V2k
            i += 1

        #Od ścian
        if player.xcor() > 300 or player.xcor() < -300:
            player.right(180)
        if player2.xcor() > 300 or player2.xcor() < -300:
            player2.right(180)


root_window = Tk() #Creates window
root_window.title("Wartości prędkości i masy") #Gives title to window
root_window.geometry("500x500") #Makes the window size 500x500
#Create Label and Entry for username
Label(root_window, text = "masa pierwszej kulki:").pack()
masa1Entry = Entry(root_window)
masa1Entry.pack()
Label(root_window, text = "masa drugiej kulki:").pack()
masa2Entry = Entry(root_window)
masa2Entry.pack()
#Create Label and Entry for password
Label(root_window, text = "Wartość prędkości pierwszej kulki").pack()
prędkość1Entry = Entry(root_window)
prędkość1Entry.pack()
Label(root_window, text = "Wartość prędkości drugiej kulki").pack()
prędkość2Entry = Entry(root_window)
prędkość2Entry.pack()
#Get inputted data from the Entry widgets
submitteprędkość1 = prędkość1Entry.get()
submitteprędkość2 = prędkość2Entry.get()
submittedmasa1 = masa1Entry.get()
submittedmasa2 = masa2Entry.get()
#Create button that calls your loginHandler Function
funCall = lambda: x(submitteprędkość1, submitteprędkość2, submittedmasa1, submittedmasa2)
Button(root_window, text = "Gotowe", command =lambda: zolw(submitteprędkość1,submitteprędkość2,submittedmasa1,submittedmasa2)).pack()
root_window.mainloop()
M3 = int(input())
wn = turtle.Screen()
wn.bgcolor("lightblue")