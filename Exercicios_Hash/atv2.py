votantes = {}  

def votar(votantes, nome):
    if nome in votantes:
        print(f"Voto impedido. '{nome}' já votou.")
    else:
        votantes[nome] = True
        print(f"Voto de '{nome}' registrado com sucesso.")

def mostrar_votantes(votantes):
    print("\nPessoas que já votaram:")
    for nome in votantes:
        print(nome)

votar(votantes, "João")
votar(votantes, "Maria")
votar(votantes, "João") 
votar(votantes, "Pedro")

mostrar_votantes(votantes)