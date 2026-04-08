numeros = [2, 3, 4, 7, 11, 15]

def encontrar_pares(lista, alvo):
    vistos = {} 
    pares = []

    for numero in lista:
        complemento = alvo - numero

        if complemento in vistos:
            pares.append((complemento, numero))

        vistos[numero] = True

    return pares

alvos = [6, 9, 20]

for alvo in alvos:
    pares = encontrar_pares(numeros, alvo)
    print(f"Alvo {alvo}: {pares}")