def parenteses_balanceados(expressao):
    pilha = []
    
    for caractere in expressao:
        if caractere == "(":
            pilha.append(caractere)
        elif caractere == ")":
            if not pilha:
                return False
            pilha.pop()
    
    return len(pilha) == 0

print(parenteses_balanceados("(2 + 3) * (5 - 1)")) 
print(parenteses_balanceados("(2 + 3 * (5 - 1)")) 