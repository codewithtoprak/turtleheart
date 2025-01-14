import math
import turtle

ekran = turtle.Screen()
ekran.bgcolor("black")
ekran.title("Güzel Sevgilime...")

kalem = turtle.Turtle()
kalem.color("red")
kalem.speed(0)
kalem.hideturtle()

def kalp(t):
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x, y


kalem.penup()
for i in range(10):
    kalem.goto(0, 0)
    kalem.pendown()
    for t in range(0, 100, 2):
        x, y = kalp(t / 10)
        kalem.goto(x * i, y * i)

    kalem.penup()

turtle.done
ekran.mainloop()