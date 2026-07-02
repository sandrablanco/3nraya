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
fila = int(input("Ingrese el número de fila (0-2): "))
columna = int(input("Ingrese el número de columna (0-2): "))
if tablero[fila][columna] == " ":
    tablero[fila][columna] = "X" #casilla vacia pon x
else: 
    print("La posición ya está ocupada. Intente nuevamente.")

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
    # Turno del ordenador
    while True:
        fila_laptop = random.randint(0, 2)
        columna_laptop = random.randint(0, 2)
        if tablero[fila_laptop][columna_laptop] == " ":
            tablero[fila_laptop][columna_laptop] = "O"
            break

 