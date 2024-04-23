tam = 5
pilha = []
t = 0
b = 0
fila = []
tam_fila = 3
re = 0
frente = 0

def inserir_pilha():
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

def remover_pilha():
    global t, pilha
    if t > 0:
        elemento_removido = pilha.pop()
        t -= 1
        print(f"Elemento removido: {elemento_removido}")
    else:
        print("A pilha está vazia, não é possível remover elementos. Underflow!")
              


def inserir_fila(elemento): 
    global re, frente
 
    espaco = 0
    for i in range(tam_fila):
        if fila[i] == None:
            espaco = espaco +  1

        if espaco >= 2 and re == tam_fila:
            re = 0

    if re == tam_fila: 
            print(f'\nFila cheia, Overflow\n')


    elif re + 1 != frente:
        fila[re] = elemento
        re = re + 1
    
    print(f'\n{fila} Ré:{re} frente:{frente}\n') 

def remover_fila():
    global frente, re, espaco

    if frente == re and fila[frente] == None:
        print("UNDERFLOW, fila ja esta vazia!")
    else:
        fila[frente] = None
        frente = (frente + 1) % tam_fila
        espaco += 1

    print(fila)


def print_menu():
    print("\033[1;33m╔══════════════════════════════╗")
    print("║          Escolha pilha ou fila         ║")
    print("╠══════════════════════════════╣")
    print("║ 1. Inserir elementos na fila ║")
    print("║ 2. Inserir elementos na pilha  ║")
    print("║ 3. Remover Elem Pilha     ║")
    print("║ 4. Remover elem Fila    ║")
    print("║ 5. Sair                 ║")
    print("╚══════════════════════════════╝\033[0m")

while True:
    print_menu()
    choice = int(input("\033[1;36mEscolha uma opção: \033[0m"))

    if choice == 1:
        inserir_fila()
        print("Insira elementos para a fila")
    elif choice == 2:
        inserir_pilha()
        print("Insira elementos para a pilha")
    elif choice == 3:
        remover_pilha()
        print("O elemento foi removido")
    elif choice == 4:
        remover_fila("O elemento foi removido")
    elif choice == 5:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha outra opção.")
        
 

