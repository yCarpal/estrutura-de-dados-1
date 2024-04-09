class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def remover(self, dado):
        atual = self.cabeca
        if atual is None:
            print("A lista está vazia")
            return
        if atual.dado == dado:
            self.cabeca = atual.proximo
            return
        while atual.proximo:
            if atual.proximo.dado == dado:
                atual.proximo = atual.proximo.proximo
                return
            atual = atual.proximo
        print("O elemento não está na lista")

    def buscar(self, dado):
        atual = self.cabeca
        while atual:
            if atual.dado == dado:
                print("Elemento encontrado na lista")
                return
            atual = atual.proximo
        print("Elemento não encontrado na lista")

    def falso_overflow(self):
        # Esta função simula um falso overflow
        print("Simulação de falso overflow!")
        self.cabeca = None

    def mostrar(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")


# Exemplo de interação com o terminal
if __name__ == "__main__":
    lista_encadeada = ListaEncadeada()
    while True:
        print("\n1. Inserir elemento")
        print("2. Remover elemento")
        print("3. Buscar elemento")
        print("4. Simular falso overflow")
        print("5. Exibir lista")
        print("6. Sair")
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            dado = int(input("Digite o elemento a ser inserido: "))
            lista_encadeada.inserir(dado)
        elif escolha == 2:
            dado = int(input("Digite o elemento a ser removido: "))
            lista_encadeada.remover(dado)
        elif escolha == 3:
            dado = int(input("Digite o elemento a ser buscado: "))
            lista_encadeada.buscar(dado)
        elif escolha == 4:
            lista_encadeada.falso_overflow()
        elif escolha == 5:
            lista_encadeada.mostrar()
        elif escolha == 6:
            break
        else:
            print("Opção inválida. Tente novamente.")