matriz = []


print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(elemento)
    matriz.append(linha)


soma_colunas = []
for j in range(3):
    soma = 0
    for i in range(3):
        soma += matriz[i][j]
    soma_colunas.append(soma)


print("\nArray unidimensional pela soma dos números de cada coluna:")
print(soma_colunas)