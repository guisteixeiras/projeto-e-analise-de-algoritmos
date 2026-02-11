#comentei o código todo pra me auxiliar nos próximos estudos

def remover_duplicados(lista):
    nova_lista = []  #lista nova
    
    for elemento in lista:  #percorre cada elemento da lista original
        if elemento not in nova_lista:  #verifica se ainda não foi adicionado
            nova_lista.append(elemento)  #adiciona na nova lista (append joga pro final da lista)
    return nova_lista  #retorna a lista sem numero repetido

lista = [4, 2, 9, 4, 3, 2, 8]
resultado = remover_duplicados(lista)
print(resultado)

#guilherme teixeira soares souza - 5º período CCOMP