def quick_sort(lista):
    def partition(lista, low, high):
        pivot = lista[high]
        i = low - 1
        for j in range(low, high):
            if lista[j] < pivot:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[high] = lista[high], lista[i + 1]
        return i + 1

    def quick_sort_recursive(lista, low, high):
        if low < high:
            pi = partition(lista, low, high)
            quick_sort_recursive(lista, low, pi - 1)
            quick_sort_recursive(lista, pi + 1, high)

    quick_sort_recursive(lista, 0, len(lista) - 1)
    return lista

def merge_sort(lista):
    def merge(lista, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = lista[l:m + 1]
        R = lista[m + 1:r + 1]

        i = j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            lista[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            lista[k] = R[j]
            j += 1
            k += 1

    def merge_sort_recursive(lista, l, r):
        if l < r:
            m = (l + r) // 2
            merge_sort_recursive(lista, l, m)
            merge_sort_recursive(lista, m + 1, r)
            merge(lista, l, m, r)

    merge_sort_recursive(lista, 0, len(lista) - 1)
    return lista

def explain_heap_sort():
    print("\n\033[1;34m[Heap Sort]\033[0m")
    print("Heap Sort é um algoritmo de ordenação que utiliza a estrutura de dados heap.")
    print("Ele constrói um heap máximo a partir da lista e então repete a seguinte operação até que o heap contenha apenas um elemento:")
    print("Remove o maior elemento do heap (que sempre estará na raiz do heap) e reconstrói o heap.")
    print("Complexidade: O(n log n) no pior caso.\n")

def explain_quick_sort():
    print("\n\033[1;34m[Quick Sort]\033[0m")
    print("Quick Sort é um algoritmo de ordenação que utiliza a abordagem de dividir para conquistar.")
    print("Seleciona um elemento como pivô e particiona a lista ao redor do pivô de tal forma que os elementos menores que o pivô fiquem antes dele e os elementos maiores fiquem depois.")
    print("Complexidade: O(n log n) no caso médio e O(n^2) no pior caso.\n")

def explain_merge_sort():
    print("\n\033[1;34m[Merge Sort]\033[0m")
    print("Merge Sort é um algoritmo de ordenação que utiliza a abordagem de dividir para conquistar.")
    print("Divide a lista em duas metades, ordena cada metade recursivamente e depois mescla as duas metades ordenadas.")
    print("Complexidade: O(n log n) em todos os casos.\n")

def print_menu():
    print("\033[1;33m╔══════════════════════════════╗")
    print("║          ARCADE SORT          ║")
    print("╠══════════════════════════════╣")
    print("║ 1. Criar lista               ║")
    print("║ 2. Ordenar usando Quick Sort ║")
    print("║ 3. Ordenar usando Merge Sort ║")
    print("║ 4. Explicar Heap Sort       ║")
    print("║ 5. Explicar Quick Sort      ║")
    print("║ 6. Explicar Merge Sort      ║")
    print("║ 7. Sair                      ║")
    print("╚══════════════════════════════╝\033[0m")

lista = []

while True:
    print_menu()
    choice = int(input("\033[1;36mEscolha uma opção: \033[0m"))

    if choice == 1:
        n = int(input("\nDigite o tamanho da lista: "))
        lista = [int(input("Digite o elemento {}: ".format(i + 1))) for i in range(n)]
        print("Lista criada:", lista)
    elif choice == 2:
        print("\nOrdenando usando Quick Sort...")
        print("Resultado:", quick_sort(lista.copy()))
    elif choice == 3:
        print("\nOrdenando usando Merge Sort...")
        print("Resultado:", merge_sort(lista.copy()))
    elif choice == 4:
        explain_heap_sort()
    elif choice == 5:
        explain_quick_sort()
    elif choice == 6:
        explain_merge_sort()
    elif choice == 7:
        print("\n\033[1;31mSaindo...\033[0m")
        break
    else:
        print("\033[1;31mOpção inválida. Por favor, escolha uma opção válida.\033[0m")
