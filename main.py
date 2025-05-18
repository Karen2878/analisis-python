
def saludar(nombre):
    print("Hola " + nombre)

def dividir(a, b):
    return a / b

saludar("Mundo")

try:
    print(dividir(10, 0))
except ZeroDivisionError:
    print("Error: división por cero")
