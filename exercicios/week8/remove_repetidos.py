def remove_repetidos(lista):
	listaOrdenada = []
	listaDeNumerosUnicos = []

	for numeroCorrente in lista:
		
		if numeroCorrente not in listaDeNumerosUnicos:
			listaDeNumerosUnicos.append(numeroCorrente)

	while len(listaDeNumerosUnicos) > 0:
	
		numeroMinimo = min(listaDeNumerosUnicos)
		listaOrdenada.append(numeroMinimo)

	
		index = listaDeNumerosUnicos.index(numeroMinimo)
		del listaDeNumerosUnicos[index]

	return listaOrdenada
