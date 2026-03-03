class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def pre_ordem(no):
    if no:
        print(no.valor, end=" ")
        pre_ordem(no.esquerda)
        pre_ordem(no.direita)

def em_ordem(no):
    if no:
        em_ordem(no.esquerda)
        print(no.valor, end=" ")
        em_ordem(no.direita)

def pos_ordem(no):
    if no:
        pos_ordem(no.esquerda)
        pos_ordem(no.direita)
        print(no.valor, end=" ")

