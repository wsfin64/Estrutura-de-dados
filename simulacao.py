# Aluno Wellington da Silva

from ListaEncadeada import ListaEncadeada, ListaException
from random import randint

try:
    # Instanciando as lista L1, L2, L3, 4 L4
    print('* Criando as listas L1, L2, L3 e L4')
    L1 = ListaEncadeada()
    L2 = ListaEncadeada()
    L3 = ListaEncadeada()
    L4 = ListaEncadeada()

    print('* Inserindo 10 números aleatórios (entre 1 e 100) na lista L1:')
    for i in range(10):  # Inserindo elementos na lista L1
        num = randint(1, 100)
        L1.insereFim(num)
        print(f'Valor{i + 1}: {num}')

    print()

    print('* Inserindo 15 números aleatórios (entre 1 e 100) na lista L2:')

    for j in range(15):  # Inserindo elementos na lista L2
        num = randint(1, 100)
        L2.insereFim(num)
        print(f'Valor{j + 1}: {num}')

    print()

    print('* Concatenando L1 e L2 em L3:')
    print(f'Conteudo de L1: {L1}')
    print(f'Conteudo de L2: {L2}')

    L3.concatena(L1, L2)  # contatenando as listas l1 e l2 na l3, utilizando o método criado na classe ListaEncadeada
    print(f'Contatenação em L3: {L3}')

    print()

    print('* Armazenando os elementos da L3 na L4 na ordem inversa')

    for dado in range(1, L3.tamanho() + 1):
        L4.insereInicio(L3.elemento(dado))
    print(f'Conteúdo de L4: {L4}')

    print()
    # imprimindo as listas l1, l2, l3 e l4
    print(f'L1: {L1}')
    print(f'L2: {L2}')
    print(f'L3: {L3}')
    print(f'L1: {L4}')

except ListaException as err:
    print(err)
