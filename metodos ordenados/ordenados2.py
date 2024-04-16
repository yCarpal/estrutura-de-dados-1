def quick_sort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr

def merge_sort(arr):
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = arr[l:m + 1]
        R = arr[m + 1:r + 1]

        i = j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort_recursive(arr, l, r):
        if l < r:
            m = (l + r) // 2
            merge_sort_recursive(arr, l, m)
            merge_sort_recursive(arr, m + 1, r)
            merge(arr, l, m, r)

    merge_sort_recursive(arr, 0, len(arr) - 1)
    return arr

def explain_heap_sort():
    print("\n\033[1;34m[Heap Sort]\033[0m")
    print("Heap Sort é um algoritmo de ordenação que utiliza a estrutura de dados heap.")
    print("Ele constrói um heap máximo a partir do array e então repete a seguinte operação até que o heap contenha apenas um elemento:")
    print("Remove o maior elemento do heap (que sempre estará na raiz do heap) e reconstrói o heap.")
    print("Complexidade: O(n log n) no pior caso.\n")

def explain_quick_sort():
    print("\n\033[1;34m[Quick Sort]\033[0m")
    print("Quick Sort é um algoritmo de ordenação que utiliza a abordagem de dividir para conquistar.")
    print("Seleciona um elemento como pivô e particiona o array ao redor do pivô de tal forma que os elementos menores que o pivô fiquem antes dele e os elementos maiores fiquem depois.")
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
    print("║ 0. Sair                      ║")
    print("╚══════════════════════════════╝\033[0m")

arr = []

while True:
    print_menu()
    choice = int(input("\033[1;36mEscolha uma opção: \033[0m"))

    if choice == 1:
        n = int(input("\nDigite o tamanho da lista: "))
        arr = [int(input("Digite o elemento {}: ".format(i+1))) for i in range(n)]
    elif choice == 2:
        print("\nOrdenando usando Quick Sort...")
        print("Resultado:", quick_sort(arr.copy()))
    elif choice == 3:
        print("\nOrdenando usando Merge Sort...")
        print("Resultado:", merge_sort(arr.copy()))
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
#A