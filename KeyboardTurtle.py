import turtle
import random

class Arrow (turtle.Turtle):
    def ___init___ (self, xvel=300):
        turtle.Turtle.___init___(self)
        self.tracer(0)

    def reset_direction (self):
        self.setheading(60)
    def thrusters(self):
        self.forward(50)
    def move(self):
        pass
oliver = Arrow()

laura = Arrow()

wn = turtle.Screen()
#oliver = turtle.Turtle()

def h1():
    oliver.setheading(50)

def h2():
    oliver.circle(45,5)

def h3():
    oliver.setheading(-60)

def h4():
    oliver.circle(-45,5)

def Return_to_Origin():
    oliver.up()
    oliver.goto(0,0)
    oliver.down()
    b = ["Red", "Blue", "Green"]
    colorvalue=random.randint(0,2)
    oliver.color(b[colorvalue])

def screenClicked(x,y):
    a = ["Red","Blue","Green", "Medium Blue", "Lime Green", "DodgerBlue", "Dark Blue"]
    b= ["Orange", "C", "aqua", "gold", "darkkhaki", "royalblue", "peru", "magneta"]
    colorvalue=random.randint(0,6)
    oliver.color(a[colorvalue])
    laura.color(b[colorvalue])


wn.onkey(oliver.reset_direction, 'Up')
wn.onkey(laura.reset_direction,'a')
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Down")
wn.onkey(h4, "Right")
wn.onkey(oliver.thrusters, "Up")
wn.onkey(laura.thrusters, "f")
wn.onkey(Return_to_Origin, "0")
wn.onclick(screenClicked)        
wn.listen()
