total = 0
numeros = 0
incremento = 0

def Somar(valor):
    global total
    total += valor

def PegarEntrada(label):
    return float(input("Forneça o valor do nº{}: ".format(label)))

numeros = int(input("Digite um número inteiro: "))

while incremento < numeros:
    incremento += 1
    valor = PegarEntrada(incremento)
    Somar(valor)

print("Soma Total: {}".format(total))
