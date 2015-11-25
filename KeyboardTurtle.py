#Original Code  from http://openbookproject.net/thinkcs/python/english3e/events.html
import turtle
import random

class Arrow (turtle.Turtle):
    def ___init___ (self, xvel=300):
        turtle.Turtle.___init___(self)
        self.tracer(0)
    def move(self):
        pass

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
def Return_to_Origin():
    oliver.up()
    oliver.goto(0,0)
    oliver.down()
    b = ["Red", "Blue", "Green"]
    colorvalue=random.randint(0,2)
    oliver.color(b[colorvalue])
def screenClicked(x,y):
    a = ["Red","Blue","Green", "Medium Blue", "Lime Green", "DodgerBlue", "Dark Blue"]
    colorvalue=random.randint(0,6)
    oliver.color(a[colorvalue])
def fire():
    oliver.forward(50)
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Down")
wn.onkey(h4, "Right")
wn.onkey(fire, "f")
wn.onkey(Return_to_Origin, "0")
wn.onclick(screenClicked)        
wn.listen()
