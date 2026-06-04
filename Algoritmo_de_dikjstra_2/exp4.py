vertices = ['API', 'Cache', 'Banco', 'Fila']

arestas = [
    ('API', 'Cache', 5),
    ('Cache', 'Banco', -3),
    ('Banco', 'Fila', 2)
]


def bellman_ford(vertices, arestas, origem):

    distancias = {}

    for v in vertices:
        distancias[v] = float('inf')

    distancias[origem] = 0

    for _ in range(len(vertices) - 1):
        for u, v, peso in arestas:
            if distancias[u] != float('inf'):
                if distancias[u] + peso < distancias[v]:
                    distancias[v] = distancias[u] + peso

    for u, v, peso in arestas:
        if distancias[u] != float('inf'):
            if distancias[u] + peso < distancias[v]:
                raise Exception("Ciclo negativo detectado! Loop infinito de chamadas.")

    return distancias

try:

    resultado = bellman_ford(vertices, arestas, 'API')

    print("Menores tempos:")
    print(resultado)

except Exception as erro:

    print(erro)