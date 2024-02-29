def calcular_area_triangulo(lado1, lado2, lado3):
    # Calcular o semiperímetro
    semiperimetro = (lado1 + lado2 + lado3) / 2
    # Calcular a área usando a fórmula de Heron
    area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5
    return area

def main():
    lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
    lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
    lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

    area = calcular_area_triangulo(lado1, lado2, lado3)

    print("A área do triângulo é:", area)

if __name__ == "__main__":
    main()
