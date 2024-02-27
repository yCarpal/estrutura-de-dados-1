matriz = []


for i in range(2):
    linha = []
    for j in range(2):
        if i < j:
            elemento = 2 * i + 7 * j
        elif i == j:
            elemento = 3 * i ** 2
        else:
            elemento = 4 * i ** 3 + 5 * j ** 2 + 1
        linha.append(elemento)
    matriz.append(linha)


print("Matriz obtida:")
for linha in matriz:
    print("[", end=" ")
    for elemento in linha:
        print("{:4}".format(elemento), end=" ")
    print("]")