# Aluno: Wellington da Silva


class ListaException(Exception):

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
    def dado(self, novo_dado):
        self.__dado = novo_dado

    @prox.setter
    def prox(self, novo_prox):
        self.__prox = novo_prox

    def __str__(self):
        return str(self.__dado)


class ListaEncadeada:

    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def vazia(self):
        return True if self.__tamanho == 0 else False

#    def cheia(self):
#       pass

    def tamanho(self):
        return self.__tamanho

    def busca(self, dado):
        if self.vazia():
            raise ListaException('A lista está vazia')

        cursor = self.__head
        contador = 1

        while cursor is not None:
            if cursor.dado == dado:
                return contador
            else:
                cursor = cursor.prox
                contador += 1

        raise ListaException('O valor informado na busca não está na lista')

    def elemento(self, posicao):
        # Operação que recebe a posição de um elemento da lista e retorna o conteúdo (dado) que está armazenado.
        try:
            assert posicao > 0

            if self.vazia():
                raise ListaException('A lista está vazia')

            cursor = self.__head
            contador = 1

            while cursor is not None and contador < posicao:
                cursor = cursor.prox
                contador += 1

            if cursor is not None:
                return cursor.dado

            raise ListaException('A posição é inválida para a lista')

        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise

    def inserir(self, posicao, dado):
        # Operação que insere um dado na lista na posição indicada (posição válida)
        try:
            assert posicao > 0

            # Condição 1: Inserção de a lista estiver vazia

            if self.vazia():

                if posicao != 1:
                    raise ListaException('A lista está vazia, defina o argumento posição como 1')

                self.__head = Node(dado)
                self.__tamanho += 1
                return

            # Condição 2: Inserção na primeira posição em uma lista não vazia
            if posicao == 1:

                novo = Node(dado)
                novo.prox = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            # Condição 3: inserção após a primeira posição em uma lista não vazia.
            cursor = self.__head
            contador = 1

            while cursor is not None and contador < (posicao - 1):
                cursor = cursor.prox
                contador += 1

            if cursor is None:
                raise ListaException('A posição é inválida para inserção')

            novo = Node(dado)
            novo.prox = cursor.prox

            cursor.prox = novo
            self.__tamanho += 1
            return

        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')

        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise

    def remover(self, posicao):
        # Operação que remove um elemento da lista e retorna seu valor
        try:
            assert posicao > 0
            if self.vazia():
                raise ListaException('Lista vazia, não é possível remover elementos')

            cursor = self.__head
            contador = 1

            while cursor is not None and contador <= (posicao - 1):
                anterior = cursor
                cursor = cursor.prox
                contador += 1

            if cursor is None:
                raise ListaException('Posição inválida para remoção')

            dado = cursor.dado

            if posicao == 1:
                self.__head = cursor.prox
            else:
                anterior.prox = cursor.prox

            self.__tamanho -= 1
            return dado

        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise

    def imprimir(self):
        # Método que imprime o conteúdo da lista sequencial
        print(self.__str__())

    def print_auxiliar(self, node):

        if node is None:
            return

        self.print_auxiliar(node.prox)
        print(node.dado, ' ', end='')


    def imprimirInvertido(self):

        self.print_auxiliar(self.__head)


    def modificar(self, posicao, novo_dado):
        # Método que altera o conteúdo armazenado em uma determinada posição da lista
        try:
            assert posicao > 0
            if self.vazia():
                raise ListaException('Lista vazia, não é possível remover elementos')

            cursor = self.__head
            contador = 0

            while cursor is not None and contador < (posicao - 1):
                cursor = cursor.prox
                contador += 1

            if cursor is not None:
                cursor.dado = novo_dado

                return

            raise ListaException('Posição inválida para a lista')

        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')

        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise

    def __str__(self):
        str = 'Lista: ['
        cursor = self.__head
        while cursor is not None:
            str += f'{cursor.dado}'
            cursor = cursor.prox
            if cursor is not None:
                str += ', '
        str += ']'
        return str

    def insereInicio(self, dado):

        novo = Node(dado)
        novo.prox = self.__head
        self.__head = novo
        self.__tamanho += 1
        return

    def insereFim(self, dado):

        if self.vazia():
            self.__head = Node(dado)
            self.__tamanho += 1
            return

        cursor = self.__head
        contador = 1

        while cursor is not None and contador < self.__tamanho:
            cursor = cursor.prox
            contador += 1

        if cursor is None:
            raise ListaException('A posição é inválida para inserção')

        novo = Node(dado)

        cursor.prox = novo
        self.__tamanho += 1
        return

    def esvaziar(self):

        if self.vazia():
            raise ListaException('A lista já está vazia')

        self.__head = None
        self.__tamanho = 0
        return

    def removeInicio(self):

        # Caso a lista esteja vazia
        if self.vazia():
            raise ListaException('A lista está vazia, não há elemento para ser removido')

        # Caso a lista só tenha um elemento
        if self.__tamanho == 1:
            cursor = self.__head
            self.__head = None
            self.__tamanho = 0

            return cursor.dado

        cursor = self.__head

        novo_head = cursor.prox

        self.__head = novo_head

        self.__tamanho -= 1
        return cursor

    def removeFinal(self):

        # Verificando se a lista está vazia
        if self.vazia():
            raise ListaException('Lista vizia, não há dado para ser removido')

        # Quando a lista só possui um elemento
        if self.__tamanho == 1:
            cursor = self.__head
            self.__head = None
            self.__tamanho = 0

            return cursor.dado

        cursor = self.__head
        contador = 1

        while cursor is not None and contador <= (self.__tamanho - 1):
            anterior = cursor
            cursor = cursor.prox
            contador += 1

        if cursor is None:
            raise ListaException('Posição inválida para remoção')

        dado = cursor.dado

        anterior.prox = cursor.prox

        self.__tamanho -= 1
        return dado

    def removerOcorrencias(self, dado):

        if self.vazia():
            raise ListaException('A lista não possui dado para ser removido')

        cursor = self.__head
        contador = 1

        # caso só tenha um elemento na lista
        if self.__tamanho == 1 and cursor.dado == dado:
            self.__head = None
            self.__tamanho = 0
            return
        """
        while cursor is not None and contador <= (self.__tamanho):
            anterior = cursor
            if cursor.dado == dado:
                anterior.prox = cursor.prox
            cursor = cursor.prox
            contador += 1
        """

        for i in range(self.__tamanho):
            anterior = cursor
            cursor = cursor.prox
            if anterior.dado == dado:
                anterior = cursor.prox
                cursor = cursor.prox
                self.__tamanho -= 1

        raise ListaException('Não há nenhuma ocorrência na lista do dado informado')

    def concatena(self, lista1, lista2):

        for i in range(1, lista1.tamanho() + 1):
            self.insereFim(lista1.elemento(i))

        for j in range(1, lista2.tamanho() + 1):
            self.insereFim(lista2.elemento(j))
