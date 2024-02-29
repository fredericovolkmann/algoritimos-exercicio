def metros_quadrados_para_hectares(largura,profundidade):
    area_em_metros_quadrados = largura * profundidade
    area_em_hectares = area_em_metros_quadrados / 10000
    return area_em_hectares
def main():
    largura = float(input("Digite a largura do terreno em metros: "))
    profundidade = float(input("Digite a profundidade do terreno em metros: "))
    
    area_em_hectares = metros_quadrados_para_hectares(largura, profundidade)
    
    print("A área do terreno é de", area_em_hectares, "hectares.")

if __name__ == "__main__":
    main()
