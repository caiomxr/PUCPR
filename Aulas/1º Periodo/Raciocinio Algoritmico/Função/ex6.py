matriz = [
    [9, 1, 8],
    [2, 9, 2],
    [6, 2, 9]
]


def imprime_diagonal(matriz):
    for i in range(len(matriz)):
        print(matriz[i][i])


imprime_diagonal(matriz)
