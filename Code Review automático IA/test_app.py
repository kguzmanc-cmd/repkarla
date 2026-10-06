from app import calcular_descuento, dividir


def test_descuento():
    resultado = calcular_descuento(100, 10)
    assert resultado == 90


def test_sin_descuento():
    resultado = calcular_descuento(100, 0)
    assert resultado == 100


def test_division():
    resultado = dividir(10, 2)
    assert resultado == 5
