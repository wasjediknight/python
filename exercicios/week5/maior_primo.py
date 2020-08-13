def Primo(numero):
    numeroDeDivisores = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            numeroDeDivisores += 1

            if numeroDeDivisores > 2:
                return False

    return True


def maior_primo(numero):
    if numero < 2:
        return 0

    for numeroCorrente in range(numero, 2, -1):
        if Primo(numeroCorrente):
            return numeroCorrente


def test_NumerosMaioresQueUm():
    assert maior_primo(100) == 97


def test_NumerosMenoresQueDois():
    assert maior_primo(1) == 0
