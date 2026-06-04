import random

def particionar(arr, baixo, alto):
    pivo = arr[alto]
    i = baixo - 1

    for j in range(baixo, alto):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    print(f"Pivô usado: {pivo} | Array agora: {arr}")
    return i + 1

def quicksort(arr, baixo, alto):
    if baixo < alto:
        pos_pivo = particionar(arr, baixo, alto)
        quicksort(arr, baixo, pos_pivo - 1)
        quicksort(arr, pos_pivo + 1, alto)

array = random.sample(range(1, 100), 10)
print(f"Array inicial: {array}\n")
quicksort(array, 0, len(array) - 1)
print(f"\nArray final ordenado: {array}")