#Original Code  from http://openbookproject.net/thinkcs/python/english3e/events.html
import turtle
import random

wn = turtle.Screen()
oliver = turtle.Turtle()


def h1():
    oliver.setheading(60)

def h2():
    oliver.circle(45,5)
def h3():
    oliver.setheading(-60)
def h4():
    oliver.circle(45,5)
def screenClicked(x,y):
    a = ["Red","Blue","Green", "Orange"]
    colorvalue=random.randint(0,3)
    oliver.color(a[colorvalue])
def fire():
    oliver.forward(50)
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Down")
wn.onkey(h4, "Right")
wn.onclick(screenClicked)        
wn.listen()
