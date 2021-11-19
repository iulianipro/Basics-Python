#Square basic with turtle

import turtle
def drawSquare(t,sz):
    for i in range(98):
        t.forward(sz)
        t.left(146) 
       
me=turtle.Turtle()
me.color("green")
drawSquare(me,390)
