grafo = {
    "poster":          {"disco-vinil": 5, "guitarra-usada": 0},
    "disco-vinil":     {"baixo": 15, "bateria": 20},
    "guitarra-usada":  {"baixo": 15, "bateria": 25},
    "baixo":           {"piano": 20},
    "bateria":         {"piano": 10},
    "piano":           {}
}

custos = {"disco-vinil": 5, "guitarra-usada": 0, "baixo": float("inf"), "bateria": float("inf"), "piano": float("inf")}
pais = {"disco-vinil": "poster", "guitarra-usada": "poster", "baixo": None, "bateria": None, "piano": None}
processados = []

def no_mais_barato():
    return min((n for n in custos if n not in processados), key=lambda n: custos[n], default=None)

no = no_mais_barato()
while no:
    for vizinho, peso in grafo[no].items():
        novo = custos[no] + peso
        if novo < custos[vizinho]:
            custos[vizinho] = novo
            pais[vizinho] = no
    processados.append(no)
    no = no_mais_barato()

print("Custo mínimo:", custos["piano"])  