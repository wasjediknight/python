
def DivisorSemResto(numero, divisor = 3):
    return True if numero % divisor == 0 else False

def fizzbuzz(numero):
    if DivisorSemResto(numero) and DivisorSemResto(numero, 5):
        return 'FizzBuzz'
    elif DivisorSemResto(numero) and not DivisorSemResto(numero, 5):
        return 'Fizz'
    elif not DivisorSemResto(numero) and DivisorSemResto(numero, 5):
        return 'Buzz'
    else:
        return numero

def test_DivisivelPorTresECinco():
    assert 'FizzBuzz' == fizzbuzz(15)

def test_DivisivelApenasPorTres():
    assert 'Fizz' == fizzbuzz(3)

def test_DivisivelApenasPorCinco():
    assert 'Buzz' == fizzbuzz(5)

def test_NaoDivisivelPorTresECinco():
    assert 4 == fizzbuzz(4)
