def resolver_labirinto(lab, x, y):
    if (x < 0 or x >= len(lab) or
        y < 0 or y >= len(lab[0]) or
        lab[x][y] != 0):
        return False
    
    lab[x][y] = 2
    
    if x == len(lab)-1 and y == len(lab[0])-1:
        return True
    
    if (resolver_labirinto(lab, x+1, y) or
        resolver_labirinto(lab, x, y+1) or
        resolver_labirinto(lab, x-1, y) or
        resolver_labirinto(lab, x, y-1)):
        return True
    
    lab[x][y] = 0
    return False


labirinto = [
    [0,1,0,0],
    [0,1,0,1],
    [0,0,0,1],
    [1,1,0,0]
]

if resolver_labirinto(labirinto, 0, 0):
    print("Caminho encontrado:")
else:
    print("Não existe caminho")

for linha in labirinto:
    print(linha)