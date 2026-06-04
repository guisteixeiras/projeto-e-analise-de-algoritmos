import random

def particionar(arr, baixo, alto):
    pivo = arr[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def quicksort_iterativo(arr):
    baixo = 0
    alto = len(arr) - 1
    pilha = []
    pilha.append((baixo, alto))

    while pilha:
        baixo, alto = pilha.pop()
        if baixo < alto:
            p = particionar(arr, baixo, alto)
            pilha.append((baixo, p - 1))
            pilha.append((p + 1, alto))


array = random.sample(range(1, 200), 15)
print(f"Antes:  {array}")
quicksort_iterativo(array)
print(f"Depois: {array}")