from turtle import *

# Define a scaling factor
scale_factor = 0.5  # Adjust this as needed

# The objective is to create HBO logo on python with turtle

# LETTER H

fillcolor('black') # Set the fill color to black

# Set the pen to the first point of the logo
penup()
goto(-150 * scale_factor, 0 * scale_factor)  # Apply scaling to initial position
pendown()
begin_fill() # Start filling the shape

# Create variable for LETTER H that contain length and width of the first line
lengthWidthFirstLine = [200 * scale_factor, 50 * scale_factor, 200 * scale_factor, 50 * scale_factor]

left(90)
for i in lengthWidthFirstLine:
    forward(i)
    circle(0, -90)

end_fill() # End filling the shape

fillcolor('black') # Set the fill color to black

# Set the pen to the first point of the logo

penup()
goto(-65 * scale_factor, 0 * scale_factor)  # Apply scaling to initial position
pendown()

begin_fill() # Start filling the shape

for i in lengthWidthFirstLine:
    forward(i)
    circle(0, -90)

end_fill() # End filling the shape

fillcolor('black') # Set the fill color to black

penup()
goto(-100 * scale_factor, 125 * scale_factor)  # Apply scaling to initial position
pendown()
begin_fill()

# to make it simple, im use while loop, 

line = 0 # the iterators 
left(-90)
while line < 4 : 
    forward(35 * scale_factor)
    circle(0, -90)
    line += 1 # increment the iterator

end_fill()


# LETTER B

penup()
goto(0 * scale_factor, 0 * scale_factor)  # Apply scaling to initial position
pendown()
begin_fill()

left(90)
for i in lengthWidthFirstLine:
    forward(i)
    circle(0, -90)
        
end_fill()

begin_fill()

right(90)
forward(90 * scale_factor)
circle(53 * scale_factor, 180)
left(90)
forward(12 * scale_factor)
left(-90)
right(180)
circle(53 * scale_factor, 180)
forward(90 * scale_factor)

end_fill()

fillcolor('white')
penup()
goto(50 * scale_factor, 35 * scale_factor)  # Apply scaling to initial position
pendown()
begin_fill()

right(180)
forward(20 * scale_factor)
circle(20 * scale_factor, 180)
forward(20 * scale_factor)
left(90)
forward(50 * scale_factor)

end_fill()

penup()
goto(50 * scale_factor, 125 * scale_factor)  # Apply scaling to initial position
pendown()
begin_fill()

left(90)
forward(20 * scale_factor)
circle(20 * scale_factor, 180)
forward(20 * scale_factor)
left(90)
forward(50 * scale_factor)

end_fill()

# LETTER O

fillcolor('black')
penup()
goto(230 * scale_factor, 0 * scale_factor)  # Apply scaling to initial position
pendown()
begin_fill()

left(90)
circle(100 * scale_factor, 360)
end_fill()

fillcolor('white')
penup()
goto(230 * scale_factor, 50 * scale_factor)  # Apply scaling to initial position
pendown()

begin_fill()

circle(50 * scale_factor, 360)

end_fill()

fillcolor('black')
penup()
goto(230 * scale_factor, 60 * scale_factor)  # Apply scaling to initial position
pendown()
begin_fill()

circle(40 * scale_factor, 360)

end_fill()

hideturtle()  # Hide the turtle

done()

# Adding shape transformation to the whole drawing
shapetransform(((0.8, 0), (0, 1.2), (0, 0), (0, 0), (0, 0)))
