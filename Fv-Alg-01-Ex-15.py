import math

def calcular_area_poligono_regular(lado, num_lados):
    area = (num_lados * lado ** 2) / (4 * math.tan(math.pi / num_lados))
    return area

def main():
    lado = float(input("Digite o comprimento de um lado do polígono regular: "))
    num_lados = int(input("Digite o número de lados do polígono regular: "))

    area = calcular_area_poligono_regular(lado, num_lados)

    print("A área do polígono regular é:", area)

if __name__ == "__main__":
    main()
4