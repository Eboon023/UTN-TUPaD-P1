# Ejercicio 1
# def imprimir_hola_mundo():
#     print("Hola Mundo!")
# imprimir_hola_mundo()

# Ejercicio 2
# def saludar_usuario(nombre):
#     print(f"Hola {nombre}!")
# saludar_usuario("Marcos")

# Ejercicio 3
# def  informacion_personal(nombre, apellido,edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
# nom = input("Ingresar nombre: ")
# ape = input("Ingresar apellido: ")
# eda = input("Ingresar edad: ")
# resi = input("Ingresar lugar de reesidencia: ")
# informacion_personal(nom, ape, eda, resi)

# Ejercicio 4
# import math
# def calcular_area_circulo(radio):
#     return math.pi * (radio ** 2)
# def calcular_perimetro_circulo(radio):
#     return 2 * math.pi * radio
# rad = float(input("Ingresá el radio del círculo: "))
# print(f"\nEl área del círculo es: {calcular_area_circulo(rad):.2f}")
# print(f"El perímetro del círculo es: {calcular_perimetro_circulo(rad):.2f}")

# Ejercicio 5
# def segundos_a_horas(segundos):
#     return segundos / 3600
# seg = int(input("Ingresá la cantidad de segundos: "))
# print(f"\nEso equivale a {segundos_a_horas(seg):.2f} horas.")

# Ejercicio 6
# def tabla_multiplicar(num):
#     print(f"Tabla de multiplicar del {num}:")
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")
# tabla_multiplicar(int(input("Ingresá un número para ver su tabla de multiplicar: ")))

# Ejercicio 7
# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b if b != 0 else "No se puede dividir por cero"
#     return (suma, resta, multiplicacion, division)
# result = operaciones_basicas(int(input("Ingresá el primer número: ")), int(input("Ingresá el segundo número: ")))
# print("\nResultados de las operaciones:")
# print(f"Suma: {result[0]}")
# print(f"Resta: {result[1]}")
# print(f"Multiplicación: {result[2]}")
# print(f"División: {result[3]}")

# Ejercicio 8
# def calcular_imc(peso, altura):
#     return peso / (altura ** 2)
# print(f"\nTu índice de masa corporal (IMC) es: {calcular_imc(float(input("Ingresá tu peso en kilogramos: ")), float(input("Ingresá tu altura en metros: "))):.2f}")

# Ejercicio 9
# def celsius_a_fahrenheit(celsius):
#     return celsius * 9/5 + 32
# print(f"\nLa temperatura en Fahrenheit es: {celsius_a_fahrenheit(float(input("Ingresá la temperatura en grados Celsius: "))):.2f}°F")

# Ejercicio 10
# def calcular_promedio(a, b, c):
#     return (a + b + c) / 3
# print(f"\nEl promedio de los tres números es: {calcular_promedio(float(input("Ingresá el primer número: ")), float(input("Ingresá el segundo número: ")), float(input("Ingresá el tercer número: "))):.2f}")
def funcion_c(vector, tamanio_vector):

    max = vector[0]

    for i in range(0, tamanio_vector): 

        if vector[i] > max:

            max = vector[i]

    return max

 

tamanio_vector = 3

vector = [0] * tamanio_vector  

vector[0] = 4

vector[1] = 6

vector[2] = 1

 

print(funcion_c(vector, tamanio_vector))