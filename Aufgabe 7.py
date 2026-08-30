import time
from turtle import *

speed(0)
hideturtle()  # Hide the turtle cursor for a cleaner look
penup()

#Defining the List of colors for the Circles
colors = ['yellow', 'blue', 'green', 'red',]  # List of colors for the circles

for color in colors:  # Loop through each color in the list
    dot(100, color)  # Draw a circle with the current color
    forward(200)  # Move the turtle forward to position for the next circle
    left(90)  # Turn the turtle to the right by 90 degrees
    
time.sleep(2)  # Pause for 2 seconds to view the drawing


