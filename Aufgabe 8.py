import time
from turtle import *

speed(0)
hideturtle()  # Hide the turtle cursor for a cleaner look
left(90)  # Turn the turtle to face upwards

# Defining the function to draw a traffic light body
pensize(70)  # Set the pen size for the body of the traffic light
pencolor('black')  # Set the pen color to black
forward(100)  # Move the turtle forward to draw the body of the traffic light

# Defining the function to draw a colored circle for the traffic light
def draw_colored_circle(color):
    dot(40, color)

# Drawing the traffic light circles
penup()
back(3)
draw_colored_circle('red') 
back(50)
draw_colored_circle('yellow') 
back(50)
draw_colored_circle('green') 

time.sleep(2)