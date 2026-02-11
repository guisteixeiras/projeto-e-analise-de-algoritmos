# Implemente a pesquisa binária usando o loop WHILE, você deve imprimir somente se for divisível por 2,
# se o número não estiver na lista deve retornar -1, anote o tempo de execução.

import time

lista = list(range(1, 51))


valor_procurado = 3

inicio_lista = 0
fim_lista = len(lista) - 1

encontrado = False

inicio_tempo = time.time()

while inicio_lista <= fim_lista:
    meio = (inicio_lista + fim_lista) // 2

    if lista[meio] == valor_procurado:
        encontrado = True
        break
    elif valor_procurado < lista[meio]:
        fim_lista = meio - 1
    else:
        inicio_lista = meio + 1

fim_tempo = time.time()

if encontrado and valor_procurado % 2 == 0:
    print(f"Valor encontrado: {valor_procurado}")
elif not encontrado:
    print("-1")
print(f"Tempo de execução: {fim_tempo - inicio_tempo:.8f} segundos")
