from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto((0, 280))
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=('Arial', 10, 'normal'))

    def game_over(self):
        self.goto((0, 0))
        self.write("Game over.", align="center", font=('Arial', 20, 'normal'))

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.score))

        self.score = 0
        self.update_score()
