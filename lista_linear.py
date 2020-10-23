class ListaLinear:

    def __init__(self):
        self.__dado = []

    def tamanho(self):
        return len(self.__dado)

    def eh_vazia(self):
        return True if len(self.__dado) == 0 else False

    def inserir(self, posicao, elemento):
        try:
            assert 0 < posicao <= len(self.__dado) + 1
            self.__dado.insert(posicao - 1, elemento)
        except AssertionError:
            print(f'Posicao invalida!, informe um valor entre 1 e {len(self.__dado) + 1}')

    def mostrar_elemento(self, posicao):
        try:
            print(self.__dado[posicao - 1])
        except IndexError:
            print('Não há elementos nesta posição')

    def __str__(self):
        return self.__dado.__str__()


lst = ListaLinear()
lst.inserir(1, 'oi')
lst.inserir(1, 'ola')
# lst.mostrar_elemento(2)
lst.inserir(7, 'ws')
print(lst)
# lst.mostrar_elemento(-5)
