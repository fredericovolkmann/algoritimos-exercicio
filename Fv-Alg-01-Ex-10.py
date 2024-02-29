import math

def calcular_operacoes(a, b):
    soma = a + b
    diferenca = a - b
    produto = a * b
    quociente = a / b
    resto = a % b
    resultado_penultimo = math.log10(a)
    resultado_ultimo = a ** b
    return soma, diferenca, produto, quociente, resto, resultado_penultimo, resultado_ultimo

def main():
    a = int(input("Digite o primeiro número inteiro (a): "))
    b = int(input("Digite o segundo número inteiro (b): "))

    soma, diferenca, produto, quociente, resto, resultado_penultimo, resultado_ultimo = calcular_operacoes(a, b)

    print("Soma de a e b:", soma)
    print("Diferença quando b é subtraído de a:", diferenca)
    print("Produto de a por b:", produto)
    print("Quociente quando a é dividido por b:", quociente)
    print("Resto quando a é dividido por b:", resto)
    print("Resultado de log10(a):", resultado_penultimo)
    print("Resultado de a elevado a b:", resultado_ultimo)

if __name__ == "__main__":
    main()
