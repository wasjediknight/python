import math

def CatetosInteiros(hipotenusa):
    incremento = 1

    while incremento < hipotenusa:
      
        cateto = (hipotenusa ** 2) - (incremento ** 2)

    
        if cateto > 0:
            cateto = math.sqrt(cateto)

          
            if cateto % 1 == 0:
                return True

        incremento += 1

    return False


def soma_hipotenusas(numero):
    hipotenusas = []
    hipotenusa = 1

    while hipotenusa <= numero:
       
        if CatetosInteiros(hipotenusa):
            hipotenusas.append(hipotenusa)

        hipotenusa += 1

    
    return sum(hipotenusas)
