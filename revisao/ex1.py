tamanho_vetor = int(input("Insira o tamnho do vetor: "))

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