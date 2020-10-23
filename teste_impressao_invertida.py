from ListaEncadeada import ListaEncadeada, ListaException


try:

    lista = ListaEncadeada()

    lista.insereInicio(10)
    lista.insereInicio(20)
    lista.insereInicio(30)

    lista.imprimir()
    lista.imprimirInvertido()
except ListaException as err:
    print(err)