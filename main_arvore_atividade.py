from BinarySearchTree import BinarySearchTree
from binarySearchTreeException import BinarySearchTreeException

arvore = BinarySearchTree()

try:
    while True:
        print('(d) Digitar um texto')
        print('(e) Exibir palavras do texto Ascendente/Descendente')
        print('(c) Exibir frequência de ocorrência das palavras')
        print('(s) Sair')

        escolha = input('Escolha uma das opções acima: ')

        if escolha in 'dD':
            frase = str(input('Digite algo: '))
            arvore.deleteTree()
            lista_frase = frase.split()

            for palavras in lista_frase:
                arvore.add(palavras)

            print('Árvore montada com sucesso!')

        elif escolha in 'eE':
            if not arvore.isEmpty():
                arvore.inorder()
            else:
                raise BinarySearchTreeException('Árvore vazia')

        # ESPAÇO PARA A FREQUENCIA #

        elif escolha in 'sS':
            break

except BinarySearchTreeException as err:
    print(err)
