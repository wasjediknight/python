def PegarEntrada():
  return int(input("Digite um número: "))


def ListaEmOrdemInversa(lista):
	listaInversa = []


	for numero in range(len(lista), 0, -1):

		listaInversa.append(lista[numero - 1])

	return listaInversa


def Main():
	lista = []
	numero = 1


	while numero != 0:
		numero = PegarEntrada()


		if numero != 0:
			lista.append(numero)


	listaInversa = ListaEmOrdemInversa(lista)


	for numero in listaInversa:
		print(numero)

Main()
