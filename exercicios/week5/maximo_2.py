def maximo(numero1, numero2):
    return max(numero1, numero2)

def test_NumPositivo():
    assert maximo(3, 4) == 4

def test_NumNegativo():
    assert maximo(0, -1) == 0
