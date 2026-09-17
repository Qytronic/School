import time
from turtle import *

dot(50, 'black')
def square(size):
    for i in range(4):
        forward(size)
        right(90)
        
        
def pattern():
    x = 0
    for i in range(3):
        square(x + 100)
        x += 100

pattern()

time.sleep(5)