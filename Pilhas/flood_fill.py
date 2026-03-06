def flood_fill(matriz, x, y, cor_antiga, cor_nova):
    if (x < 0 or x >= len(matriz) or
        y < 0 or y >= len(matriz[0]) or
        matriz[x][y] != cor_antiga):
        return
    
    matriz[x][y] = cor_nova
    
    flood_fill(matriz, x+1, y, cor_antiga, cor_nova)
    flood_fill(matriz, x-1, y, cor_antiga, cor_nova)
    flood_fill(matriz, x, y+1, cor_antiga, cor_nova)
    flood_fill(matriz, x, y-1, cor_antiga, cor_nova)


matriz = [
    [1,1,1,2],
    [1,1,0,2],
    [1,0,1,2]
]

flood_fill(matriz, 0, 0, 1, 9)

for linha in matriz:
    print(linha)