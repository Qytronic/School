import time
from turtle import *

speed(0)
hideturtle()  # Hide the turtle cursor for a cleaner look

#Defining the function to draw a no entry sign 
def draw_no_entry_sign(color):
    dot(100, 'red')  # Draw the red circle
    dot(80, color)  # Draw the inner circle with the specified color

draw_no_entry_sign('white')  # Call the function with 'white' as the inner circle color

penup()
forward(200)  # Move the turtle forward to position for the next sign
pendown()

draw_no_entry_sign('blue')  # Call the function with 'blue' as the inner circle color

pensize(8)  # Set the pen size for the Diagonal line
pencolor('red')  # Set the pen color to red
right(45)  # Turn the turtle to the right by 45 degrees
forward(40)  # Move the turtle forward to draw the Diagonal line
back(80)  # Move the turtle backward to draw the other half of the Diagonal line

time.sleep(2)  # Pause for 2 seconds to view the drawing


