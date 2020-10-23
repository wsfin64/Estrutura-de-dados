# Aluno: Wellington da Silva

from ListaEncadeada import ListaEncadeada, ListaException

lista = ListaEncadeada()

while True:

    try:

        print('--------------------------------')
        lista.imprimir()
        print('Editor de Listas')
        print('--------------------------------')
        print('1 - Tamanho')
        print('2 - Inserir')
        print('3 - Remover')
        print('4 - Exibr elemento')
        print('5 - Procurar valor')
        print('6 - Modificar lista')
        print('-------')
        print('7 - Inserir no início')
        print('8 - Insere no fim da lista')
        print('9 - Esvaziar a lista')
        print('10 - Remover o primeiro elemento')
        print('11 - Remover o último elemento')
        print('12 - Remover todas as ocorrências de um valor')
        print('13 - Sair')

        entrada = int(input('Digite sua opção: '))

        if entrada == 1:
            print()
            print(f'A lista possui {lista.tamanho()} elemento(s) no momento')
            print()

        elif entrada == 2:
            posicao = int(input('Informe a posição de inserção: '))
            dado = input('Informe o dado: ')
            lista.inserir(posicao, dado)

        elif entrada == 3:
            posicao = int(input('Informe a posição do elemento para removê-lo: '))
            print(f' O elemento {lista.remover(posicao)} foi removido')

        elif entrada == 4:
            posicao = int(input('Informe a posição para visualizar: '))
            print(f'O elemento da posição {posicao} é {lista.elemento(posicao)}')

        elif entrada == 5:
            dado = input('Informe o dado da ser buscado: ')
            print(lista.busca(dado))

        elif entrada == 6:
            posicao = int(input('Informe a posição do dado que deseja modificar: '))
            dado = input('Agora, informe o dado que substituirá o dado selecionado: ')
            lista.modificar(posicao, dado)

        elif entrada == 7:
            dado = input('Informe o dado que será inserido na primeira posição da lista: ')
            lista.insereInicio(dado)

        elif entrada == 8:
            dado = input('Informe o dado para inserção no fim da lista: ')
            lista.insereFim(dado)

        elif entrada == 9:
            lista.esvaziar()

        elif entrada == 10:
            print(f'O elemento {lista.removeInicio()} foi removido da lista')

        elif entrada == 11:
            print(f'O elemento {lista.removeFinal()} foi removido da lista')

        elif entrada == 12:
            dado = input('Informe o dado para remover todas as occorrências: ')
            lista.removerOcorrencias(dado)

        if entrada == 13:
            break

    except ListaException as err:
        print(err)

    except ValueError:
        print('Digite um número inteiro')
