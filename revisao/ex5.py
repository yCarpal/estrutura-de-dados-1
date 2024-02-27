# Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da
# forma:
# A[i][j] = 2*i + 7*j se i < j;
# A[i][j] = 3*i^2 se i = j ;
# A[i][j] = 4*i^3 + 5*j^2 + 1 se i > j.



matriz = []

for i in range(10):
    linha = []
    for j in range(10):
        if i < j:
            elemento = (2 * i) + (7 * j)
        elif i == j:
            elemento = 3 * (i ** 2)
        else:
            elemento = (4 * (i ** 3)) + (5 * (j ** 2)) + 1
        linha.append(elemento)
    matriz.append(linha)


print("Matriz obtida:")
for linha in matriz:
    print("[", end=" ")
    for elemento in linha:
        print("{:4}".format(elemento), end=" ")
    print("]")