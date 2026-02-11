# Implemente a pesquisa simples usando o loop WHILE e teste em uma lista de 50 números, anote o tempo de execução

import time

lista = list(range(1, 51))

valor_procurado = 37

indice = 0
encontrado = False

inicio = time.time()

while indice < len(lista):
    if lista[indice] == valor_procurado:
        encontrado = True
        break
    indice += 1

fim = time.time()

if encontrado:
    print(f"Valor {valor_procurado} encontrado na posição {indice}")
else:
    print(f"Valor {valor_procurado} não encontrado")

print(f"Tempo de execução: {fim - inicio:.8f} segundos")




