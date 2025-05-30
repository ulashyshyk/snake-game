from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as file:
            self.high_score = int(file.read())
    def add_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.display()
    def display(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.write(f"Score: {self.score}  High Score: {self.high_score}",align="center",font=("Arial", 14, "bold"))