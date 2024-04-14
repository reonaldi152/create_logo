from turtle import *  # Import the turtle module

# Set the background color of the screen
screensize(400, 400, '#1E1A29')

# Set the pen size and color for the border of the logo
pensize(2)
pencolor('#870064')

# Define the coordinates for the upper and lower parts of the letter 'T'
letterTUpper = [140, 26, 306, 26, 140]
letterTLower = [280, 26, 280]

# Draw the first 'T' letter
fillcolor('#EE3FB0')  # Set the fill color to pink
penup()
goto(-55, 325)  # Move the pen to the starting position
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
goto(0, 273)
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
secondLetterTUpper = [105, 18, 230, 18, 105]
secondLetterTLower = [210, 18, 210]

# Draw the first 'T' letter of the second row
fillcolor('#EE3FB0')
penup()
goto(-265, -115)
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
goto(-137, -97)
pendown()
begin_fill()

# Draw the 'Y' letter
forward(23)
left(-45)
forward(120)
left(90)
forward(120)
left(-45)
forward(23)
left(225)
forward(140)
left(45)
forward(135)
left(-90)
forward(18)
left(-90)
forward(135)
left(45)
forward(140)

end_fill()

# Draw the second 'Y' letter
penup()
goto(85, -97)
pendown()
begin_fill()

# Draw the 'Y' letter
left(-135)
forward(23)
left(-45)
forward(120)
left(90)
forward(120)
left(-45)
forward(23)
left(225)
forward(140)
left(45)
forward(135)
left(-90)
forward(18)
left(-90)
forward(135)
left(45)
forward(140)

end_fill()

hideturtle()  # Hide the turtle

done()  # Close the turtle graphics window