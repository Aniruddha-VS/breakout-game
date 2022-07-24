from turtle import Turtle

class Brick(Turtle):
    def __init__(self, pos):
        super().__init__()

        self.goto(pos)
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=2, stretch_len=1)




    def disappear(self):
        self.goto(500, 500)
