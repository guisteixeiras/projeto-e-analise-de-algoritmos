#comentei o código todo pra me auxiliar nos próximos estudos

def mover_zeros(lista):
    posicao = 0 #indice começa com 0 até o tam da lista (leng(lista))
    
    for i in range(len(lista)): #percorre toda a lista (range idnica o índice do valor)
        if lista[i] != 0:  #se não for zero
            lista[posicao] = lista[i]  #move o número i para o inicio
            posicao += 1  #encrementa

    while posicao < len(lista): #preenche o restante da lista com zeros
        lista[posicao] = 0
        posicao += 1
    return lista

lista = [0, 1, 0, 3, 12]
resultado = mover_zeros(lista)
print(resultado)

#guilherme teixeira soares souza - 5º período CCOMP
