import numpy as np
import random

def create_board():
    return np.full((3, 3), " ")

board = create_board()

#tablero
def show_board():
    print("-" * 9) #linea de separación
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
show_board()

def check_winner(board, jugador):
for row in board:
    if np.all(row == jugador):
        return True
for column in board.T:
    if np.all(column == jugador):
        return True

if np.all(np.diag(board) == jugador):
    return True
#diagonal a la inversa
if np.all(np.diag(np.fliplr(board)) == jugador):
    return True 

def empate(board):
    return not np.any(board == " ")
def jugada_usuario(board):
    while True:
        try:
            row = int(input("Fila (0-2): "))
            column = int(input("Columna (0-2): "))
            if board[row, column] == " ":
                board[row, column] = "X"
                break
            else:
                print("Esa casilla ya está ocupada.")
        except (ValueError, IndexError): #error del usuario 
            print("Entrada inválida, intenta de nuevo.")


# if board[row, column] == " ":
#     board[row, column] = "X"
# if board[row_laptop, column_laptop] == " ":
#     board[row_laptop, column_laptop] = "O"
