from turtle import *

# The objective is to create HBO logo on python with turtle

# LETTER H

fillcolor('black') # Set the fill color to black

# Set the pen to the first point of the logo
penup()
goto(-150, 0)
pendown()
begin_fill() # Start filling the shape

# Create variable for LETTER H that contain length and width of the first line

lengthWidthFirstLine = [200,50,200,50]

left(90)
for i in lengthWidthFirstLine:
    forward(i)
    circle(0, -90)

end_fill() # End filling the shape

fillcolor('black') # Set the fill color to black

# Set the pen to the first point of the logo

penup()
goto(-65, 0)
pendown()

begin_fill() # Start filling the shape

for i in lengthWidthFirstLine:
    forward(i)
    circle(0, -90)

end_fill() # End filling the shape

fillcolor('black') # Set the fill color to black

penup()
goto(-100, 125)
pendown()
begin_fill()

# to make it simple, im use while loop, 

line = 0 # the iterators 
left(-90)
while line < 4 : 
    forward(35)
    circle(0, -90)
    line += 1 # increment the iterator

end_fill()


# LETTER B

penup()
goto(0, 0)
pendown()
begin_fill()

left(90)
for i in lengthWidthFirstLine:
    forward(i)
    circle(0, -90)
        
end_fill()

begin_fill()

right(90)
forward(90)
circle(53, 180)
left(90)
forward(12)
left(-90)
right(180)
circle(53, 180)
forward(90)

end_fill()

fillcolor('white')
penup()
goto(50, 35)
pendown()
begin_fill()

right(180)
forward(20)
circle(20, 180)
forward(20)
left(90)
forward(50)

end_fill()

penup()
goto(50, 125)
pendown()
begin_fill()

left(90)
forward(20)
circle(20, 180)
forward(20)
left(90)
forward(50)

end_fill()

# LETTER O

fillcolor('black')
penup()
goto(230, 0)
pendown()
begin_fill()

left(90)
circle(100, 360)
end_fill()

fillcolor('white')
penup()
goto(230, 50)
pendown()

begin_fill()

circle(50, 360)

end_fill()

fillcolor('black')
penup()
goto(230, 60)
pendown()
begin_fill()

circle(40, 360)

end_fill()

hideturtle()  # Hide the turtle

done()
