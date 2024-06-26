def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def selection_sort(lista):
    n = len(lista)
    for step in range(n):
        indice = step
        for j in range(step + 1, n):
            if lista[j] < lista[indice]:
                indice = j
        lista[step], lista[indice] = lista[indice], lista[step]

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

def print_menu():
    print("\033[1;33m╔══════════════════════════════╗")
    print("║          ARCADE SORT          ║")
    print("╠══════════════════════════════╣")
    print("║ 1. Criar lista                ║")
    print("║ 2. Ordenar usando Bubble Sort ║")
    print("║ 3. Ordenar usando Selection   ║")
    print("║    Sort                       ║")
    print("║ 4. Ordenar usando Insertion   ║")
    print("║    Sort                       ║")
    print("║ 5. Explicar Bubble Sort       ║")
    print("║ 6. Explicar Selection Sort    ║")
    print("║ 7. Explicar Insertion Sort    ║")
    print("║ 8. Sair                       ║")
    print("╚══════════════════════════════╝\033[0m")

def explain_bubble_sort():
    print("\n\033[1;34m[Bubble Sort]\033[0m")
    print("Bubble Sort é um algoritmo de ordenação simples que funciona iterando sobre a lista múltiplas vezes.")
    print("Em cada iteração, compara-se cada par de elementos adjacentes e os troca se estiverem na ordem errada.")
    print("Este processo é repetido até que a lista esteja ordenada.\n")

def explain_selection_sort():
    print("\n\033[1;34m[Selection Sort]\033[0m")
    print("Selection Sort é um algoritmo de ordenação que divide a lista em duas partes: a parte ordenada e a parte não ordenada.")
    print("Em cada iteração, encontra-se o menor elemento da parte não ordenada e o coloca na posição correta na parte ordenada.")
    print("Este processo é repetido até que a lista esteja completamente ordenada.\n")

def explain_insertion_sort():
    print("\n\033[1;34m[Insertion Sort]\033[0m")
    print("Insertion Sort é um algoritmo de ordenação que constrói a lista ordenada um elemento de cada vez, movendo elementos não ordenados para a parte ordenada.")
    print("Em cada iteração, um elemento é removido da parte não ordenada e inserido na posição correta na parte ordenada.")
    print("Este processo é repetido até que não haja mais elementos na parte não ordenada.\n")

lista = []
while True:
    print_menu()
    choice = int(input("\033[1;36mEscolha uma opção: \033[0m"))

    if choice == 1:
        n = int(input("\nDigite o tamanho da lista: "))
        lista = [int(input("Digite o elemento {}: ".format(i + 1))) for i in range(n)]
        print("Lista criada:", lista)
    elif choice == 2:
        bubble_sort(lista)
        print("\nLista ordenada usando Bubble Sort:", lista)
    elif choice == 3:
        selection_sort(lista)
        print("\nLista ordenada usando Selection Sort:", lista)
    elif choice == 4:
        insertion_sort(lista)
        print("\nLista ordenada usando Insertion Sort:", lista)
    elif choice == 5:
        explain_bubble_sort()
    elif choice == 6:
        explain_selection_sort()
    elif choice == 7:
        explain_insertion_sort()
    elif choice == 8:
        print("\n\033[1;31mSaindo...\033[0m")
        break
    else:
        print("\033[1;31mOpção inválida. Por favor, escolha uma opção válida.\033[0m")