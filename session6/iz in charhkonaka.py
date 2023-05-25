import turtle 
import time 
num = 6

forw = 25
leif = 90
forw2 = 55
angle = 360.0 / num
color = ["yellow", "orange", "red", "purple", "blue", "green"]
turtle.bgcolor("black")
p = turtle.Pen(shape= "turtle")
p.pencolor("white")
p.left(30)
for i in range(3):
    p.forward(30)
    p.left(120)

p.up()
p.forward(5)
p.right(100)
p.forward(15)
p.down()
p.left(100)
p.forward(40)



for j in range(4):
    p.left(90)
    p.forward(50)

p.up()
p.forward(forw)
p.down()
p.left(leif)
for i in range(num):
            
        p.forward(forw2)
        p.left(angle)

    # forw += 2
    # leif += 2
    # forw2 += 5
    # num +=    
        
    
