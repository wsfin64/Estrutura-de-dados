from PilhaEncadeada import PilhaEncadeada, PilhaException


class ValidacaoError(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class Conversor:

    def __init__(self, expressao):
        self.__expressao = expressao
        self.__saida = ''
        self.__saida_prefixa = ''
        self.__pilha = PilhaEncadeada()
        self.__operadores = ['+', '-', '*', '/', '^', ')', '(']

    @property
    def expressao(self):
        # Retorna a expressao Infixa passada pelo usuário.
        return self.__expressao

    def operador(self, char):
        # Verificando se o operador está listado entre os operadores válidos
        return True if char in self.__operadores else False

    def operando(self, char):
        # Verificando que se o operador é uma letra do alfabeto.
        if char.isalpha():
            return True

    def valida(self):
        """Verifica sa a expressão informada é válida ou não.
        Este exemplo estarei utilizando as seguintes regras de validação:
        1 - Verificar se há espaços na expressão
        2 - Verificando se cada caractere da expressao é um operador ou operando.
        3 - Verificando as paridades dos parênteses."""

        dados = PilhaEncadeada()

        if ' ' in self.__expressao:
            raise ValidacaoError('Digite uma expressão válida sem espaços.')

        for char in self.__expressao:
            if not self.operador(char) and not self.operando(char):
                raise ValidacaoError('Expressão inválida!')

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

    def posfixa(self):

        # Este método converte expressao infixa passada pelo usuário para Posfixa.

        if self.valida():

            for exp in self.__expressao:
                if self.operador(exp):

                    if self.__pilha.vazia():

                        self.__pilha.empilhar(exp)

                    else:
                        prioridade_topo = self.obterPrioridade(self.__pilha.topo())
                        prioridade_operador = self.obterPrioridade(exp)

                        if prioridade_operador > prioridade_topo and exp != ')':

                            self.__pilha.empilhar(exp)

                        while not self.__pilha.vazia() and prioridade_topo >= prioridade_operador and exp != '(':

                            aux = self.__pilha.topo()

                            self.__saida += aux

                            self.__pilha.desempilhar()

                            self.__pilha.empilhar(exp)

                            if self.__pilha.topo() == exp:
                                break

                        if exp == '(':
                            self.__pilha.empilhar(exp)

                        if exp == ')':
                            while self.__pilha.topo() != '(':

                                aux = self.__pilha.topo()

                                self.__saida += aux
                                self.__pilha.desempilhar()

                            if self.__pilha.topo() == '(':
                                self.__pilha.desempilhar()

                else:
                    self.__saida += exp

                # print(self.__pilha)

            while not self.__pilha.vazia():
                if self.__pilha.topo() == '(':
                    self.__pilha.desempilhar()
                else:
                    aux = self.__pilha.topo()
                    self.__saida += aux
                    self.__pilha.desempilhar()

        else:
            raise ValidacaoError('Expressao inválida')

    def prefixa(self):

        # Conversão da expressão infixa para prefixa

        string = self.__expressao
        string_invertida = ''

        pilha_inversao = PilhaEncadeada()

        for i in string:
            pilha_inversao.empilhar(i)

        for i in range(len(string)):
            dado = pilha_inversao.desempilhar()
            if dado == ')':
                string_invertida += '('
            elif dado == '(':
                string_invertida += ')'
            else:
                string_invertida += dado

        self.__expressao = string_invertida

        if self.valida():

            for exp in self.__expressao:
                if self.operador(exp):

                    if self.__pilha.vazia():

                        self.__pilha.empilhar(exp)

                    else:
                        prioridade_topo = self.obterPrioridade(self.__pilha.topo())
                        prioridade_operador = self.obterPrioridade(exp)

                        if prioridade_operador > prioridade_topo and exp != ')':

                            self.__pilha.empilhar(exp)

                        while not self.__pilha.vazia() and prioridade_topo >= prioridade_operador and exp != '(':

                            aux = self.__pilha.topo()

                            self.__saida_prefixa += aux

                            self.__pilha.desempilhar()

                            self.__pilha.empilhar(exp)

                            if self.__pilha.topo() == exp:
                                break

                        if exp == '(':
                            self.__pilha.empilhar(exp)

                        if exp == ')':
                            while self.__pilha.topo() != '(':

                                aux = self.__pilha.topo()

                                self.__saida_prefixa += aux
                                self.__pilha.desempilhar()

                            if self.__pilha.topo() == '(':
                                self.__pilha.desempilhar()

                else:
                    self.__saida_prefixa += exp

                # print(self.__pilha)

            while not self.__pilha.vazia():
                if self.__pilha.topo() == '(':
                    self.__pilha.desempilhar()
                else:
                    aux = self.__pilha.topo()
                    self.__saida_prefixa += aux
                    self.__pilha.desempilhar()

        else:
            raise ValidacaoError('Expressao inválida')

        string = self.__saida_prefixa
        string_invertida = ''

        pilha_inversao = PilhaEncadeada()

        for i in string:
            pilha_inversao.empilhar(i)

        for i in range(len(string)):
            dado = pilha_inversao.desempilhar()
            if dado == ')':
                string_invertida += '('
            elif dado == '(':
                string_invertida += ')'
            else:
                string_invertida += dado

        self.__saida_prefixa = string_invertida

    def saida_posfixa(self):
        if ')' in self.__saida:
            new = self.__saida.replace(')', '')
            self.__saida = new
        return self.__saida

    def saida_prefixa(self):
        return self.__saida_prefixa
