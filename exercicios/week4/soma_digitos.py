soma = 0


def SeperarNumeros(numero):
    digitosIniciais = numero // 10
    digitoFinal = numero % 10
    return digitosIniciais, digitoFinal

numeroUsuario = int(input("Digite um número inteiro: "))
separacao = SeperarNumeros(numeroUsuario)


while sum(separacao):
    soma += separacao[1]
    separacao = SeperarNumeros(separacao[0])

print(soma)


