import random

tablero = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]

def mostrar_tablero():
    print("-" * 9) #linea de separación
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

mostrar_tablero()

#posicionar ficha del jugador
# fila = int(input("Ingrese el número de fila (0-2): "))
# columna = int(input("Ingrese el número de columna (0-2): "))
# if tablero[fila][columna] == " ":
#     tablero[fila][columna] = "X" #casilla vacia pon x
# else: 
#     print("La posición ya está ocupada. Intente nuevamente.")
    
def ganador(tablero, jugador):
   # Comprobar filas
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True
    # Comprobar columnas
    for columna in range(3):
        if all(tablero[fila][columna] == jugador for fila in range(3)):
            return True
    # Comprobara diagonales
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False
def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True
while True:
    # Turno del jugador
    mostrar_tablero()
    fila = int(input("Ingrese el número de fila (0-2): "))
    columna = int(input("Ingrese el número de columna (0-2): "))
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = "X"
    else:
        print("La posición ya está ocupada. Intente nuevamente.")
        continue

    if ganador(tablero, "X"):
        mostrar_tablero()
        print("¡El ganador es el jugador!")
        break
    # Turno del ordenador
    while True:
        fila_laptop = random.randint(0, 2)
        columna_laptop = random.randint(0, 2)
        if tablero[fila_laptop][columna_laptop] == " ":
            tablero[fila_laptop][columna_laptop] = "O"
            break
    mostrar_tablero()

    if ganador(tablero, "O"):
        mostrar_tablero()
        print("¡El ganador es el ordenador!")
        break
    if tablero_lleno(tablero):
        mostrar_tablero()
        print("¡El juego es un empate!")
        break