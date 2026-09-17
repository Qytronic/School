import time
from turtle import *

x = 0

def triangle(length):
    for i in range(3):
        forward(length)
        left(120)

for i in range(3):
    triangle(x + 100)
    x += 100
    
time.sleep(5)
