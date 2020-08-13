
def maximo(numero1, numero2, numero3):
    maiorNumero = 0
    numeros = (numero1, numero2, numero3)

    for chave, numeroCorrente in enumerate(numeros):
        if numeroCorrente > maiorNumero:
            maiorNumero = numeroCorrente

    return maiorNumero


def maximoMelhorada(numeros = []):
    numeros.sort()
    return numeros[(len(numeros) - 1):len(numeros)]

def test_MaiorEntreNumerosPositivos():
    assert 101 == maximo(101, 5, 87)

def test_MaiorEntreNumerosNegativos():
    assert 0 == maximo(-5, -325, 0)

def test_MaiorEntreNumerosPositivosENegativos():
    assert 42 == maximo(-5, 0, 42)
