from PilhaEncadeada import PilhaEncadeada, PilhaException


class ConversorPosfixa:

    def __init__(self, expressao):
        self.__expressao = expressao
        self.__saida = ''
        self.__pilha = PilhaEncadeada()
        self.__operadores = ['+', '-', '*', '/', '^', ')', '(']

    @property
    def expressao(self):
        return self.__expressao

    def operador(self, char):
        return True if char in self.__operadores else False

    def operando(self, char):
        if char not in self.__operadores:
            return True

    def valida(self):
        """Verifica sa a expressão informada é válida ou não.
        Este exemplo estarei utilizando as seguintes regras de validação:
        1 - O número de parêntesis '(' abrindo a expressão, deve ser o mesmo de parêntesis fechando a expressão ')'.
        2 - Após um operandor deverá obrigatoriamente existir um operando ou uma expressão com ()."""

        dados = PilhaEncadeada()

        for caractere in self.__expressao:

            if caractere == '(':
                dados.empilhar(caractere)
            elif caractere == ')':
                if not dados.vazia():
                    dados.desempilhar()
                else:
                    dados.empilhar(caractere)
                    break
        return True if dados.vazia() else False

    def obterPrioridade(self, operador):

        if operador == '(':
            return 1
        elif operador == '+' or operador == '-':
            return 2
        elif operador == '*' or operador == '/':
            return 3
        else:
            return 4

    def conversao(self):

        if self.valida():

            for i in range(len(self.__expressao)):
                if self.operador(self.__expressao[i]):

                    if self.__pilha.vazia():

                        self.__pilha.empilhar(self.__expressao[i])

                    else:
                        prioridade_topo = self.obterPrioridade(self.__pilha.topo())
                        prioridade_operador = self.obterPrioridade(self.__expressao[i])

                        if prioridade_operador > prioridade_topo and self.__expressao[i] != ')':

                            self.__pilha.empilhar(self.__expressao[i])

                        while not self.__pilha.vazia() and prioridade_topo >= prioridade_operador and self.__expressao[i] != '(':

                            aux = self.__pilha.topo()

                            self.__saida += aux

                            self.__pilha.desempilhar()

                            self.__pilha.empilhar(self.__expressao[i])

                            if self.__pilha.topo() == self.__expressao[i]:
                                break

                        if self.__expressao[i] == '(':
                            self.__pilha.empilhar(self.__expressao[i])

                        if self.__expressao[i] == ')':
                            while self.__pilha.topo() != '(':

                                aux = self.__pilha.topo()

                                self.__saida += aux
                                self.__pilha.desempilhar()

                            if self.__pilha.topo() == '(':
                                self.__pilha.desempilhar()

                else:
                    self.__saida += self.__expressao[i]

                print(self.__pilha)

            while not self.__pilha.vazia():
                if self.__pilha.topo() == '(':
                    self.__pilha.desempilhar()
                else:
                    aux = self.__pilha.topo()
                    self.__saida += aux
                    self.__pilha.desempilhar()

        else:
            print('Expressão inválida!')

    def saida(self):
        return self.__saida

    def pilha(self):
        return self.__pilha


string = 'a*(b+c)/d'
conv = ConversorPosfixa(string)

conv.conversao()

print(conv.saida())
