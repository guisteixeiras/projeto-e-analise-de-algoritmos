from collections import deque

grafo = {
    "Twin Peaks": ["Parada 2", "Parada 3"],
    "Parada 2": ["Parada 3", "Parada 4"],
    "Parada 3": ["Parada 4", "Parada 5"],
    "Parada 4": ["Parada 6", "Parada 5"],
    "Parada 5": ["Parada 6"],
    "Parada 6": ["Golden Gate"],
    "Golden Gate": []
}

def menor_caminho(grafo, inicio, destino):
    fila = deque([(inicio, 0)])
    verificados = []

    while fila:
        parada, distancia = fila.popleft()

        if parada not in verificados:
            if parada == destino:
                print(f"Caminho mais curto: {distancia} etapas")
                return distancia

            verificados.append(parada)
            for vizinho in grafo[parada]:
                fila.append((vizinho, distancia + 1))

    print("Destino não encontrado.")
    return -1

menor_caminho(grafo, "Twin Peaks", "Golden Gate")