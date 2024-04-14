from turtle import *

# Define a scaling factor
scale_factor = 0.5  # Adjust this as needed

# Set the background color of the screen
screensize(400 * scale_factor, 400 * scale_factor, '#1E1A29')

# Set the pen size and color for the border of the logo
pensize(2 * scale_factor)
pencolor('#870064')

# Define the coordinates for the upper and lower parts of the letter 'T'
letterTUpper = [140 * scale_factor, 26 * scale_factor, 306 * scale_factor, 26 * scale_factor, 140 * scale_factor]
letterTLower = [280 * scale_factor, 26 * scale_factor, 280 * scale_factor]

# Draw the first 'T' letter
fillcolor('#EE3FB0')  # Set the fill color to pink
penup()
goto(-55 * scale_factor, 325 * scale_factor)  # Move the pen to the starting position
pendown()
begin_fill()

# Draw the upper part of the 'T' letter
left(180)
for i in letterTUpper:
    forward(i)
    left(-90)

# Draw the lower part of the 'T' letter
left(-180)
for i in letterTLower:
    forward(i)
    left(-90)

end_fill()

# Draw the second 'T' letter
penup()
goto(0 * scale_factor, 273 * scale_factor)
pendown()
begin_fill()

# Draw the upper part of the 'T' letter
left(180)
for i in letterTUpper:
    forward(i)
    left(-90)

# Draw the lower part of the 'T' letter
left(-180)
for i in letterTLower:
    forward(i)
    left(-90)

end_fill()

# Define the coordinates for the upper and lower parts of the second letter 'T'
secondLetterTUpper = [105 * scale_factor, 18 * scale_factor, 230 * scale_factor, 18 * scale_factor, 105 * scale_factor]
secondLetterTLower = [210 * scale_factor, 18 * scale_factor, 210 * scale_factor]

# Draw the first 'T' letter of the second row
fillcolor('#EE3FB0')
penup()
goto(-265 * scale_factor, -115 * scale_factor)
pendown()
begin_fill()

# Draw the upper part of the 'T' letter
left(180)
for i in secondLetterTUpper:
    forward(i)
    left(-90)

# Draw the lower part of the 'T' letter
left(-180)
for i in secondLetterTLower:
    forward(i)
    left(-90)

end_fill()

# Draw the 'Y' letter
penup()
goto(-137 * scale_factor, -97 * scale_factor)
pendown()
begin_fill()

# Draw the 'Y' letter
forward(23 * scale_factor)
left(-45)
forward(120 * scale_factor)
left(90)
forward(120 * scale_factor)
left(-45)
forward(23 * scale_factor)
left(225)
forward(140 * scale_factor)
left(45)
forward(135 * scale_factor)
left(-90)
forward(18 * scale_factor)
left(-90)
forward(135 * scale_factor)
left(45)
forward(140 * scale_factor)

end_fill()

# Draw the second 'Y' letter with rotation and scaling using shapetransform()
penup()
goto(85 * scale_factor, -97 * scale_factor)
pendown()
begin_fill()

# Define the shape for the second 'Y' letter
second_Y_shape = ((0, 0), (0.2, 0.2), (0, 0.6), (-0.2, 0.2), (0, 0))

# Apply rotation and scaling to the shape
shapetransform(((0.8, 0), (0, 1.2), (0, 0), (0, 0), (0, 0)))

# Set the shape
shape(second_Y_shape)

end_fill()

hideturtle()  # Hide the turtle

done()  # Close the turtle graphics window
