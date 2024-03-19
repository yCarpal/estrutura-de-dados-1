tam = 5
pilha = []
t = 0
b = 0

def Traco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

def criar_pilha():
    global tam
    tam = int(input("Digite o tamanho máximo da pilha: "))
    b = int(input("Digite o valor da base da pilha : "))

def inserir():
    global t, pilha, b
    if t < tam:
        elemento = input("Insira um elemento para a pilha: ")
        pilha.append(elemento)
        t += 1
        print("Elemento inserido com sucesso!")
        print(f"Pilha atual: {pilha}")
        for item in pilha[::-1]: 
            print(f"{item}")
    else:
        print("Elemento não pode ser inserido, Overflow.")

def remover():
    global t, pilha
    if t > 0:
        elemento_removido = pilha.pop()
        t -= 1
        print(f"Elemento removido: {elemento_removido}")
    else:
        print("A pilha está vazia, não é possível remover elementos. Underflow!")

def consultar_elemento():
    global t, pilha
    if t > 0:
        for item in pilha[::-1]:  
            print(f"{item}")
        indice = int(input("Digite o índice do elemento que deseja consultar: "))
        if 0 <= indice < t:
            print(f"O elemento na posição {indice}, da pilha é: {pilha[indice]}")
        else:
            print("Índice inválido. Por favor, insira um índice válido dentro da faixa da pilha.")
    else:
        print("A pilha está vazia, não há elementos para consultar.")

def menu():
    Traco("\nMenu:")
    Traco("1. Criar pilha")
    Traco("2. Inserir elemento")
    Traco("3. Remover elemento")
    Traco("4. Consultar elemento")
    Traco("5. Sair")

opcao = None
while opcao != 5:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        criar_pilha()
    elif opcao == 2:
        inserir()
    elif opcao == 3:
        remover()
    elif opcao == 4:
        consultar_elemento()
    elif opcao == 5:
        print("Encerrando o programa...")
    else:
        print("Opção inválida. Por favor, escolha outra opção.")



inserir(pilha)
print(f"Pilha após a inserção: {pilha}")  

remover(pilha)
print(f"Pilha após a remoção: {pilha}")

indice = int(input("Digite o índice do elemento que deseja consultar: "))
consultar_elemento(pilha, indice)