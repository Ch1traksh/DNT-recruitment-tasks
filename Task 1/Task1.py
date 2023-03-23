import turtle as t

pen = t.Turtle()
pen.speed(10)

colours = ["green", "blue", "purple", "red"]
travel = 150
min_length = 20
step = 1
angle = 88

while(travel > min_length):
    pen.color(colours[travel % 4])
    pen.fd(travel)
    pen.left(angle)
    travel = travel - step

t.exitonclick()