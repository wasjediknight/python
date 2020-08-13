import math

def Entrada(label):
    return int(input("Entrada {}: ".format(label)))

def Bhaskara(a, b, c):
    delta = (b**2) - (4*a*c)

    if delta >= 0:
        raizes = (-b + math.sqrt(delta)) / (2*a), (-b - math.sqrt(delta)) / (2*a)
        raizesEmOrdem = tuple(sorted(raizes))

        if delta > 0:
            return "as raízes da equação são {} e {}".format(raizesEmOrdem[0], raizesEmOrdem[1])
        else:
            return "a raiz desta equação é {}".format(raizes[0])
    else:
        return "esta equação não possui raízes reais"


entradas = Entrada("A"), Entrada("B"), Entrada("C")
print(Bhaskara(entradas[0], entradas[1], entradas[2]))


