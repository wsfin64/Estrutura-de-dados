from FilaEncadeada import FilaEncadeada, FilaException
from Computador import Computador
from Recurso import Recurso
from Job import Job
from ListaEncadeada import ListaEncadeada, ListaException


pcs = ListaEncadeada()
jobs = FilaEncadeada()

while True:
    try:

        print(f'Computadores Cadastrados: {pcs}')
        print(f'Jobs em execução: {jobs.tamanho()} | {jobs}')
        print('--------------------------------')
        print('1 - Cadastrar computador')
        print('2 - Inserir Job')
        print('3 - Finalizar Job')
        print('4 - Mostrar nó cabeça')
        print('5 - Sair')

        entrada = int(input('Escolha a opção desejada : '))

        if entrada == 1:
            ip = str(input('Informe o ip da maquina: '))
            hostname = str(input('Hostname da máquina: '))
            contador = 0

            if pcs.tamanho() == 0:
                pcs.insereFim(Computador(ip, hostname))
                print('Maquina cadastrada')
            else:
                for obj in range(1, pcs.tamanho() + 1):
                    ob = pcs.elemento(obj)
                    if ip == ob.ip:  # Verificando se o ip informado já havia sido cadastrado anteriormente
                        raise ListaException('O ip informado, já está cadastrado')

                pcs.insereFim(Computador(ip, hostname))
                print('Maquina cadastrada')

        elif entrada == 2:

            if pcs.vazia():
                raise FilaException('Não há computadores cadastrados! ')

            print(f'Computadores disponíveis: {pcs}')
            pc = str(input('Informe o IP da maquina: '))

            contador = 0
            for obj in range(1, pcs.tamanho() + 1):  # Verficando se o ip informado já está cadastrado
                ob = pcs.elemento(obj)
                if pc == ob.ip:
                    nome_recurso = str(input('Informe o recurso/arquivo: '))
                    tamanho_recurso = float(input('Informe o tamanho do arquivo em MB: '))
                    arquivo = Recurso(tamanho_recurso, nome_recurso)
                    job = Job(pc, arquivo)
                    jobs.enfileirar(job)
                    contador += 1

            if contador == 0:
                raise FilaException('A máquina informada não está cadastrada')

        elif entrada == 3:
            if pcs.vazia():
                raise FilaException('Não há computadores cadastrados! ')

            jobs.desenfileirar()

        elif entrada == 4:
            if jobs.tamanho() == 0:
                raise FilaException('A fila de jobs está vazia')
            print(jobs.mostrar_cabeca())

        elif entrada == 5:
            print('Programa finalizado')
            break

    except TypeError as err:
        print(err)

    except ValueError as err2:
        print('Informe apenas números inteiros')

    except ListaException as err3:
        print(err3)

    except FilaException as err4:
        print(err4)
