import time
import random
import sys

sys.setrecursionlimit(20000)

def particionar_primeiro(arr, baixo, alto):
    arr[baixo], arr[alto] = arr[alto], arr[baixo]
    pivo = arr[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def quicksort_primeiro(arr, baixo, alto):
    if baixo < alto:
        p = particionar_primeiro(arr, baixo, alto)
        quicksort_primeiro(arr, baixo, p - 1)
        quicksort_primeiro(arr, p + 1, alto)


def particionar_aleatorio(arr, baixo, alto):
    idx = random.randint(baixo, alto)
    arr[idx], arr[alto] = arr[alto], arr[idx]
    pivo = arr[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def quicksort_aleatorio(arr, baixo, alto):
    if baixo < alto:
        p = particionar_aleatorio(arr, baixo, alto)
        quicksort_aleatorio(arr, baixo, p - 1)
        quicksort_aleatorio(arr, p + 1, alto)


def mediana_de_tres(arr, baixo, alto):
    meio = (baixo + alto) // 2
    a, b, c = arr[baixo], arr[meio], arr[alto]
    if (a <= b <= c) or (c <= b <= a):
        return meio
    elif (b <= a <= c) or (c <= a <= b):
        return baixo
    else:
        return alto

def particionar_mediana(arr, baixo, alto):
    idx = mediana_de_tres(arr, baixo, alto)
    arr[idx], arr[alto] = arr[alto], arr[idx]
    pivo = arr[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def quicksort_mediana(arr, baixo, alto):
    if baixo < alto:
        p = particionar_mediana(arr, baixo, alto)
        quicksort_mediana(arr, baixo, p - 1)
        quicksort_mediana(arr, p + 1, alto)


array_original = list(range(10000, 0, -1))

arr1 = array_original[:]
inicio = time.time()
quicksort_primeiro(arr1, 0, len(arr1) - 1)
print(f"Pivô Primeiro:   {time.time() - inicio:.4f}s")

arr2 = array_original[:]
inicio = time.time()
quicksort_aleatorio(arr2, 0, len(arr2) - 1)
print(f"Pivô Aleatório:  {time.time() - inicio:.4f}s")

arr3 = array_original[:]
inicio = time.time()
quicksort_mediana(arr3, 0, len(arr3) - 1)
print(f"Pivô Mediana:    {time.time() - inicio:.4f}s")