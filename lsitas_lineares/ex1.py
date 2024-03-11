def criar_lista():
 
    num_elementos = int(input("Quantos números você deseja adicionar à lista? "))
    lista = []
    for i in range(num_elementos):
        numero = int(input("Insira o número: "))
        lista.append(numero)
    return lista

def remover_elemento(lista):
   
    elemento = int(input("Insira o elemento que deseja remover: "))
  
    if elemento in lista:
        resposta = input(f"Tem certeza que deseja remover o elemento {elemento}? (s/n): ").lower()
        if resposta == 's':
            lista.remove(elemento)
            print("Elemento removido com sucesso.")
            print("Lista atualizada:", lista)
        elif resposta == 'n':
            print("Elemento não removido.")
        else:
            print("Resposta inválida.")
    else:
        print("Elemento não encontrado na lista.")

def consultar_elemento(lista):
 
    elemento = int(input("Insira o elemento que deseja consultar: "))
    # Verificando se o elemento está na lista
    if elemento in lista:
        print(f"O elemento {elemento} está na lista.")
    else:
        print(f"O elemento {elemento} não está na lista.")

def tamanho_lista(lista):
   
    tamanho = len(lista)
    print(f"O tamanho da lista é {tamanho}.")

def inserir_elemento(lista):
 
    elemento = int(input("Insira o elemento que deseja inserir: "))
    posicao = int(input("Insira a posição onde deseja inserir o elemento: "))
   
    lista.insert(posicao, elemento)
    print(f"Elemento {elemento} inserido na posição {posicao}.")
    print("Lista atualizada:", lista)


def exibir_menu():
    print("\nMenu:")
    Traco("1. Criar lista")
    Traco("2. Remover elemento")
    Traco("3. Consultar elemento")
    Traco("4. Determinar tamanho da lista")
    Traco("5. Inserir elemento em posição específica")
    Traco("0. Sair")


def Traco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


lista = []
opcao = None

while opcao != 0:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        lista = criar_lista()
        print("Lista atualizada:", lista)
    elif opcao == 2:
        if lista:
            remover_elemento(lista)
            print("Lista atualizada:", lista)
        else:
            print("Lista vazia. Crie uma lista primeiro.")
    elif opcao == 3:
        if lista:
            consultar_elemento(lista)
        else:
            print("Lista vazia. Crie uma lista primeiro.")
    elif opcao == 4:
        if lista:
            tamanho_lista(lista)
        else:
            print("Lista vazia. Crie uma lista primeiro.")
    elif opcao == 5:
        if lista:
            inserir_elemento(lista)
            print("Lista atualizada:", lista)
        else:
            print("Lista vazia. Crie uma lista primeiro.")
    elif opcao == 0:
        print("Encerrando o programa...")
    else:
        print("Opção inválida. Tente novamente.")



        # ###Os arrays em Python têm melhor desempenho do que as listas devido à sua representação contígua na memória, armazenando um único tipo de dado, 
        # o que reduz o custo de operações extras, e sua capacidade de aproveitar 
        # otimizações específicas para operações massivas, como as oferecidas pela biblioteca NumPy.