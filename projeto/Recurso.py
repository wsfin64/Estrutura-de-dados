class Recurso:

    def __init__(self, tamanho, nome):
        self.__tamanho = float(tamanho)
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @property
    def tamanho(self):
        return float(self.__tamanho)

    def __str__(self):
        return f'{self.__nome} - {self.__tamanho}KB'
