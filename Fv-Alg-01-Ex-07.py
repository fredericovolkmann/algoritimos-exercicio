def soma_n_primeiros_numeros(n):
    soma = (n * (n + 1)) / 2
    return soma

def main():
    n = int(input("Digite um número inteiro positivo: "))
    
    if n <= 0:
        print("O número precisa ser positivo.")
    else:
        resultado = soma_n_primeiros_numeros(n)
        print("A soma dos {} primeiros números inteiros é: {}".format(n, resultado))

if __name__ == "__main__":
    main()
-3