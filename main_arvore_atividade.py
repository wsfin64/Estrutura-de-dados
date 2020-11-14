from BinarySearchTree import BinarySearchTree
from binarySearchTreeException import BinarySearchTreeException

arvore = BinarySearchTree()


while True:
    try:
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
                print('----------------------')
                print('Em ordem Ascendente:')
                arvore.inorder()
                print('Em ordem Descendente:')
                arvore.inorder_descendente()
                print('----------------------')

            else:
                raise BinarySearchTreeException('Árvore vazia')

        elif escolha in 'cC':
            if not arvore.isEmpty():
                print('----------------------------------------')
                arvore.listar()
                array = arvore.getValues()
                array_filtrado = set(array)
                for valor in array_filtrado:
                    print(f'{valor}: {arvore.frequencia(valor)}')
                    # Detalhes da implementação do metodo frequencia está na classe BinarySearchTree
                print('----------------------------------------')
            else:
                raise BinarySearchTreeException('A arvore esta vazia')

        elif escolha in 'sS':
            break

    except BinarySearchTreeException as err:
        print(err)
