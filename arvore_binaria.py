class ArvoreBinaria:

    def pre_ordem(self, arvore):
        if arvore is not None:
            print(arvore.dado, end='')  # Visita a raiz
            self.pre_ordem(arvore.esq)
            self.pre_ordem(arvore.dir)

    def em_ordem(self, arvore):
        if arvore is not None:
            self.em_ordem(arvore.esq)
            print(arvore.dado, end='')  # Visita a raiz
            self.em_ordem(arvore.dir)

    def pos_ordem(self, arvore):
        if arvore is not None:
            self.pos_ordem(arvore.esq)
            self.pos_ordem(arvore.dir)
            print(arvore.dado, end='')  # Visita a raiz
