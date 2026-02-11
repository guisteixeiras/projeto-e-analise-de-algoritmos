#comentei o código todo pra me auxiliar nos próximos estudos

def segundo_maior(lista):
    maior = lista[0]
    segundo_maior = lista[0] #também começa com o menor valor possível
    
    for numero in lista:  #percorre cada número da lista
        if numero > maior:  
            segundo_maior = maior #o antigo maior vira segundo maior
            maior = numero #atualiza o maior
        elif numero > segundo_maior and numero != maior:
            segundo_maior = numero  #atualiza o segundo maior
    return segundo_maior

lista = [5, 1, 9, 3, 7]
resultado = segundo_maior(lista)
print(resultado)

#guilherme teixeira soares souza - 5º período CCOMP
