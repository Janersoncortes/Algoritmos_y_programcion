from turtle import*
import random
bgcolor("black")
penup()
goto(-600,100)
pendown()
pensize(1)
color("green")
speed(0)
begin_fill()
right(110)
p=1
while p <5:
    forward(150)
    left(145)
    p=p+1
end_fill()
penup()
goto(-620,40)
pendown()
pensize(10)
pencolor("white")
right(470)
forward(40)
backward(20)
right(90)
forward(40) 
right(90)
forward(20) 
#dos
penup()
goto(-450,100)
pendown()
pensize(1)
color("yellow")
speed(0)
begin_fill()
left(70)
p=1
while p <5:
    forward(150)
    left(145)
    p=p+1
end_fill()
penup()
goto(-450,40)
pendown()
pensize(10)
pencolor("red")
left(500)
forward(40)
backward(40)
left(40)
forward(40)
backward(10) 
right(110)
forward(15)
#tres
penup()
goto(-300,100)
pendown()
pensize(1)
color("red")
speed(0)
begin_fill()
left(70)
p=1
while p <5:
    forward(150)
    left(145)
    p=p+1
end_fill()
penup()
goto(-315,40)
pendown()
right(110)
pensize(10)
pencolor("white")
right(90)
forward(45)
backward(45)
left(30)
forward(50) 
left(150)
forward(45)
#cuatro
penup()
goto(-80,45)
pendown()
pensize(1)
pencolor("black")
color("green")
speed(0)
begin_fill()
left(90)
p=1
while p <5:
    forward(150)
    left(145)
    p=p+1
end_fill()
penup()
goto(-165,40)
pendown()
right(40)
pensize(10)
pencolor("white")
forward(20)
backward(20)
right(90)
forward(20)
left(90)
forward(20)
backward(20)
right(90)
forward(20)
left(90)
forward(20)
#cinco
penup()
goto(-50,-40)
pendown()
pensize(1)
color("yellow")
speed(0)
begin_fill()
left(35)
p=1
while p <5:
    forward(150)
    left(145)
    p=p+1
end_fill()
penup()
goto(-15,40)
pendown()
pensize(10)
pencolor("red")
left(15)
forward(40)
backward(40)
left(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
left(135)
forward(30)
#seis
penup()
goto(155,100)
pendown()
pensize(1)
pencolor("black")
color("red")
speed(0)
begin_fill()
left(-65)
p=1
while p <5:
    forward(150)
    left(145)
    p=p+1
end_fill()
penup()
goto(165,0)
pendown()
pensize(10)
pencolor("white")
left(70)
forward(20)
backward(20)
right(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
#siete
penup()
goto(345,-45)
pendown()
pensize(1)
pencolor("black")
color("green")
speed(0)
begin_fill()
left(105)
p=1
while p <5:
    forward(150)
    left(145)
    p=p+1
end_fill()
penup()
goto(315,0)
pendown()
pensize(10)
right(145)
pencolor("white")
forward(20)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
#ocho
penup()
goto(377,47)
pendown()
pensize(1)
pencolor("black")
color("yellow")
speed(0)
begin_fill()
left(52)
p=1
while p <5:
    forward(150)
    left(145)
    p=p+1
end_fill()
penup()
goto(465,-2)
pendown()
right(50)
pensize(10)
pencolor("red")
right(40)
forward(45)
backward(45)
left(30)
forward(50) 
left(150)
forward(45)
penup()
goto(0,0)
pendown() 
pensize(2)       
speed(0)
bgcolor("black")
r,g,b=255,0,0

for i in range(255*2):
    colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3
    fd(20+i)
    rt(45)
    pencolor(r,g,b)        
mainloop()