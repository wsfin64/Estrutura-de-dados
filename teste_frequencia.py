from BinarySearchTree import BinarySearchTree


arvore = BinarySearchTree()
string = 'Kilson é o maior pegador de maior gordinhas bonitas de pegador joao pessoa pegador'


array = string.split()
print(array)

for i in array:
    arvore.add(i)

arvore.inorder()

print(f'Maior: {arvore.frequencia("maior")}')
