import time
from turtle import *

speed(0)
hideturtle()  # Hide the turtle cursor for a cleaner look

#Defining the function to draw a red Triangle
def draw_red_triangle():
    pencolor('red')  # Set the pen color to red
    pensize(5)  # Set the pen size for the triangle
    for i in range(3):  # Loop to draw 3 sides of the triangle
        forward(100)  # Move the turtle forward to draw a side of the triangle
        left(120)  # Turn the turtle to the left by 120 degrees to draw the next side

draw_red_triangle()  # Call the function to draw the red triangle


#Drawing the Exclamation mark
penup()  # Lift the pen to move without drawing
forward(50)  # Move the turtle forward to position for the Exclamation mark
left(90)  # Turn the turtle to face upwards
forward(10)  # Move the turtle forward to position for the Exclamation mark


#Drawing the dot of the Exclamation mark
dot(10, 'Black')  # Draw the dot of the Exclamation mark

#Drawing the line of the Exclamation mark
forward(15)  # Move the turtle forward to position for the line of the Exclamation mark
pensize(6)  # Set the pen size for the line of the Exclamation mark
pendown()  # Lower the pen to start drawing
pencolor('Black')  # Set the pen color to black
forward(40) # Draw the line of the Exclamation mark

time.sleep(2)  # Pause for 2 seconds to view the drawing