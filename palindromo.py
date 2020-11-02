def is_palindromo(_string):
    if len(_string) <= 2:
        return 'É palíndromo'
    if _string[0] == _string[-1]:
        print(_string[1:-1])
        return is_palindromo(_string[1:-1])
    return 'Não é palíndromo'


string = 'radar'
print(is_palindromo(string))
