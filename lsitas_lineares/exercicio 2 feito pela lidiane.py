# Estrutura de dado em forma de Pilha.
stack =  []
TAM = 5


#Insere um novo elemento na pilha de dados.
def NovoElemento():
    x = int(input("Digite um elemento para a pilha:  "))
    if len(stack) < TAM:
        stack.append(x)
        print("Elemento incluido com sucesso!")
    else:
        print("Elemento não poderá ser inserido! Overflow!")

#Apaga um elemento na pilha de dados.
def ApagaElemento():
    del stack[( len (stack) - 1)]
    print("Elemento excluido com sucesso!")

#Consulta se um elemento está na pilha.
def ConsultaElemento(a:int):
    x = len(stack)-1 
    while(x >= 0):
        if(stack[x] == a):
           return x
        x = x - 1
    return x
    
    
while True:
    Opcao = 0
    print (" 0 - SAIR\n 1 - Novo \n 2 - Exibe os elemento da pilha \n 3 - Remove elemento da pilha\n 4 - Encontra elemento na pilha\n")
    Opcao = (input("Escolha uma Opção:  "))

    if Opcao == "0":
        break
    elif Opcao == "1": 
        NovoElemento()
    elif Opcao == "2": 
        print (stack)
        print()
    elif Opcao == "3":
        if len(stack) == 0:
             print ("Underflow.... Pilha Vazia\n")
        else:
            print (f"O elemento que será apagado da pilha é o elemento {stack [len(stack) -1]}")
            ApagaElemento()
            print()
            print (stack)
            print()
    elif Opcao == "4":
        procura = int(input("Informe o elemento que deseja verificar se está na pilha:  "))
        x = ConsultaElemento(procura)
        if x >= 0:
            print(f"Elemento {procura} encontrado na posiçâo: {x}")
        else:
            print(f"Elemento {procura} não encontrado")

    else:
        print("Esta não é uma opção válida")
        print()