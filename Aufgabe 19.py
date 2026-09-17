import time
from turtle import *

speed(0)

#Defining the Function to draw a Square
def square():
    for i in range(4):
        forward(50)
        right(90)
    

#Defining the Function to draw a Triangle
def triangle():
    for i in range(3):
        forward(50)
        left(120)
        
        

#Drawing a House with these Functions
triangle()
forward(50)
right(90)
square()



def House():
    triangle()
    forward(50)
    right(90)
    square()

#Drawing 3 Houses in a Row
for i in range(3):
    penup()
    left(90)
    forward(100)
    pendown()
    House()
    penup()


time.sleep(3)
