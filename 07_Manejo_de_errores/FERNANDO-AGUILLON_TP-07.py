# Ejercicio 1
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# num = int(input("Ingresá un número entero positivo: "))

# print(f"\nFactoriales del 1 al {num}:")
# for i in range(1, num + 1):
#     print(f"{i}! = {factorial(i)}")

# Ejercicio 2
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# pos = int(input("Ingresá una posición para mostrar la serie de Fibonaci hasta ahí: "))

# print(f"\nSerie de Fibonacci hasta la posición {pos}:")
# for i in range(pos + 1):
#     print(f"Fibonacci({i}) = {fibonacci(i)}")

# Ejercicio 3
# def potencia(n, m):
#     if m == 0:
#         return 1
#     else:
#         return n * potencia(n, m - 1)

# num = int(input("Ingrese el numero base: "))
# pot = int(input("Ingrese la potencia a la que quiere elevarlo: "))

# print("El resultado es: ", potencia(num, pot))

# Ejercicio 4
# def dec_a_bin(dec):
#     if dec == 1:
#         return "1"
#     else:
#         return str(dec_a_bin(dec // 2)) + str(dec % 2)

# print(dec_a_bin(int(input("Ingrese el numero a convertir a binario: "))))

# Ejercicio 5
# def es_palindromo(palabra):
#     if len(palabra) <= 2:
#         return print("Es palindromo")
#     else:
#         if palabra[0] == palabra[-1]:
#             return es_palindromo(palabra[1:-2])
#         else:
#             return print("No es palindromo")

# es_palindromo(input("Ingrese la palabra para comprobar si es palindromo: "))

# Ejercicio 6
# def suma_digitos(n):
#     if n < 10:
#         return n
#     else:
#         return suma_digitos(n // 10) + (n % 10)

# print(suma_digitos(int(input("Ingrese el numero a sumar sus digitos: "))))  

# Ejercicio 7
# def contar_bloques(n):
#     if n == 1:
#         return 1
#     else:
#         return n + contar_bloques(n - 1)

# print(f"La cantidad de bloques a ocupar es de {contar_bloques(int(input("Ingrese la cantidad de pisos de la piramide: ")))}")

# Ejercicio 8
def contar_digito(n, d):
    if n == 0:
        return 0
    else:
        resto = n % 10
        if resto == d:
            return 1 + contar_digito(n // 10, d)
        else:
            return contar_digito(n // 10, d)

num = int(input("Ingresá un número entero positivo: "))
digito = int(input("Ingresá un dígito del 0 al 9: "))

if num >= 0 and 0 <= digito <= 9:
    print(f"\nEl dígito {digito} aparece {contar_digito(num, digito)} veces en el número {num}.")
else:
    print("No es un número positivo y/o un dígito válido entre 0 y 9.")
