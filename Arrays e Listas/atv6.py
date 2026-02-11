#comentei o código todo pra me auxiliar nos próximos estudos

def pesquisa_binaria(lista, alvo): #função
    indice = 0 #primeiro índice
    fim = len(lista) -1 #len(lista) len(lista) = tamanho da lista

    while indice <= fim: #loop para rodar a lista toda
        meio = (indice + fim) // 2 #divide em 2 para saber para qual lado buscar

        if lista[meio] == alvo: #verifica se o valor está no meio
            return meio #se for, retorna o índice
        elif lista[meio] < alvo: #se o valor do meio for menor, signifca que o alvo é maior 
            indice = meio + 1 
        else:   
            fim = meio - 1 #se o valor for menor que a metade, subtrai 1 divide novamente 
    return - 1

lista = [1, 3, 5, 7, 9, 11, 15]
alvo = 3

resultado = pesquisa_binaria(lista, alvo)
print(resultado)  

#guilherme teixeira soares souza - 5º período CCOMP