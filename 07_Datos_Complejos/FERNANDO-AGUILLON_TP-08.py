# Ejercicio 1, 2 y 3
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300
# print(precios_frutas)

# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800
# print(precios_frutas)

# frutas = list(precios_frutas.keys())
# print(frutas)

# Ejercicio 4
# agenda = {}
# for i in range(5):
#     nombre = input(f"Ingrese el nombre del contacto #{i+1}: ")
#     numero = input(f"Ingrese el número telefónico de {nombre}: ")
#     agenda[nombre] = numero

# consulta = input("Ingrese el nombre del contacto que desea consultar: ")

# if consulta in agenda:
#     print(f"El número de {consulta} es: {agenda[consulta]}")
# else:
#     print(f"No se encontró el contacto con nombre '{consulta}'.")

# Ejercicio 5
# frase = input("Ingresa una frase: ").split()

# palabras_unicas = set(frase)
# print("Palabras únicas:", palabras_unicas)

# frecuencia = {}
# for palabra in frase:
#     frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# print("Frecuencia de palabras:", frecuencia)

# Ejercicio 6
# alumnos = {}
# for i in range(3):
#     nombre = input(f"Ingresá el nombre del alumno #{i+1}: ")
#     print(f"Ingresá las 3 notas de {nombre} separadas por espacios:")
#     notas_str = input()
#     notas = tuple(map(float, notas_str.split()))
#     alumnos[nombre] = notas

# for nombre, notas in alumnos.items():
#     promedio = sum(notas) / len(notas)
#     print(f"{nombre} tiene un promedio de {promedio:.2f}")

# Ejercicio 7
# parcial1 = {'Raul', 'Estella', 'Fernando', 'Joaquin'}
# parcial2 = {'Fernando', 'Zulma', 'Raul', 'Maria'}

# ambos = parcial1 & parcial2
# solo_uno = parcial1 ^ parcial2
# al_menos_uno = parcial1 | parcial2

# print("Aprobaron ambos parciales:", ambos)
# print("Aprobaron solo uno de los dos parciales:", solo_uno)
# print("Aprobaron al menos un parcial:", al_menos_uno)

# Ejercicio 8
# stock_productos = {
#     'Yoghurt': 50,
#     'Queso': 10,
#     'Pan': 40
# }

# producto = "algo"

# while True:
#     producto = input("Ingrese el nombre del producto a consultar o agregar(o presionar ENTER para salir): ").title()

#     if producto == "": break
     
#     if producto in stock_productos:
#         print(f"Stock actual de {producto}: {stock_productos[producto]} unidades")
#         agregar = input("¿Desea agregar unidades a este producto? (s/n): ").lower()
#         if agregar == 's':
#             cantidad = int(input("Ingrese la cantidad a agregar: "))
#             stock_productos[producto] += cantidad
#             print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
#     else:
#         print(f"{producto} no está en el inventario.")
#         nuevo = input("¿Desea agregar este nuevo producto? (s/n): ").lower()
#         if nuevo == 's':
#             cantidad = int(input(f"Ingrese el stock inicial para {producto}: "))
#             stock_productos[producto] = cantidad
#             print(f"{producto} agregado con {cantidad} unidades.")

# print("\nStock actual:")
# for prod, cantidad in stock_productos.items():
#     print(f"{prod}: {cantidad} unidades")

# Ejercicio 9
# agenda = {
#     ("Lunes", "10:00") : "Reunion",
#     ("Martes", "12:00") : "Clases de ingles",
#     ("Miercoles", "20:00") : "Paricial de Quimica",
#     ("Domingo", "13:30") : "Almuerzo familiar"
# }

# dia_consulta = input("Ingresá el día que querés consultar: ").title()
# hora_consulta = input("Ingresá la hora que querés consultar: ")

# if (dia_consulta, hora_consulta) in agenda:
#     print(f"En {dia_consulta} a las {hora_consulta} tenés: {agenda[(dia_consulta, hora_consulta)]}")
# else:
#     print(f"No hay eventos registrados para {dia_consulta} a las {hora_consulta}.")

# Ejercicio 10
paises_a_capitales = {
    'Italia': 'Roma',
    'Canadá': 'Ottawa',
    'Australia': 'Canberra',
    'México': 'Ciudad de México',
    'Egipto': 'El Cairo',
    'Sudáfrica': 'Pretoria',
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Francia': 'París',
    'Japón': 'Tokio',
    'España': 'Madrid',
    'Alemania': 'Berlín'
}

capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()}

print(capitales_a_paises)
