lista = [7, 8, 15, 23, 18, 5, 2, 29, 30, 12]  # lista original com os números desordenados

def quicksort(lista):  # define a função quicksort, que recebe uma lista
    if len(lista) < 2:  # verifica se a lista tem menos de 2 elementos
        return lista  # se tiver 0 ou 1 elemento, ela já está ordenada

    else:  # se a lista tiver 2 ou mais elementos
        pivo = lista[0]  # escolhe o primeiro elemento da lista como pivô

        menores = [i for i in lista[1:] if i <= pivo]  # cria uma lista com os elementos menores ou iguais ao pivô
        maiores = [i for i in lista[1:] if i > pivo]  # cria uma lista com os elementos maiores que o pivô

        return quicksort(menores) + [pivo] + quicksort(maiores)  
        # ordena recursivamente os menores
        # coloca o pivô no meio
        # ordena recursivamente os maiores

print(quicksort(lista))  # chama a função e mostra a lista ordenada