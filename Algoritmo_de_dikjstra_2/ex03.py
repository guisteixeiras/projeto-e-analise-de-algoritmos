import heapq

grafo = {
    'F1': {'D': 20},
    'F2': {'D': 10},
    'F3': {'D': 50},
    'F4': {'D': 30},
    'D': {}
}


def adicionar_vertice_ficticio(grafo, fornecedores):

    grafo['SUPER'] = {}

    for fornecedor in fornecedores:
        grafo['SUPER'][fornecedor] = 0


def dijkstra(grafo, origem):

    distancias = {}

    for vertice in grafo:
        distancias[vertice] = float('inf')

    distancias[origem] = 0

    fila = [(0, origem)]

    while fila:

        distancia_atual, atual = heapq.heappop(fila)

        for vizinho, peso in grafo[atual].items():

            nova_distancia = distancia_atual + peso

            if nova_distancia < distancias[vizinho]:

                distancias[vizinho] = nova_distancia

                heapq.heappush(fila, (nova_distancia, vizinho))

    return distancias


fornecedores = ['F1', 'F2', 'F3', 'F4']

adicionar_vertice_ficticio(grafo, fornecedores)

distancias = dijkstra(grafo, 'SUPER')

print("Menor custo até D:", distancias['D'])