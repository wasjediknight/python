def Entrada():
    return int(input("digite: "))

def Retangulo(dimensoes):
    largura, altura = dimensoes
    preencher = 1

    while preencher <= altura:
        preencherHorizontal = 1

        while preencherHorizontal <= largura:
            print("#", end="")
            preencherHorizontal += 1

        print("")
        preencher += 1

def Main():
    dimensoes = (Entrada(), Entrada())
    Retangulo(dimensoes)

Main()
