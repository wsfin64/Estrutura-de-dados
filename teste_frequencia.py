from BinarySearchTree import BinarySearchTree


arvore = BinarySearchTree()
string = 'estrutura estrutura de dados é outro nível de programação'


array = string.split()
print(array)

for i in array:
    arvore.add(i)

ar = arvore.inorder()

print(arvore.frequencia('estrutura'))
