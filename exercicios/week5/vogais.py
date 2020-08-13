def vogal(caractere):
    if isinstance(caractere, str):
        vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        return caractere in vogais
    return False

def test_vogais():
    assert vogal("a") == True

def test_consoantes():
    assert vogal("b") == False

def test_NaoString():
    assert vogal(1) == False
