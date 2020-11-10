from arvore_binaria_exception import ArvoreBinariaException


class Node:

    def __init__(self, dado=None):
        self.__dado = dado
        self.__esq = None
        self.__dir = None
        
    # ------------------------------------------- DADO ------------------------------------------ #

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, novo_dado):
        self.__dado = novo_dado

    # ----------------------------------------- ESQUERDA ---------------------------------------- #

    @property
    def esq(self):
        return self.__esq

    @esq.setter
    def esq(self, nova_esq):
        if self.__esq is not None:
            raise ArvoreBinariaException('Nó esquerdo já existe')
        self.__esq = nova_esq

    # ----------------------------------------- DIREITA ----------------------------------------- #

    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, nova_dir):
        if self.__dir is not None:
            raise ArvoreBinariaException('Nó direito já existe')
        self.__dir = nova_dir
