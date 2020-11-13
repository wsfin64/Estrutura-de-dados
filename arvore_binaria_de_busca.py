class BinarySearchTree:

    def __init__(self):
        self.__root = None

    def search(self, chave):
        if self.__root is not None:
            return self.__search_data(chave, self.__root)
        else:
            return None

    def __search_data(self, chave, node):
        if chave == node.dado:
            return node
        elif chave < node.dado and node.esq is not None:
            return self.__search_data(chave, node.esq)
        elif chave > node.dado and node.dir is not None:
            return self.__search_data(chave, node.dir)
        else:
            return None
