from turtle import Turtle, Screen

mnk = Turtle()
screen = Screen()
screen.setup(800, 800)
screen.title("Sketch Maker")


def move_forward():
    mnk.forward(10)


def move_backward():
    mnk.backward(10)


def turn_left():
    new_heading = mnk.heading() + 10
    mnk.setheading(new_heading)


def turn_right():
    new_heading = mnk.heading() - 10
    mnk.setheading(new_heading)

def clear():
    mnk.clear()
    mnk.penup()
    mnk.home()
    mnk.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")

screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")


screen.exitonclick()


