class PilhaException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class Node:

    def __init__(self, dado):
        self.__dado = dado
        self.__prox = None

    @property
    def dado(self):
        return self.__dado

    @property
    def prox(self):
        return self.__prox

    @dado.setter
    def dado(self, novoDado):
        self.__dado = novoDado

    @prox.setter
    def prox(self, novoProx):
        self.__prox = novoProx


class PilhaEncadeada:

    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def vazia(self):
        return True if self.__tamanho == 0 else False

    def tamanho(self):
        return self.__tamanho

    def topo(self):

        if self.vazia():
            raise PilhaException('A pilha está vazia!')

        topo = self.__topo
        return topo.dado

    def empilhar(self, dado):
        # Insere elementos sempre a primeira posição(topo)

        if self.vazia():

            # Inserção do primeiro elemento na pilha
            novo = Node(dado)
            self.__topo = novo

            self.__tamanho += 1
            return

        novo = Node(dado)
        topo = self.__topo
        novo.prox = topo
        self.__topo = novo

        self.__tamanho += 1
        return

    def desempilhar(self):
        # Remoção do topo

        if self.vazia():
            raise PilhaException('A pilha está vazia, não há elementos para remover')

        topo = self.__topo
        dado = topo.dado

        self.__topo = topo.prox

        self.__tamanho -= 1
        return dado

    def imprimir(self):
        return self.__str__()

    def esvaziar(self):
        self.__topo = None
        self.__tamanho = 0

    def base(self):
        # Mostrando o último elemento da pilha, ou seja, a sua base

        if self.vazia():
            raise PilhaException('A pilha está vazia')

        cursor = self.__topo

        while cursor.prox is not None:
            cursor = cursor.prox

        ultimo = cursor
        return ultimo.dado

    def __str__(self):
        string = '['
        cursor = self.__topo
        for i in range(self.__tamanho):
            string += f'{cursor.dado}'
            cursor = cursor.prox
            if cursor is not None:
                string += ', '
        string += ']'
        return string
