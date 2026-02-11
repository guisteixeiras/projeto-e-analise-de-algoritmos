#comentei o código todo pra me auxiliar nos próximos estudos

def pesquisa_linear (lista, alvo): #função
    indice = 0 # começando pela posição 0 na lista

    while indice < len(lista): # loop para percorrer a lista // len(lista) é poara retornar o tamanho da lista
        if lista[indice] == alvo: #valida se os números batem
            return indice # se encontrar retorna a posição (indice) da lista
        indice +=1 # incrementa e passa pro proximo indice da lista
    
    return -1 # retonra -1 se o valor não for encontrado na lista toda

lista = [3, 7, 1, 9, 5]
numero_alvo = 9

resultado = pesquisa_linear(lista, numero_alvo) # chama a função, retorna o resultado para "resultado"
print(resultado) 

#guilherme teixeira soares souza - 5º período CCOMP