def calcular_saldo_investimento(valor_inicial, anos):
    taxa_juros = 0.12
    saldo = valor_inicial * (1 + taxa_juros) ** anos
    return saldo

def main():
    valor_inicial = float(input("Digite o valor inicial depositado na conta: R$ "))

    for anos in range(1, 4):
        saldo = calcular_saldo_investimento(valor_inicial, anos)
        print("Saldo após {} ano(s): R$ {:.2f}".format(anos, saldo))

if __name__ == "__main__":
    main()
