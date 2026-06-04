vertices = ['ouro', 'gema', 'espada']

arestas = [
    ('ouro', 'gema', 1),
    ('gema', 'espada', -2),
    ('espada', 'ouro', -2)
]

def bellman_ford(vertices, arestas, origem):

    distancias = {}
    pai = {}

    for v in vertices:
        distancias[v] = float('inf')
        pai[v] = None
        
    distancias[origem] = 0

    for _ in range(len(vertices) - 1):
        for u, v, peso in arestas:
            if distancias[u] != float('inf'):
                if distancias[u] + peso < distancias[v]:
                    distancias[v] = distancias[u] + peso
                    pai[v] = u

    ciclo = None

    for u, v, peso in arestas:
        if distancias[u] != float('inf'):
            if distancias[u] + peso < distancias[v]:
                ciclo = v
                break

    if ciclo is not None:
        for _ in range(len(vertices)):
            ciclo = pai[ciclo]
        caminho_ciclo = []
        atual = ciclo

        while True:
            caminho_ciclo.append(atual)
            atual = pai[atual]
            if atual == ciclo:
                caminho_ciclo.append(ciclo)
                break
        caminho_ciclo.reverse()
        print("Ciclo negativo encontrado:")
        print(caminho_ciclo)
    else:
        print("Nenhum ciclo negativo encontrado")


bellman_ford(vertices, arestas, 'ouro')