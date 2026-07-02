tablero = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]

def mostrar_tablero():
    print("-" * 9)
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

mostrar_tablero()