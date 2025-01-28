from turtle import Turtle

DEFAULT_SPEED_AND_OFFSET = 20

class Snake:
    def __init__(self, length):
        self.length = length
        self.body = []
        self.next_body_offset = 0
        self.heading = 0
        self.spawn()
        self.head = self.body[0]

    def spawn(self):
        for _ in range(self.length):
            body_part = Turtle()
            body_part.shape("square")
            body_part.color("white")
            body_part.penup()
            body_part.setposition(x=self.next_body_offset, y=0)
            self.next_body_offset -= DEFAULT_SPEED_AND_OFFSET
            self.body.append(body_part)

    def move(self):
        for body_part_num in range(len(self.body) - 1, 0, -1):
            self.body[body_part_num].goto(self.body[body_part_num - 1].xcor(), self.body[body_part_num - 1].ycor())
        self.head.setheading(self.heading)
        self.head.forward(DEFAULT_SPEED_AND_OFFSET)

    def set_heading(self, heading):
        if abs(self.heading - heading) != 180:
            self.heading = heading

    def up(self):
        self.set_heading(90)

    def down(self):
        self.set_heading(270)

    def left(self):
        self.set_heading(180)

    def right(self):
        self.set_heading(0)

    def grow(self):
        body_part = Turtle()
        body_part.speed("fastest")
        body_part.shape("square")
        body_part.color("white")
        body_part.penup()
        body_part.goto(self.body[-1].position())
        self.body.append(body_part)
