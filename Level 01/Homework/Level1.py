from turtle import * 

#we want to paint a house
# es
#step 1: draw a square
speed(7)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90) 

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawfing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
right(330)
end_fill()

penup()
goto(20, 175)
pendown()

color("blue")
forward(45)
left(90)        

forward(45)
left(90)
forward(45)
left(90)
forward(45)
right(180)
forward(22.5)
right(90)
forward(45)
right(90)
forward(22.5)
right(90)
forward(22.5)
right(90)
forward(45)

penup()
goto(180, 175)
pendown()

left(180)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(22.5)
left(90)
forward(45)
left(90)
forward(22.5)
left(90)
forward(22.5)
left(90)
forward(45)






exitonclick()