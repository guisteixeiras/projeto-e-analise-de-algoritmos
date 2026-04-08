numeros = [1, 2, 2, 3, 4, 5, 6, 66, 7, 8, 9, 99]

def numeros_unicos(lista):
    vistos = {}   
    resultado = []

    for numero in lista:
        if numero not in vistos:
            vistos[numero] = True
            resultado.append(numero)

    return resultado

resultado = numeros_unicos(numeros)
print("Números únicos:", resultado)