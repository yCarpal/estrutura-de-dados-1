# Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os
# demais elementos. Escreva ao final a matriz obtida.

matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(0)
    matriz.append(linha)


for i in range(5):
    matriz[i][i] = 1


print("Matriz obtida:")
for linha in matriz:
    print(linha)


print("""poderia substituir o primeiro passo por algo mais simples como apenas gerar uma matrix de 5x5 sendo assim:
for _ in range(5):
    linha = [0] * 5
    matriz.append(linha)
porém para minha interpretação ficaria melhor a identificação de linha e coluna da minha matriz assim formando-a certo""")