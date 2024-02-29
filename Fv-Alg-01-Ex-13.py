def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def main():
    base = float(input("Digite o comprimento da base do triângulo: "))
    altura = float(input("Digite o comprimento da altura do triângulo: "))

    area = calcular_area_triangulo(base, altura)

    print("A área do triângulo é:", area)

if __name__ == "__main__":
    main()
