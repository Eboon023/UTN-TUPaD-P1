# Ejercicio 1
# for x in range(101):
#     print(x)


# Ejercicio 2
# cont = 0
# num = int(input("Ingrese un numero entero: "))

# while int(num) > 0:
#     cont += 1
#     num /= 10

# print(f"El numero contiene {cont} digitos")


# Ejercicio 3
# num1 = int(input("Ingrese el numero desde donde sumar: "))
# num2 = int(input("Ingrese el numero hasta donde sumar: "))
# sum = 0

# for x in range(num1 + 1, num2):
#     sum += x

# print(f"El total de la suma de los numeros entre {num1} y {num2} es {sum}")


# Ejercicio 4
# sum = 0
# print("Ingrese numeros para sumar, para pararlo y mostrar el resultado ingrese el 0")
# num = int(input("Ingrese un numero: "))

# while num != 0:
#     sum += num
#     num = int(input("Ingrese un numero: "))

# print(f"El resultado de a suma es: {sum}")


# Ejercicio 5
# import random
# num_aleatorio = random.randint(0, 9)
# cont = 1
# num = int(input("Ingrese un numero: "))

# while num != num_aleatorio:
#     num = int(input("Intente otra vez:"))
#     cont += 1

# print(f"Usted a usado {cont} intentos para adivinar el numero {num_aleatorio}")


# Ejercicio 6
# for x in range(98, 0, -2):
#     print(x)


# Ejercicio 7
# num = int(input("Ingrtese un numero entero positivo: "))
# sum = 0

# for x in range(1, num):
#     sum += x

# print(f"La suma de los valores comprendidos entre 0 y {num} da {sum} como resultado")


# Ejercicio 8
# pos = 0
# neg = 0
# par = 0
# imp = 0

# print("Ingrtese 100 numeros a continuacion")

# for x in range(0, 100):
#     num = int(input(f"Ingrese el {x+1}° numero: "))
    
#     if num % 2 == 0:
#         par += 1
#     else:
#         imp += 1

#     if num >= 0:
#         pos += 1
#     else:
#         neg += 1

# print(f"Positivos: {pos}\nNegativos: {neg}\nPares: {par}\nImpares: {imp}")


# Ejercicio 9
# sum = 0

# print("Ingrese 100 numeros enteros")

# for x in range(0, 10):
#     num = int(input(f"Ingrese el {x+1}° numero: "))
#     sum += num

# print(f"La media de la suma es {sum/10}")



# Ejercicio 10
# num = input("Ingrese el numero a invertir: ")

# for x in range(len(num)-1, -1, -1):
#     print(num[x], end ="")