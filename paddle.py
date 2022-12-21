from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.position(direction)
        self.shapesize(1, 5, 0)
        self.left(90)

    def up(self):
        self.forward(30)

    def down(self):
        self.back(30)

    def position(self, direction):
        if direction == "left":
            self.goto(x=370, y=0)

        if direction == "right":
            self.goto(x=-370, y=0)
