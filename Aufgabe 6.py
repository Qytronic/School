import time
from turtle import *

speed(0)
hideturtle()  # Hide the turtle cursor for a cleaner look
x = 5   # Initialize the pen size for the telescope pieces

#Defining the function to draw a piece of the telescope
def draw_telescope_piece(size):
    pensize(size)  # Set the pen size for the telescope piece
    pencolor('orange')  # Set the pen color to orange
    forward(40)  # Move the turtle forward to draw the telescope piece


for i in range(4):  # Loop to draw 4 pieces of the telescope
    draw_telescope_piece(x)  # Call the function to draw a telescope piece with the specified pen size
    x += 5  # Increase the pen size for the next telescope piece

time.sleep(2)  # Pause for 2 seconds to view the drawing



