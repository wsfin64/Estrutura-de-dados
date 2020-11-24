class BandaInternet:

    def __init__(self, largura):
        self.__largura = largura

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, nova_largura):
        self.__largura = nova_largura
