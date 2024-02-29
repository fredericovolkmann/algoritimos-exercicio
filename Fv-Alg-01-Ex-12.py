import math

def calcular_area_circulo(raio):
    area = math.pi * raio ** 2
    return area

def calcular_volume_esfera(raio):
    volume = (4/3) * math.pi * raio ** 3
    return volume

def main():
    raio = float(input("Digite o valor do raio (em unidades de comprimento): "))

    area_circulo = calcular_area_circulo(raio)
    volume_esfera = calcular_volume_esfera(raio)

    print("A área do círculo de raio {} é {:.2f} unidades de área.".format(raio, area_circulo))
    print("O volume da esfera de raio {} é {:.2f} unidades cúbicas.".format(raio, volume_esfera))

if __name__ == "__main__":
    main()
