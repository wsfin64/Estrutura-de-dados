

from Conversor import Conversor, ValidacaoError

print('Conversor de expressoes de Infixa para Prefixa e Posfixa')


while True:
    try:
        print('-----------------------------------------------')
        print('1 - Converter uma expressão infixa para POSFIXA')
        print('2 - Converter uma expressão infixa para PREFIXA')
        print('3 - Converter uma expressão infixa para AMBAS')
        print('4 - Para Sair')
        opcao = int(input('Escolha: '))
        print('-----------------------------------------------')

        if opcao == 1:
            expressao = input('Digite uma expressao valida no formato infixo (sem espacos): ')
            p = Conversor(expressao)
            if p.valida():
                print('OK expressão válida!')
                p.posfixa()
                print(f'Expressão original: {expressao}')
                print(f'Expressão Posfixa: {p.saida_posfixa()}')

            else:
                raise ValidacaoError('Expressao inválida')

        if opcao == 2:
            expressao = input('Digite uma expressao valida no formato infixo (sem espacos): ')
            p = Conversor(expressao)
            if p.valida():
                print('OK expressão válida!')
                p.prefixa()
                print(f'Expressão original: {expressao}')
                print(f'Expressão Posfixa: {p.saida_prefixa()}')

            else:
                raise ValidacaoError('Expressão inválida')

        if opcao == 3:
            expressao = input('Digite uma expressao valida no formato infixo (sem espacos): ')
            p = Conversor(expressao)
            if p.valida():
                print('OK expressão válida!')
                p.posfixa()
                p.prefixa()
                print(f'Expressão original: {expressao}')
                print(f'Expressão Prefixa: {p.saida_prefixa()}')
                print(f'Expressão Posfixa: {p.saida_posfixa()}')

            else:
                raise ValidacaoError('Expressão inválida!')

        if opcao == 4:
            break

    except ValidacaoError as err:
        print(err)

    except ValueError:
        print('Digite apenas números inteiros entre 1 e 4')
