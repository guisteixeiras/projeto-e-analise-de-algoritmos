from collections import deque

rede = {
    "voce": ["Claire", "Bob", "Alice"],
    "Bob": ["Peggy", "Anuj"],
    "Alice": ["Peggy"],
    "Claire": ["Jonny", "Thom"],
    "Peggy": [],
    "Anuj": [],
    "Jonny": [],
    "Thom": []
}

def e_vendedor(nome):
    return nome[-1] == "m"

def busca(nome_inicial):
    fila = deque()
    fila += rede[nome_inicial]
    verificados = []

    while fila:
        pessoa = fila.popleft()

        if pessoa not in verificados:
            if e_vendedor(pessoa):
                print(f"{pessoa} é um vendedor de mangas!")
                return True
            else:
                fila += rede[pessoa]
                verificados.append(pessoa)

    print("Nenhum vendedor encontrado.")
    return False

busca("voce")