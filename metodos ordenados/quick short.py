def passo():
    print("""Escolha um elemento pivô: O algoritmo seleciona um elemento da lista, chamado de pivô. A escolha do pivô pode afetar o desempenho do algoritmo, mas geralmente é escolhido o primeiro, o último ou um elemento aleatório.

Divisão: A lista é particionada em duas sub-listas: uma contendo elementos menores que o pivô e outra contendo elementos maiores que o pivô. Idealmente, os elementos iguais ao pivô são colocados em qualquer uma das sub-listas. Isso pode ser feito enquanto percorre a lista ou através de trocas.

Recursão: O Quicksort é aplicado recursivamente às duas sub-listas geradas anteriormente, isto é, a etapa de divisão e ordenação é repetida para cada sub-lista.

Combinação: Não é necessário fazer nada nesta etapa específica do algoritmo, pois as sub-listas já estão ordenadas. O Quicksort, portanto, não precisa de uma etapa explícita de combinação, ao contrário do Merge Sort, por exemplo.

Conquista: Quando a recursão atinge sub-listas de tamanho zero ou um (que estão automaticamente ordenadas), a recursão termina.

Concatenação: Como a ordenação é feita "in-place" (ou seja, sem alocar memória adicional), não é necessário fazer nenhuma concatenação explícita. A lista original é agora ordenada.""")


def partition(arr, low, high):
    """
    Função para particionar a lista e retornar o índice do pivô.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort(arr, low, high):
    """
    Função principal que implementa o algoritmo Quicksort.
    """
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Exemplo de uso:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n-1)
print("Lista ordenada:", arr)


def Traco(msg):
    print("-" * 40)
    print(msg)
    print("-" * 40)

while True:
    Traco("\nMenu:")
    Traco("1. O que é QuickSort?")
    Traco("2. Como é o Passo a Passo?")
    Traco("3. Exemplo de uso")
    Traco("4. Sair")

    opcao = int(input("Escolha uma das opções acima: "))

    if opcao == 1:  
        passo()

    elif opcao == 2:
        passo()

    elif opcao == 3:
        print("Lista ordenada:", arr)

    elif opcao == 4:
        break

    else:
        print("Opção desconhecida, Volte sempre")
