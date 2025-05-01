# Ejercicio 1
#edad = int(input("Ingrese su edad: "))
#if edad > 18 :
#    print("Es mayor de edad")

# Ejercicio 2
# nota = int(input("Ingrese su nota: "))
# if nota >= 6 :
#     print("Aprobado")
# else:
#     print("Desaprobado")

# Ejercicio 3
# num = int(input("Ingrese un numero par: "))
# if num % 2 == 0 :
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")

# Ejercicio 4
# edad = int(input("Ingrese su edad: "))
# print("Pertenece a la categoria de edad: ", end="")
# if edad < 12 :
#     print("Niño/a")
# elif edad >= 12 and edad < 18 :
#     print("Adolecente")
# elif edad >= 18 and edad < 30 :
#     print("Adulto/a Joven")
# else:
#     print("Adulto/a")

# Ejercicio 5
# contrasenia = len(input("Ingrese una contraseña: "))
# if contrasenia < 8 or contrasenia >14 :
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# else:
#     print("Ha ingresado una contraseña correcta")

# Ejercicio 6
# from statistics import mode, median, mean
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# print(f"{numeros_aleatorios} \n {mean(numeros_aleatorios)} \n {median(numeros_aleatorios)} \n {mode(numeros_aleatorios)}")

# if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
#     print("Sesgo positivo o a la derecha")
# elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
#     print("Sesgo negativo o a la izquierda")
# elif mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios):
#     print("Sin sesgo")

# Ejercicio 7
# frase = input("Ingrese un frase: ")

# if frase[-1] in "aeiouAEIOU":
#     frase = frase + "!"

# print(frase)

# Ejercicio 8
# nombre = input("Ingrese su nombre: ")

# num = int(input("Ingrese el numero corespondiente a su elección: \n1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro\n"))

# if num == 1:
#     print(nombre.upper())
# elif num == 2:
#     print(nombre.lower())
# elif num == 3:
#     print(nombre.title())
# else:
#     print("Opcion no correspondiente")

# Ejercicio 9
# magnitud = int(input("Por favor ingrese la magnitud del terremoto: "))

# if magnitud < 3:
#     print("Muy leve (imperceptible)")
# elif magnitud >= 3 and magnitud < 4:
#     print("Leve (ligeramente perceptible)")
# elif magnitud >= 4 and magnitud < 5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños)")
# elif magnitud >= 5 and magnitud < 6:
#     print("Fuerte (puede causar daños en estructuras débiles)")
# elif magnitud >= 6 and magnitud < 7:
#     print("Muy Fuerte (puede causar daños significativos)")
# elif magnitud >= 7:
#     print("Extremo (puede causar graves daños a gran escala)")

# # Ejercicio 10
# em = input("indique en que hemisferio se encuentra (S/N): ").lower()

# mes = input("Indique en que mes se encuentra: ").lower()

# dia = int(input("Indique el numero de dia que es: "))

# if dia >= 0 and dia <= 31:
#     if em == "s":
#         if mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20) or (mes == "diciembre" and dia >= 21):
#             print("Usted esta en Verano")
#         elif mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20) or (mes == "marzo" and dia >= 21):
#             print("Usted esta en Otoño")
#         elif mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20) or (mes == "junio" and dia >= 21):
#             print("Usted esta en Invierno")
#         elif mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20) or (mes == "septiembre" and dia >= 21):
#             print("Usted esta en Primavera")
#         else:
#             print("Datos ingrasados incorrectos")
#     elif em == "n":
#         if mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20) or (mes == "diciembre" and dia >= 21):
#             print("Usted esta en Invierno")
#         elif mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20) or (mes == "marzo" and dia >= 21):
#             print("Usted esta en Primavera")
#         elif mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20) or (mes == "junio" and dia >= 21):
#             print("Usted esta en Verano")
#         elif mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20) or (mes == "septiembre" and dia >= 21):
#             print("Usted esta en Otoño")
#         else:
#             print("Datos ingrasados incorrectos")
#     else:
#         print("Datos ingrasados incorrectos")
# else:
#     print("Datos ingrasados incorrectos")