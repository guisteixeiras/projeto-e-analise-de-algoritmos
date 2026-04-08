texto = """
Espante o Stress. A Casa dos Esportes tem a melhor receita para você arejar a cabeça.
Que tal uma pescaria, caçada ou acampamento? Tudo em caça, pesca e camping você encontra
na Casa dos Esportes de São Domingos. Barracas, fogareiros, anzóis, redes e tarrafas e
demais apetrechos. Fique longe do Stress. Na hora de relaxar, relaxe com os melhores preços
à vista, as melhores condições a prazo e o atendimento da Casa dos Esportes. Avenida Padre
João Maria, 1.451, telefone 215.42.44, em São Domingos.
"""

def limpar_texto(texto):
    pontuacoes = ".,!?;:-–\n"
    texto = texto.lower()

    for p in pontuacoes:
        texto = texto.replace(p, " ")

    return texto

def contar_frequencia(texto):
    texto_limpo = limpar_texto(texto)
    palavras = texto_limpo.split()

    frequencia = {} 

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia

frequencia = contar_frequencia(texto)

print("Frequência das palavras:")
for palavra, qtd in frequencia.items():
    print(f"{palavra}: {qtd}")