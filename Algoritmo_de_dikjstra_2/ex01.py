import heapq

grafo = {
    'Manhuaçu': {
        'João Monlevade': 120,
        'Ouro Preto': 180
    },

    'João Monlevade': {
        'Manhuaçu': 120,
        'Belo Horizonte': 100
    },

    'Ouro Preto': {
        'Manhuaçu': 180,
        'Belo Horizonte': 90
    },

    'Belo Horizonte': {
        'João Monlevade': 100,
        'Ouro Preto': 90
    }
}


def dijkstra(grafo, origem, destino):

    distancias = {}
    anteriores = {}

    for vertice in grafo:
        distancias[vertice] = float('inf')
        anteriores[vertice] = None

    distancias[origem] = 0

    fila = [(0, origem)]

    while fila:

        distancia_atual, atual = heapq.heappop(fila)

        if atual == destino:
            break

        for vizinho, peso in grafo[atual].items():

            nova_distancia = distancia_atual + peso

            if nova_distancia < distancias[vizinho]:

                distancias[vizinho] = nova_distancia
                anteriores[vizinho] = atual

                heapq.heappush(fila, (nova_distancia, vizinho))

    caminho = []

    atual = destino

    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]
    caminho.reverse()
    return distancias[destino], caminho

def bloquear_aresta(grafo, cidade1, cidade2):
    if cidade2 in grafo[cidade1]:
        del grafo[cidade1][cidade2]
    if cidade1 in grafo[cidade2]:
        del grafo[cidade2][cidade1]


tempo, rota = dijkstra(grafo, 'Manhuaçu', 'Belo Horizonte')

print("Tempo mínimo:", tempo)
print("Rota:", rota)
print("\n--- Bloqueando estrada ---\n")
bloquear_aresta(grafo, 'João Monlevade', 'Belo Horizonte')
tempo, rota = dijkstra(grafo, 'Manhuaçu', 'Belo Horizonte')
print("Novo tempo mínimo:", tempo)
print("Nova rota:", rota)