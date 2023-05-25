import turtle 
import time 

turtle.bgcolor("black")

color = ["blue","purple", "red", "green", "yellow", "orange"]

p = turtle.Pen()

i = 0
while i < 360 :
    for j in range(len(color)):
        p.width(i / 100 + 1)
        p.pencolor(color[j])
        p.forward(i)
        p.left(59)
        i += 1


turtle.done()

#time.sleep(10)