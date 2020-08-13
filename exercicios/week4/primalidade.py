def EsteNumeroEPrimo(numero):
    numeroDeDivisores = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            numeroDeDivisores += 1

            if numeroDeDivisores > 2:
                return False

    return True

numero = int(input("Digite um número inteiro: "))
print("primo" if EsteNumeroEPrimo(numero) else "não primo")
