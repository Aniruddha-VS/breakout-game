from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super(Paddle, self).__init__()

        self.goto(pos)
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("blue")
        self.go_right()
        self.go_left()

    def go_right(self):
        self.goto(self.xcor()+20, self.ycor())

    def go_left(self):
        self.goto(self.xcor()-20, self.ycor())
