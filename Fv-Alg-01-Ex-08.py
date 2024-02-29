def calcular_peso_total(bugigangas, quinquilharias):
    peso_bugigangas = bugigangas * 75
    peso_quinquilharias = quinquilharias * 112
    peso_total = peso_bugigangas + peso_quinquilharias
    return peso_total

def main():
    bugigangas = int(input("Digite a quantidade de bugigangas: "))
    quinquilharias = int(input("Digite a quantidade de quinquilharias: "))

    peso_total = calcular_peso_total(bugigangas, quinquilharias)

    print("O peso total do pedido é de {} gramas.".format(peso_total))

if __name__ == "__main__":
    main()
