#comentei o código todo pra me auxiliar nos próximos estudos

def ordenacao_por_selecao(lista):  #função
    n = len(lista)  #tamanho da lista na variável n
    
    for i in range(n):  #corre cada posição da lista 
        indice_menor = i  #coloca o menor na 1 posição
        for j in range(i + 1, n):  #roda o resto da lista após a posição i
            if lista[j] < lista[indice_menor]:  #verifica se encontrou um número menor
                indice_menor = j  #atualiza o índice do menor elemento encontrado
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i] #ordenando em crescente
    return lista  #retorna a lista ordenada

lista = [29, 10, 14, 37, 13] 
ordenada = ordenacao_por_selecao(lista) 
print(ordenada) 

#guilherme teixeira soares souza - 5º período CCOMP

