from turtle import *  # Import the turtle module

# Define a scaling factor
scale_factor = 0.5  # Adjust this as needed

# The objective is to create a YouTube logo on Python with turtle

# Set the pen to the first point of the logo
penup()  # Move the pen to the specified position without leaving a trail
goto(-140 * scale_factor, -100 * scale_factor)  # Apply scaling to initial position
pendown()  # Start drawing

fillcolor('red')  # Set the fill color to red

begin_fill()  # Start filling the color

for i in [330 * scale_factor, 150 * scale_factor, 330 * scale_factor, 150 * scale_factor]:  # This list contains the forward distances
    forward(i)  # Move the pen forward by the specified distance
    circle(100 * scale_factor, 90)  # Draw a circle with the specified radius and angle

end_fill()  # End filling the color

# Set the pen to the second point of the logo
penup()
goto(-15 * scale_factor, 15 * scale_factor)  # Apply scaling to initial position
pendown()

fillcolor('white')  # Set the fill color to white

begin_fill()  # Start filling the color

for i in [30, 120, 120]:  # This list contains the left angles
    left(i)  # Turn the pen left by the specified angle
    forward(150 * scale_factor)  # Move the pen forward by the specified distance

end_fill()  # End filling the color

hideturtle()  # Hide the turtle

done()  # Close the turtle graphics window
