numeroAnterior = 0
numerosAdjacentesIguais = False


def SeperarNumeros(numero):
    digitosIniciais = numero // 10
    digitoFinal = numero % 10
    return digitosIniciais, digitoFinal

numeroUsuario = int(input("Digite um número inteiro: "))
separacao = SeperarNumeros(numeroUsuario)

while separacao[0] > 0 and not numerosAdjacentesIguais:
    numeroAnterior = separacao[1]
    separacao = SeperarNumeros(separacao[0])
    if separacao[1] == numeroAnterior:
        numerosAdjacentesIguais = True

if numerosAdjacentesIguais:
    print("sim");
else:
    print("não");
