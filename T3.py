
laberinto = [
    [1, 1, 1, 1, 99, 1, 1, 1, 0],   # 0 = inicio (verde)
    [1, 99, 1, 99, 1, 99, 1, 99, 1],
    [1, 1, 1, 99, 1, 1, 99, 1, 99],
    [99, 1, 99, 99, 1, 99, 99, 99, 1],
    [1, 1, 99, -1, 1, 1, 3, 99, 1],
    [-2, 99, 1, 99, 1, 99, 1, 1, 1],
    [1, 99, 1, -1, 1, 1, 1, 99, 1],
    [1, 99, 99, 99, 1, 2, 99, 1, 1],
    [0, 1, 3, 1, 1, 99, 1, 1, 1]    # 0 = final (rojo)
]

inicio = (0, 8)
fin = (8, 0)

camino = [['-' for _ in range(9)] for _ in range(9)]

# Backtracking
def backtrack(x, y, energia):
    # Si llegamos al final
    if (x, y) == fin:
        camino[x][y] = 'F'
        return True

    if (x, y) != inicio:
        camino[x][y] = 'X'

    # Energía
    if (x, y) not in [inicio, fin]:
        energia += laberinto[x][y]

        # si energía se vuelve inválida, retrocede
        if energia < 0 or energia > 18:
            if (x, y) != inicio:
                camino[x][y] = '-'
            return False

    # movimientos: izquierda, abajo, arriba, derecha
    for dx, dy in [(0,-1),(1,0),(-1,0),(0,1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 9 and 0 <= ny < 9:
            if laberinto[nx][ny] != 99 and camino[nx][ny] == '-':
                if backtrack(nx, ny, energia):
                    return True

    # desmarcar si no funcionó
    if (x, y) != inicio:
        camino[x][y] = '-'
    return False



print("\nLABERINTO ORIGINAL:\n")
for fila in laberinto:
    print(fila)

exito = backtrack(inicio[0], inicio[1], energia=18)

# marcar inicio
camino[inicio[0]][inicio[1]] = 'I'

print("\nRESULTADO:\n")
if exito:
    print(" Camino encontrado")
else:
    print(" No hay camino posible")

print("\nMATRIZ DE CAMINO:\n")
for fila in camino:
    print(fila)
