def Fatorial(numero):
    fatorial = 1
    for numeroCorrente in range(numero, 0, -1):
        fatorial *= numeroCorrente

    return fatorial

numero = int(input("Digite o valor de n: "))
print(Fatorial(numero))
