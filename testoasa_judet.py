from turtle import Turtle
class Judet(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.nume_judet="placeholder"
        self.numar_judet=-1
        self.locatie=(0,0)


    def now_color(self):
        self.clear()
        self.color("orange")
        self.write(self.numar_judet, align="center")

    def write_number(self):
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.goto(self.locatie)
        self.write(self.numar_judet, align="center")
    def write_judet(self):
        self.clear()
        self.color("green")
        self.write(self.nume_judet,align="center")
    def write_gresit(self):
        self.clear()
        self.color("red")
        self.write(self.nume_judet, align="center")
