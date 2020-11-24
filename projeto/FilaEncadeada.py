class FilaException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class Node:

    def __init__(self, dado):
        self.__dado = dado
        self.__prox = None

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, novo_dado):
        self.__dado = novo_dado

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, novo_prox):
        self.__prox = novo_prox

    def __str__(self):
        return self.__dado.__str__()


class NoCabeca:

    def __init__(self):
        self.__tamanho = 0
        self.__inicio = None
        self.__fim = None

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, novo_tamanho):
        self.__tamanho = novo_tamanho

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, novo_inicio):
        self.__inicio = novo_inicio

    @property
    def fim(self):
        return self.__fim

    @fim.setter
    def fim(self, novo_fim):
        self.__fim = novo_fim

    def __str__(self):
        return f'Nó cabeça --> |{self.inicio} | Tamanho da fila: {self.__tamanho} | {self.fim}|'


class FilaEncadeada:

    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__head = NoCabeca()  # Instância do nó cabeça com todos as propriedade igual a None

    def vazia(self):
        return True if self.tamanho() == 0 else False

    def tamanho(self):
        return self.__head.tamanho

    def enfileirar(self, dado):
        # Ao inserir elementos, será necessário alterar os pornteiros de inicio e fim do nó cabeça!

        if self.vazia():
            novo = Node(dado)
            self.__inicio = novo
            self.__head.inicio = self.__inicio
            self.__head.fim = novo
            #self.__tamanho += 1
            self.__head.tamanho += 1
            return

        novo = Node(dado)
        fim = self.__head.fim
        fim.prox = novo
        self.__fim = novo
        self.__head.fim = self.__fim
        #self.__tamanho += 1
        self.__head.tamanho += 1

    def desenfileirar(self):
        # Ao remover elementos, será necessário reorganizar o ponteiro inicial do nó cabeça

        if self.vazia():
            raise FilaException('A fila está vazia!')

        if self.tamanho() == 1:
            self.__inicio = None
            self.__fim = None
            #self.__tamanho = 0
            self.__head.inicio = self.__inicio
            self.__head.fim = self.__fim
            self.__head.tamanho = 0
            return

        dado_removido = self.__inicio.dado
        inicio = self.__inicio.prox
        self.__inicio = inicio
        #self.__tamanho -= 1
        self.__head.inicio = self.__inicio
        self.__head.tamanho -= 1
        return dado_removido

    def __str__(self):
        string = '['
        cursor = self.__inicio
        for i in range(self.__head.tamanho):
            string += f'{cursor.dado}'
            cursor = cursor.prox
            if cursor is not None:
                string += ', '
        string += ']'
        return string

    def mostrar_cabeca(self):
        return self.__head.__str__()
