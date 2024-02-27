# Faça um programa que leia um vetor de 15 posições e o compacte, ou seja,
# elimine as posições com valor zero armazenado. Para isso, todos os elementos
# à frente do valor zero, devem ser movidos uma posição para trás no vetor. Ao
# final exiba o vetor resultante.


vetor = []
for i in range(15):
    vetor[i] = float(input(f"Informe uma valor para [{i}]: "))


for i in range(15):
    vetor = int(input("Insira um valor para o vetor: "))
    if vetor[i] != 0:
        vetor.append(i)
print(vetor)