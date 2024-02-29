def calcular_total(suco, prato_principal, sobremesa):
    subtotal = suco + prato_principal + sobremesa
    taxa_servico = subtotal * 0.10
    total = subtotal + taxa_servico
    return total

def main():
    suco = float(input("Digite o preço do suco: R$ "))
    prato_principal = float(input("Digite o preço do prato principal: R$ "))
    sobremesa = float(input("Digite o preço da sobremesa: R$ "))

    valor_total = calcular_total(suco, prato_principal, sobremesa)

    print("O valor total da conta é de R$ {:.2f}".format(valor_total))

if __name__ == "__main__":
    main()
