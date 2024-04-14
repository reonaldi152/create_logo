from turtle import *  # Import the turtle module

# The objective is to create a YouTube logo on Python with turtle

# Set the pen to the first point of the logo
penup()  # Move the pen to the specified position without leaving a trail
goto(-140, -100)  # Move the pen to the position (-140, -100)
pendown()  # Start drawing

fillcolor('red')  # Set the fill color to red

begin_fill()  # Start filling the color

for i in [330, 150, 330, 150]:  # This list contains the forward distances
    forward(i)  # Move the pen forward by the specified distance
    circle(100, 90)  # Draw a circle with the specified radius and angle

end_fill()  # End filling the color

# Set the pen to the second point of the logo
penup()
goto(-15, 15)
pendown()

fillcolor('white')  # Set the fill color to white

begin_fill()  # Start filling the color

for i in [30, 120, 120]:  # This list contains the left angles
    left(i)  # Turn the pen left by the specified angle
    forward(150)  # Move the pen forward by the specified distance

end_fill()  # End filling the color

hideturtle()  # Hide the turtle

done()  # Close the turtle graphics window