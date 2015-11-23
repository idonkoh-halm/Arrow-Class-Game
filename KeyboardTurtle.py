#Original Code  from http://openbookproject.net/thinkcs/python/english3e/events.html
import turtle


wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("darkgoldenrod")
oliver = turtle.Turtle()


def h1():
    oliver.setheading(60)

def h2():
    oliver.circle(45,5)
def h3():
   oliver.setheading(-60)
def h4():
    oliver.circle(45,5)

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Down")
wn.onkey(h4, "right")
turtle.onclick(turtle.forward(70))


wn.listen()
