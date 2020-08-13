def EsteNumeroEPrimo(numero):
    numeroDeDivisores = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            numeroDeDivisores += 1

            if numeroDeDivisores > 2:
                return False

    return True

def ContarNumerosPrimos(numeroInicial, numeroFinal):
    quantidadeDeNumerosPrimos = 0

    for numeroCorrente in range(numeroInicial, numeroFinal + 1):
        if EsteNumeroEPrimo(numeroCorrente):
            quantidadeDeNumerosPrimos += 1

    return quantidadeDeNumerosPrimos

def n_primos(numero):
    return ContarNumerosPrimos(2, numero)
