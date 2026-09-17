import time
from turtle import *

speed(0)


#Defining the Function to a square
def square():
    for i in range(4):
        forward(25)
        right(90)
        

#Drawing 4 Tetris Blocks in a row
for i in range(4):
    square()
    forward(25)

penup()
forward(100)
pendown()

#Drawing a Square of Squares
for i in range(4):
    square()
    left(90)


time.sleep(3)
