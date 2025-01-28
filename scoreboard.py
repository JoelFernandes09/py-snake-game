from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 10, 'bold'))

    def update(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 10, 'bold'))

    def add(self):
        self.score += 1
        self.update()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align="center", font=('Arial', 20, 'bold'))
