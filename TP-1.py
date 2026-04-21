##TRABAJO N°1: Realizar la Act.5 y act.22 de la guía de recursividad.

##Act.5) Desarrollar una función que permita convertir un número romano en un número decimal.

## def romano_Decimal(romano: str) -> int:

##     Función para convertir valores romanos en decimales
#     def valor_decimal(valor: str) -> int:
#         if valor == 'I': return 1
#         if valor == 'V': return 5
#         if valor == 'X': return 10
#         if valor == 'L': return 50
#         if valor == 'C': return 100
#         if valor == 'D': return 500
#         if valor == 'M': return 1000
#         return 0
    
##     Caso Base - no se ingreso nada
#     if not romano:
#         return 0
    
##     Caso Base - num. romano de tamaño 1
#     if len(romano) == 1:
#         return valor_decimal(romano[0])
    
#     Actual: int = valor_decimal(romano[0])
#     Siguiente: int = valor_decimal(romano[1])

#     if Actual < Siguiente:
#         return -Actual + romano_Decimal(romano[1:])
#     elif Actual >= Siguiente:
#         return Actual + romano_Decimal(romano[1:])

## Escribir Número romano
# print ('Valores Romanos a Decimales: ')
# print ('(Nada): ',romano_Decimal(''))
# print ('(V): ',romano_Decimal('XV'))
# print ('(VII): ',romano_Decimal('VII'))
# print ('(IV): ',romano_Decimal('IV'))


# #Act.22) El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, etc) 
# está atrapado, pero muy cerca está su mochila que contiene muchos objetos. 
# Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi 
# “con ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar 
# para encontrarlo;
# c. Utilizar un vector para representar la mochila.

## Función para buscar el sable laser
# def usar_la_fuerza(mochila, objetos_sacados = 0):
    
##     Caso Base - La mochila no posee el sable de luz
#     if not mochila:
#         return False, objetos_sacados
    

#     objeto_actual = mochila.pop()
#     objetos_sacados += 1

#     print(f"El siguiente objeto se saco de la mochila: {objeto_actual}")

##     Caso Base - La mochila posee el sable de luz
#     if objeto_actual.lower() == "sable de luz":
#         return True, objetos_sacados

#     return usar_la_fuerza(mochila, objetos_sacados)

## Objetos de la mochila
# mochila_jedi = ["Raciones", "Cantimplora", "Capa", "Sable de Luz", "Yoda", "Créditos"]

# print('El Jedi utiliza la fuerza: ')

# encontrado, cantidad = usar_la_fuerza(mochila_jedi)

# if encontrado:
#     print(f"El sable fue hallado tras sacar {cantidad} objetos.")
# else:
#     print(f"El sable no estaba en la mochila. Se sacaron {cantidad} objetos.")