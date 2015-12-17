import turtle
import random

class Arrow (turtle.Turtle):
    def ___init___ (self, xvel=300):
        turtle.Turtle.___init___(self)
        self.tracer(0)

    def reset_direction (self):
        self.setheading(60)
    def reset_direction_again (self):
        self.setheading(-60)
    def thrusters(self):
        self.forward(50)
    def move(self):
        pass
    def reset(self):
        self.up()
        self.goto(0,0)
        oliver.down()
        a=["Red","Blue"]
        colorvalue=random.randint(0,2)
        self.color(a[colorvalue])
oliver = Arrow()

laura = Arrow()

wn = turtle.Screen()
#oliver = turtle.Turtle()



def screenClicked(x,y):
    a = ["Red","Blue","Green", "Medium Blue", "Lime Green", "DodgerBlue", "Dark Blue"]
    b= ["Orange", "C", "aqua", "gold", "darkkhaki", "royalblue", "peru", "magneta"]
    colorvalue=random.randint(0,6)
    oliver.color(a[colorvalue])
    laura.color(b[colorvalue])




wn.onkey(oliver.reset_direction, 'Up')
wn.onkey(laura.reset_direction,'W')
wn.onkey(oliver.reset_direction_again, "Down")
wn.onkey(laura.reset_direction_again, "s")
wn.onkey(h3, "Left")
wn.onkey(h4, "Right")
wn.onkey(h3, "a")#for laura
wn.onkey(h4, "d")#for laura
wn.onkey(oliver.thrusters, "Up")
wn.onkey(laura.thrusters, "f")
wn.onkey(oliver.reset, "0")
wn.onclick(screenClicked)        
wn.listen()
