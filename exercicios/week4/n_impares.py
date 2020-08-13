incremento = 1
primeirosNumeros = []

quantidadeDeNumeros = int(input("Digite o valor de n: "))

while len(primeirosNumeros) < quantidadeDeNumeros:
    if incremento % 2 > 0:
        primeirosNumeros.append(incremento)
        print(incremento)
    incremento += 1
