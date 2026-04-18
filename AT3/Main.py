from matrix import transpor_matriz, multiplicar_matriz

def main():
    print("### Testando Transposicao ###")
    A_transpor = [[1, 2], [3, 4], [5, 6]]
    
    print("Entrada:")
    print(A_transpor)
    
    saida_transposicao = transpor_matriz(A_transpor)
    
    print("\nSaida:")
    print(saida_transposicao)
    
    print("\n" + "-"*30 + "\n")
    
    print("### Testando Multiplicacao ###")
    A_mult = [[1, 2], [3, 4]]
    B_mult = [[5, 6], [7, 8]]
    
    print("Entrada A:")
    print(A_mult)
    print("Entrada B:")
    print(B_mult)
    
    saida_multiplicacao = multiplicar_matriz(A_mult, B_mult)
    
    print("\nSaida:")
    print(saida_multiplicacao)

if __name__ == "__main__":
    main()
  
