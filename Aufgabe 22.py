import time
from turtle import *

speed(0)

#Defining the Function to a hexagon
def hexagon():
    for i in range(6):
        forward(50)
        left(60)

for i in range(3):
    hexagon()
    penup()
    right(120)
    backward(50)
    pendown()
    
    
time.sleep(5)
