import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    # Converter graus para radianos
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calcular distância usando a fórmula fornecida
    distancia = 6371.01 * math.acos(math.sin(lat1_rad) * math.sin(lat2_rad) + 
                                     math.cos(lat1_rad) * math.cos(lat2_rad) * 
                                     math.cos(lon1_rad - lon2_rad))
    return distancia

def main():
    # Receber latitude e longitude dos dois pontos
    lat1 = float(input("Digite a latitude do primeiro ponto em graus: "))
    lon1 = float(input("Digite a longitude do primeiro ponto em graus: "))
    lat2 = float(input("Digite a latitude do segundo ponto em graus: "))
    lon2 = float(input("Digite a longitude do segundo ponto em graus: "))

    # Calcular a distância entre os dois pontos
    distancia = calcular_distancia(lat1, lon1, lat2, lon2)

    # Exibir a distância
    print("A distância entre os pontos é de {:.2f} quilômetros.".format(distancia))

if __name__ == "__main__":
    main()
