from node_tree import Node
from arvore_binaria import ArvoreBinaria

if __name__ == '__main__':

    raiz = Node('A')
    raiz.esq = Node('B')
    raiz.dir = Node('C')

    # Criando ponteiros a esquerda e direita da raiz
    p = raiz.esq
    q = raiz.dir

    # Percorrendo o lado esquerdo da árvore
    p.esq = Node('D')
    p = p.esq

    p.dir = Node('G')

    # Percorrendo o lado direito da árvore
    q.esq = Node('E')
    q.dir = Node('F')

    q = q.esq

    q.esq = Node('H')
    q.dir = Node('I')

    arvore = ArvoreBinaria()

    print('Pre-ordem')
    arvore.pre_ordem(raiz)

    print('--------------')
    print('Em ordem')
    arvore.em_ordem(raiz)

    print('--------------')
    print('Pos Ordem')
    arvore.pos_ordem(raiz)
