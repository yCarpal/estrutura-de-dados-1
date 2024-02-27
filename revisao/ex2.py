# Faça um programa que leia um vetor de 15 posições e o compacte, ou seja,
# elimine as posições com valor zero armazenado. Para isso, todos os elementos
# à frente do valor zero, devem ser movidos uma posição para trás no vetor. Ao
# final exiba o vetor resultante.


vetor = []            
print("Digite os elementos do vetor:")
for i in range(15):
    elemento = int(input(f"Digite o elemento {i+1}: "))
    vetor.append(elemento)

# Compactando o vetor
j = 0
for i in range(len(vetor)):
    if vetor[i] != 0:
        vetor[j] = vetor[i]
        j += 1

# Preencher as últimas posições com zeros
for i in range(j, len(vetor)):
    vetor[i] = 0

# Exibindo o vetor resultante
print("\nVetor resultante:")
print(vetor)


print("O exercicio pede para criarmos um vetor com 15 numeros e que caso o usuario informe o número 0 que ele seja movido a direita de todos os números informados")

print(""" Eu criei um vetor, após isso fiz um loop para o usuario informar 15 números, e após isso criei uma variavel igual a zero e um loop de 15 repetiçoes onde se 
as unidades do meu vetor for diferente de 0 ele ira trocar de lugar com a minha variavel 0, após isso fiz outro loop para pegar os elementos do meu vetor e verificar 
se ele for igual a 0 ele ira preencher as ultimas posições com zero, no final exibindo o vetor com todas as posições corretas.""")

        
        