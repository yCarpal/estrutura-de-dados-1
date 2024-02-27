# Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o
# produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os
# dois conjuntos e o produto escalar, sendo que o produto escalar é dado por: x1
# ∗ y1 + x2 ∗ y2 + ... + xn ∗ yn.



tamanho_vetor = 5

Conjunto1= []
Conjunto2 = []

for i in range(tamanho_vetor):
    Conjunto1.append(int(input("Insira um número para o conjunto 1: ")))

for i in range(tamanho_vetor):
    Conjunto2.append(int(input("Insira um número para o conjunto 2: ")))
    

for i  in range(tamanho_vetor):
    soma = 0 
    multiplicação = Conjunto1[i] * Conjunto2[i]
    soma += multiplicação

print(f"Os conjuntos 1 : {Conjunto1} e o conjunto 2 {Conjunto2} tera seus multiplos somados {soma}")


print("\nEle quer que o usuario informe dois conjuntos de 5 numeros e que ocorra a multiplicação escalar dos dois conjuntos ")

print("""\nEu criei dois conjuntos vazios,pedi para o usuario informar números para os conjuntos e criei um ciclo do tamanho dos 
conjuntos e pedi para efetuar a multiplicação escalar que é a multiplicação de cada item do conjunto e somar os seus multiplos """)

print(""" \nNeste caso o método mais eficas a fazer é neste método pois ele economiza tempo e sua eficacia sempre será 100%, mas caso queira deixar com um menu bonito deve criar uma interface""")