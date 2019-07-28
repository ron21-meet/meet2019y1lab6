import turtle
turtle.speed(0.1)
num_pts = int(input("pick a number"))
for i in range(num_pts):
    turtle.lt(360/num_pts)
    turtle.fd(100)

turtle.done()
