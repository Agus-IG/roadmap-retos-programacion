# #02 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
#Variable Global
global_variable = "Soy Global"

# Función Simple
def saludo():
    print('¡¡Hola, Soy Jesus!!')
saludo()

# Función con Parámetro
def personalizar_Saludo(nombre):
    print(f"¡¡Hola, Mundo soy {nombre}!!")
personalizar_Saludo("Antonio")

# Función varios Parámetros
def suma(a, b):
    print(f"La suma de {a} y {b} es de {a + b}")
suma(5, 6)

# Función con Retorno
def multiplicar(a, b):
    return a * b
resultado = multiplicar(3, 4)
print(f"El resultado de la multiplicación es {resultado}")

# Función dentro de otra Función
def compleja(x, y):
    def restar(a, b):
        return a - b
    def dividir(a, b):
        if(b != 0):
            return b / a
    resta = restar(x, y)
    residuo = dividir(y, x)
    return resta, residuo
resta, residuo = compleja(8,4)
print(f"La resta es {resta} y el residuo es {residuo}")

# Variables Globales y Locales
def my_function():
    local_variable = "Soy Local"
    print(local_variable)
    print(global_variable)
my_function()



"""
EXTRA
"""
