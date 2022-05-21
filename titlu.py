from turtle import Turtle
class Titlu(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 320)
        self.color("white")
        self.write("Harta Romaniei", font=('Times New Roman', 26, 'bold'), align="center")
