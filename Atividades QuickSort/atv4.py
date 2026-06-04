import time
import random
import sys

sys.setrecursionlimit(100000)

LIMITE = 10

def insertion_sort(arr, baixo, alto):
    for i in range(baixo + 1, alto + 1):
        chave = arr[i]
        j = i - 1
        while j >= baixo and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def particionar(arr, baixo, alto):
    pivo = arr[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def quicksort_puro(arr, baixo, alto):
    if baixo < alto:
        p = particionar(arr, baixo, alto)
        quicksort_puro(arr, baixo, p - 1)
        quicksort_puro(arr, p + 1, alto)

def quicksort_hibrido(arr, baixo, alto):
    if alto - baixo + 1 <= LIMITE:
        insertion_sort(arr, baixo, alto)
        return
    if baixo < alto:
        p = particionar(arr, baixo, alto)
        quicksort_hibrido(arr, baixo, p - 1)
        quicksort_hibrido(arr, p + 1, alto)


array_original = random.sample(range(1, 200000), 50000)

arr1 = array_original[:]
inicio = time.time()
quicksort_puro(arr1, 0, len(arr1) - 1)
print(f"Quicksort puro:    {time.time() - inicio:.4f}s")

arr2 = array_original[:]
inicio = time.time()
quicksort_hibrido(arr2, 0, len(arr2) - 1)
print(f"Quicksort híbrido: {time.time() - inicio:.4f}s")