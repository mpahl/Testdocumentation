import numpy as np
from machine import Machine

def roboter():
    """ Die Erweckung eines Roboters """
    roboter = Machine()

    return roboter.calculator(1,3, "+")
    
print(roboter())
