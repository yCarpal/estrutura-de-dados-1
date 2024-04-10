def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def print_merge_sort_description():
    description = "Merge Sort é um algoritmo de ordenação eficiente que segue o paradigma de Divisão e Conquista. " \
                  "Ele divide o array em sub-arrays menores, ordena esses sub-arrays e depois os mescla " \
                  "para produzir um array ordenado. O Merge Sort tem uma complexidade de tempo garantida de " \
                  "O(n log n) em todos os casos."
    return description

def print_merge_sort_step_by_step():
    steps = "Passo a passo do Merge Sort:\n" \
            "1. Divisão: Divide o array original ao meio recursivamente até que cada sub-array contenha apenas um elemento.\n" \
            "2. Conquista: Ordena recursivamente as metades esquerda e direita de cada sub-array.\n" \
            "3. Combinação: Combina os sub-arrays ordenados em um único array ordenado."
    return steps

def merge_sort_array(arr):
    print(print_merge_sort_description())
    print(print_merge_sort_step_by_step())
    
    sorted_array = merge_sort(arr)
    print("Array ordenado é:", sorted_array)

def run_merge_sort_menu():
    while True:
        print("\n===== MENU =====")
        print("1. O que é o Merge Sort?")
        print("2. Passo a passo do Merge Sort")
        print("3. Ordenar um array usando Merge Sort")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            print(print_merge_sort_description())
        elif choice == "2":
            print(print_merge_sort_step_by_step())
        elif choice == "3":
            arr = input("Digite o array separado por espaço: ").split()
            arr = [int(x) for x in arr]  # Convertendo para inteiros
            merge_sort_array(arr)
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

run_merge_sort_menu()
