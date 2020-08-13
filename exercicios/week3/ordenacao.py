def PegarEntrada(label):
    return int(input("{} Informe um número inteiro: ".format(label)))

numeros = PegarEntrada("A"), PegarEntrada("B"), PegarEntrada("C")
numerosOrdenados = tuple(sorted(numeros))

print("crescente" if numeros == numerosOrdenados else "não está em ordem crescente")
