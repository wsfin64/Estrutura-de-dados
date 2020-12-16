from FilaEncadeada import FilaEncadeada, FilaException
from Computador import Computador
from Recurso import Recurso
from Job import Job
from ListaEncadeada import ListaEncadeada, ListaException
from BandaInternet import BandaInternet

pcs = ListaEncadeada()
jobs = ListaEncadeada()
banda = BandaInternet(10)
donwload_finalizados = FilaEncadeada()


while True:
    try:

        print(f'Computadores Cadastrados: {pcs}')
        print(f'Jobs em execução: {jobs.tamanho()} | {jobs}')
        print(f'Largura da banda de internet: {banda.largura} MB')
        print('--------------------------------')
        print('1 - Cadastrar computador')
        print('2 - Inserir Job')
        print('3 - Finalizar Job')
        print('4 - Mostrar downloads finalizados')
        print('5 - ALterar largura de banda')
        print('6 - Importar dados')
        print('7 - Simulação')
        print('8 - Sair')

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
                    jobs.insereFim(job)
                    contador += 1

            if contador == 0:
                raise ListaException('A máquina informada não está cadastrada')

        elif entrada == 3:
            if pcs.vazia():
                raise ListaException('Não há computadores cadastrados! ')

            jobs.removeInicio()

        elif entrada == 4:
            print(f'Jobs Finalizados: {donwload_finalizados}')

        elif entrada == 5:
            nova_banda = int(input('Informe a nova banda da internet em MB: '))
            banda.largura = nova_banda

        elif entrada == 6:
            lista_maquinas = []
            arquivo = open('computadores.txt')

            # Quebrando as linhas do txt e salvando em uma lista
            maquina = arquivo.read().split('\n')

            # Qubrando as strings da lista maquina e adicionado na lista_maquinas
            for i in maquina:
                maquina_filtrada = i.split()
                lista_maquinas.append(maquina_filtrada)

            for i in range(len(lista_maquinas)):
                ip = str(lista_maquinas[i][0])
                host = str(lista_maquinas[i][1])
                prioridade = lista_maquinas[i][2]
                pcs.insereFim(Computador(ip, host, prioridade))

            # ------------- LENDO O ARQUIVO RECURSOS.TXT ------------------#

            lista_recursos = []
            arquivo_recursos = open('recursos.txt')

            recurso = arquivo_recursos.read().split('\n')

            for i in recurso:
                recurso_filtrado = i.split()
                lista_recursos.append(recurso_filtrado)

            for i in range(len(lista_recursos)):
                tamanho = float(lista_recursos[i][0])
                nome = str(lista_recursos[i][1])
                arquivo = Recurso(tamanho, nome)
                job = Job(lista_maquinas[i], arquivo)
                jobs.insereFim(job)

        elif entrada == 7:
            ciclo = 1
            diferenca = 0
            download = (banda.largura * 1024) / 8
            transmissao = 0
            lista_indices = []
            indice = jobs.tamanho()
            while True:

                if jobs.tamanho() == 1:
                    break

                print(f'Ciclo atual: {ciclo}')

                for obj in range(1, indice):
                    ob = jobs.elemento(obj)
                    print(f'#{obj} - {ob.computador[0]} -------- {ob.recurso.nome} ------- Velocidade Download {transmissao:.2f}kb/s  ------- Baixados: {diferenca:.2f}KB/{ob.recurso.tamanho:.2f}KB')

                    if diferenca >= ob.recurso.tamanho:
                        maq = ob.computador[0]
                        lista_indices.append(maq)
                    transmissao = download / indice
                diferenca = diferenca + transmissao
                ciclo += 1

                if len(lista_indices) > 0:
                    for i in range(len(lista_indices)):
                        for obj in range(1, indice):
                            ob = jobs.elemento(obj)
                            if lista_indices[i] == ob.computador[0]:
                                donwload_finalizados.enfileirar(jobs.elemento(obj))
                                jobs.remover(obj)
                                indice -= 1

                opcao = input('Aperte enter para o proximo ciclo ou tecle s para sair: ')
                if opcao == 's':
                    break

            print('Simulação finalizada!')
        elif entrada == 8:
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
