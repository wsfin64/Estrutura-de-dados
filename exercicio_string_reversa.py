# imprimir uma string ao contrário usando recursividade


def printstr(string):
    if string == '':
        return
    print(string[0], end='')
    printstr(string[1:])


def printstr_invertida(string):
    if string == '':
        return
    printstr_invertida(string[1:])
    print(string[0], end='')


def tamanho_string(string):
    if string == '':
        return 0
    else:
        return 1 + tamanho_string(string[1:])


def somaDigitos(inteiro):
    if inteiro == 0:
        return 0
    else:
        return inteiro % 10 + somaDigitos(int(inteiro / 10))

def recursiva(v):
    if len(v) < 2:
        return True
    return v[0] <= v[1] and recursiva(v[1:])


"""
string = 'IFPB'

printstr(string)
print()
printstr_invertida(string)
print()
print('Tamanho:', tamanho_string(string))
"""
# print(-2 % 10)

print(30 % 15)

vetor = [25, 36, 12, 8, 54, 15, 33]
vetor1 = []
print(recursiva(vetor1))






