from asyncore import write
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score: {self.score} | Highscore: {self.highscore}", False, align="center",
                   font=('Arial', 10, 'bold'))
        self.load_highscore()

    def update(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score} | Highscore: {self.highscore}", False, align="center",
                   font=('Arial', 10, 'bold'))

    def add(self):
        self.score += 1
        self.update()

    def gameover(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update()
        self.goto(0, 260)
        self.write(f"GAME OVER! Game has been restarted!", False, align="center", font=('Arial', 10, 'bold'))

    def load_highscore(self):
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
            print(self.highscore)
            self.update()
