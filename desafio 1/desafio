tam_array = 5
array = [None] * tam_array
re = 0
frente = 0
espaco = tam_array


def inserir(elemento): 
    global re, frente
 
    espaco = 0
    for i in range(tam_array):
        if array[i] == None:
            espaco = espaco +  1

        if espaco >= 2 and re == tam_array:
            re = 0

    if re + 1 == frente or (re == tam_array and espaco == 1): 
        print(f'\n--> Falso Overflow! <--\n') 

    elif re == tam_array: 
            print(f'\nFila cheia, Overflow\n')


    elif re + 1 != frente:
        array[re] = elemento
        re = re + 1
    
    print(f'\n{array} Ré:{re} frente:{frente}\n') 

def remover():
    global frente, re, espaco

    if frente == re and array[frente] == None:
        print("UNDERFLOW, fila ja esta vazia!")
    else:
        array[frente] = None
        frente = (frente + 1) % tam_array
        espaco += 1

    print(array)

def consultar_elemento(elemento):
    global frente, re, tam_array

    encontrado = False
    i = frente
    while i != re:
        if array[i] == elemento:
            print(f"Elemento {elemento} encontrado na posição {i}")
            encontrado = True
            break
        i = (i + 1) % tam_array

    if not encontrado:
        print(f"Elemento {elemento} não encontrado na fila")

def Traco(msg):
    print("-" * 40)
    print(msg)
    print("-" * 40)

while True:
    Traco("\nMenu:")
    Traco("1. Inserir elemento")
    Traco("2. Remover elemento")
    Traco("3. Exibir elementos")
    Traco("4. Procurar elemento")
    Traco("5. Sair")

    opcao = int(input("Escolha uma das opções acima: "))

    if opcao == 1:  
        elemento = int(input("Digite o elemento que quer adicionar: "))
        inserir(elemento)
       

    elif opcao == 2:
        remover()

    elif opcao == 3:
        print(array)

    elif opcao == 4:
        procura = int(input("Digite o elemento que você quer procurar na Fila: "))
        consultar_elemento(procura)

    elif opcao == 5:
        break

    else:
        print("Opção desconhecida, tente novamente!")
