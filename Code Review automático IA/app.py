def calcular_descuento(precio, descuento):
    resultado = precio - (precio * descuento / 100)
    return resultado


def registrar_usuario(nombre, edad):
    if edad > 18:
        print("Usuario registrado")
    return True


def dividir(a, b):
    return a / b
