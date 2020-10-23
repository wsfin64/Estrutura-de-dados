class FilaException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class FilaSequencial:

    def __init__(self):
        self.__dado = []
        self.__noCabeca = None

    def vazia(self):
        return True if len(self.__dado) == 0 else False

    def tamanho(self):
        return len(self.__dado)

    def inicio(self):
        if self.vazia():
            raise FilaException('A fila está vazia!')

        return self.__dado[0]

    def inserir(self, dado):

        self.__dado.append(dado)
        return

    def remover(self):

        if self.vazia():
            raise FilaException('A fila está vazia, não há elementos para ser removido!')

        dado = self.__dado[-1]
        self.__dado.pop(0)
        return dado

    def __str__(self):
        return self.__dado.__str__()

    def imprimir(self):
        print(self.__str__())


if __name__ == '__main__':

    f = FilaSequencial()

    try:

        f.remover()
        print(f)
    except FilaException as err:
        print(err)
    print(f)