class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, data):
        if self.leftChild == None:
            self.leftChild = Node(data)	

    def insertRight(self,data):
        if self.rightChild == None:
            self.rightChild = Node(data)

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setValue(self,newValue):
        self.data = newValue

    def getValue(self):
        return self.data

    def __str__(self):
        return str(self.data)

    def hasLeftChild(self):
        return self.leftChild != None

    def hasRightChild(self):
        return self.rightChild != None
        

class BinarySearchTree:
    # Construtor que inicializa uma BST sem nó raiz
    def __init__(self):
        self.__root = None

    def getRoot(self):
        return self.__root

    def isEmpty(self):
        return self.__root == None

    # adiciona um novo nó automaticamente, na posição correta
    def add(self, data):
        if(self.__root == None):
            self.__root = Node(data)
        else:
            self.__add(data,self.__root)

    def __add(self, data, node):
        if ( data < node.data):
            if( node.getLeftChild() != None):
                self.__add(data, node.getLeftChild())
            else:
                node.insertLeft(data)
        else:
            if( node.getRightChild() != None):
                self.__add(data, node.getRightChild())
            else:
                node.insertRight(data)
            
    def search(self, chave ):
        if( self.__root != None ):
            return self.__searchData(chave, self.__root)
        else:
            return None
    
    def __searchData(self, chave, node):
        if ( chave == node.getValue()):
            return node
        elif ( chave < node.getValue() and node.getLeftChild() != None):
            return self.__searchData( chave, node.getLeftChild())
        elif ( chave > node.getValue() and node.getRightChild() != None):
            return self.__searchData( chave, node.getRightChild())
        else:
            return None

    def preorder(self):
        self.__preorder(self.__root)
        print()

    def inorder(self):
        self.__inorder(self.__root)
        print()

    def postorder(self):
        self.__postorder(self.__root)
        print()
        
    def __preorder(self, node):
        if( node != None):
            print(f'{node.data} ', end='')
            self.__preorder(node.leftChild)
            self.__preorder(node.rightChild)

    def __inorder(self, node):
        if( node != None):
            self.__inorder(node.leftChild)
            print(f'{node.data} ', end='')
            self.__inorder(node.rightChild)

    def __postorder(self, node):
        if( node != None):
            self.__postorder(node.leftChild)
            self.__postorder(node.rightChild)
            print(f'{node.data} ', end='')

    def deleteTree(self):
        # garbage collector fará o trabalho de remoção dos nós automaticamente. 
        self.__root = None

    def deleteNode(self, key):
        self.__deleteNode(self.__root, key)
    
    # Dado um nó de uma BST e uma chave busca, este método
    # deleta o nó que contém a chave e devolve o novo nó raiz
    def __deleteNode(self,root, key):
        # Caso primário: não há raiz
        if root is None: 
            return root
  
        # Se a chave a ser deletada é menor do que a chave do nó raiz (da vez),
        # então a chave se encontra na subárvore esquerda
        if key < root.data:
            root.leftChild = self.__deleteNode(root.leftChild, key) 
  
        # Se a chave a ser deletada é maior do que a chave do nó raiz (da vez),
        # então a chave se encontra na subárvore esquerda
        elif(key > root.data):
            root.rightChild = self.__deleteNode(root.rightChild, key) 
  
        # Se a chave é igual à chave do nó raiz, então este é o nó 
        # a ser removido
        else:
            # (1) Nó com apenas 1 filho ou nenhum filho
            if root.leftChild is None : 
                temp = root.rightChild  
                root = None 
                return temp

            elif root.rightChild is None :
                temp = root.leftChild  
                root = None
                return temp 
  
            # (2) Nó com dois filhos: obtem o sucessor inorder
            # (o menor nó da subárvore direita) 
            temp = self.__minValueNode(root.rightChild) 
  
            # copia o conteúdo do sucessor inorder para este nós
            root.data = temp.data 
  
            # Deletao sucessor inorder
            root.rightChild = self.__deleteNode(root.rightChild , temp.data)

        return root


    # Dada uma BST não vazia, retorna o nó
    # com a menor chave encontrada na árvore. Note que a árvore
    # inteira não precisa ser percorrida
    def __minValueNode(self, node):
        current = node 
  
        # loop para baixo a fim de encontrar a folha mais a esquerda
        while(current.leftChild is not None): 
            current = current.leftChild  
  
        return current

    # Dada uma BST não vazia, retorna o nó
    # com o maior valor de chave encontrada na árvore. Note que a árvore
    # inteira não precisa ser percorrida 
    def __maxValueNode(self, node):
        current = node

         # loop para baixo a fim de encontrar a folha mais a direita
        while(current.rightChild is not None): 
            current = current.rightChild
  
        return current

    def frequencia(self, chave):
        if self.__root is not None:
            return self.__frequencia(chave, self.__root)
        else:
            return None

    def __frequencia(self, chave, node):

        if chave != node.getValue():

            if chave > node.getValue() and node.getRightChild() is not None:
                return self.__frequencia(chave, node.getRightChild())

            elif chave < node.getValue() and node.getLeftChild() is not None:
                return self.__frequencia(chave, node.getLeftChild())

        if chave == node.getValue():

            if chave == node.getValue() and node.getRightChild() is not None:
                return 1 + self.__frequencia(chave, node.getRightChild())

            if chave == node.getValue() and node.getLeftChild() is not None:
                return 1 + self.__frequencia(chave, node.getLeftChild())

            else:
                return 1
        else:
            return 0
