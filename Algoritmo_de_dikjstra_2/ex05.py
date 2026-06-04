import heapq
import time


def possui_peso_negativo(grafo):

    for u in grafo:
        for v, peso in grafo[u]:
            if peso < 0:
                return True

    return False


def dijkstra(grafo, origem):

    distancias = {}

    for v in grafo:
        distancias[v] = float('inf')

    distancias[origem] = 0

    fila = [(0, origem)]

    while fila:

        distancia_atual, atual = heapq.heappop(fila)

        for vizinho, peso in grafo[atual]:
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(fila, (nova_distancia, vizinho))

    return distancias


def bellman_ford(grafo, origem):

    distancias = {}

    for v in grafo:
        distancias[v] = float('inf')
    distancias[origem] = 0

    arestas = []

    for u in grafo:
        for v, peso in grafo[u]:
            arestas.append((u, v, peso))
    for _ in range(len(grafo) - 1):
        for u, v, peso in arestas:
            if distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso

    return distancias

def calcularRotaOtima(grafo, origem):

    if possui_peso_negativo(grafo):
        print("Usando Bellman-Ford")
        return bellman_ford(grafo, origem)
    else:
        print("Usando Dijkstra")
        return dijkstra(grafo, origem)


grafo = {}

quantidade_vertices = 1001

for i in range(quantidade_vertices):
    grafo[str(i)] = []
    if i < quantidade_vertices - 1:
        grafo[str(i)].append((str(i + 1), 1))


inicio = time.time()

resultado = calcularRotaOtima(grafo, '0')

fim = time.time()

print("Tempo de execução:", fim - inicio)