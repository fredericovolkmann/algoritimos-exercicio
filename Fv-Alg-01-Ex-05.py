def calcular_creditos(vasilhames_pequenos, vasilhames_grandes):
    valor_creditos_pequenos = vasilhames_pequenos * 0.10
    valor_creditos_grandes = vasilhames_grandes * 0.25
    valor_total = valor_creditos_pequenos + valor_creditos_grandes
    return valor_total

def main():
    vasilhames_pequenos = int(input("Digite a quantidade de vasilhames de 1 litro ou menos: "))
    vasilhames_grandes = int(input("Digite a quantidade de vasilhames de mais de 1 litro: "))

    valor_total_creditos = calcular_creditos(vasilhames_pequenos, vasilhames_grandes)

    print("O valor total dos créditos é de R$ {:.2f}".format(valor_total_creditos))

if __name__ == "__main__":
    main()
