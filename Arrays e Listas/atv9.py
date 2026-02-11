#comentei o código todo pra me auxiliar nos próximos estudos

def intersecao(lista1, lista2):
    nova_lista = []  #lista que vai guardar os valores iguais
    
    for elemento in lista1:  #percorre a primeira lista
        if elemento in lista2:  #verifica se tem na segunda lista
            nova_lista.append(elemento)  #adiciona na nova lista
    return nova_lista  #retorna os valores iguais

lista1 = [1, 3, 5, 7, 9]
lista2 = [3, 4, 5, 6, 9]

resultado = intersecao(lista1, lista2)
print(resultado)

#guilherme teixeira soares souza - 5º período CCOMP