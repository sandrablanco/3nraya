import numpy as np
import random

tablero = np.full((3, 3), " ") #tabla de 3x3 

#tablero
def show_board():
    print("-" * 9) #linea de separación
    for row in tablero:
        print(" | ".join(row))
        print("-" * 9)