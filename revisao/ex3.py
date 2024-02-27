# Faça um programa para ler 10 números DIFERENTES a serem armazenados
# em um vetor. Os dados deverão ser armazenados no vetor na ordem que
# forem sendo lidos, sendo que caso o usuário digite um número que já foi
# digitado anteriormente, o programa deverá pedir para ele digitar outro número.
# Note que cada valor digitado pelo usuário deve ser pesquisado no vetor,
# verificando se ele existe entre os números que já foram fornecidos. Exibir na
# tela o vetor final que foi digitado.

lista = []

for i in range(10):
    while True:
        num = int(input(f"Insira o {i+1}º número da lista: "))

        if num not in lista:
            lista.append(num)
            break
        else:
            print("Digite outro número, pois ja foi digitado")

print(f"O números do vetor são : {lista}")

""

