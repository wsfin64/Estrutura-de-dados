class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ListaSequancial:

    def __init__(self):
        self.__dados = []

    def vazia(self):
        return len(self.__dados) == 0

#    def cheia(self):
#       pass

    def tamanho(self):
        return len(self.__dados)

    def busca(self, dado):
        # Operação que recebe um dado da lista e retorna a  sua posição (índice)
        """
        for i in range(len(self.__dados)):
            if self.__dados[i] == dado:
                return f'O elemento {dado} encontra-se na posição {i + 1}'
        """
        try:
            return self.__dados.index(dado) + 1
        except ValueError:
            raise ListaException(f'O valor {dado} não se encontra na lista')
        except:
            raise

    def elemento(self, posicao):
        # Operação que recebe a posição de um elemento da lista e retorna o conteúdo (dado) que está armazenado.
        try:
            assert posicao > 0
            return self.__dados[posicao - 1]
        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except IndexError:
            raise ListaException('A posição informada é inválida')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise

    def inserir(self, posicao, dado):
        # Operação que insere um dado na lista na posição indicada (posição válida)
        try:
            assert posicao > 0
            self.__dados.insert(posicao - 1, dado)
        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except IndexError:
            raise ListaException('A posição informada é inválida')
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
            else:
                valor = self.__dados[posicao - 1]
                del self.__dados[posicao - 1]
                return valor
        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except IndexError:
            raise ListaException('A posição informada é inválida')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise

    def imprimir(self):
        # Método que imprime o conteúdo da lista sequencial
        print(self.__str__())

    def modificar(self, posicao, novo_dado):
        # Método que altera o conteúdo armazenado em uma determinada posição da lista
        try:
            assert posicao > 0
            if self.vazia():
                raise ListaException('Lista vazia, não é possível remover elementos')
            self.__dados[posicao - 1] = novo_dado
            return True
        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except IndexError:
            raise ListaException('A posição informada é inválida')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise

    def __str__(self):
        return f'{self.__dados}'


l1 = ListaSequancial()

if l1.vazia():
    print('Lista está vazia')

print('Tamanho: ', l1.tamanho())


for i in range(10):
    l1.inserir(1, i * 10)

print(l1)

print(l1.remover(8))
print(l1)

print('-------------------------------')
l1.imprimir()
l1.modificar(5, 'Wellington')
l1.imprimir()

try:
    # print(l1.elemento(5))
    # l1.inserir(5, 'oi')
    # l1.remover(1)
    l1.modificar(-100, 999)
    print(l1)
except ListaException as err:
    print(err)
