from main import mostrar_tablero
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
def empty_casillas(board):
    return np.argwhere(board == " ")
    return list(zip(row, column))
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


def laptop_move(board):
    empty_cells = empty_casillas(board)
    if empty_cells.size > 0:
        row, column = random.choice(empty_cells)
        board[row, column] = "O"

def play():
board = create_board()
mostrar_tablero()
while True:
    jugada_usuario(board)
    if check_winner(board, "X"):
        show_board()
        print("¡El jugador gana!")
        break
    if empate(board):
        show_board()
        print("¡Empate!")
        break

    laptop_move(board)
    if check_winner(board, "O"):
        show_board()
        print("¡El ordenador gana!")
        break
    if empate(board):
        show_board()
        print("¡Empate!")
        break
if __name__ == "__main__":
    play()