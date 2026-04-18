def transpor_matriz(matriz):
    if not matriz:
        return []
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    matriz_transposta = [[0 for _ in range(linhas)] for _ in range(colunas)]
    
    for i in range(linhas):
        for j in range(colunas):
            matriz_transposta[j][i] = matriz[i][j]
            
    return matriz_transposta

def multiplicar_matriz(matriz_a, matriz_b):
    if not matriz_a or not matriz_b:
        return None
    
    colunas_a = len(matriz_a[0])
    linhas_b = len(matriz_b)
    
    if colunas_a != linhas_b:
        return "Erro: O numero de colunas da matriz A nao e igual ao número de linhas da matriz B"
    
    linhas_a = len(matriz_a)
    colunas_b = len(matriz_b[0])
    
    matriz_resultante = [[0 for _ in range(colunas_b)] for _ in range(linhas_a)]
    
    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]
                
    return matriz_resultante
