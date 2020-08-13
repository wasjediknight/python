import math

def PegarEntrada(plano, coordenada):
    return float(input("Forneça a coordenada {} para o Plano {}: ".format(coordenada, plano)))

planoA = PegarEntrada("A", "X"), PegarEntrada("A", "Y")
planoB = PegarEntrada("B", "X"), PegarEntrada("B", "Y")

preCalculo = (planoA[0]-planoB[0])**2 + (planoA[1]-planoB[1])**2
distancia = math.sqrt(preCalculo)

if (distancia>=10):
    print("longe")
else:
    print("perto")
       



