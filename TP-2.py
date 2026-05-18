# TRABAJO N°2: Realizar la Act.20 y act.24 de la guía de pilas.

# Importar la clase pila para ambas actividades.
from clase_Pila import Pila

# Act.20) Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. 
# Luego desarrolle otro algoritmo que genere la secuencia de movimientos necesarios para hacer volver 
# al robot a su lugar de partida, retornando por el mismo camino que fue.

def obtener_direccion_opuesta(direccion):
    opuestos = {
        "norte": "sur", "sur": "norte",
        "este": "oeste", "oeste": "este",
        "noreste": "suroeste", "suroeste": "noreste",
        "noroeste": "sureste", "sureste": "noroeste"
    }
    return opuestos.get(direccion.lower(), direccion)

# 1. Algoritmo para registrar movimientos del robot
pila_movimientos = Pila()

# Suponemos que el robot registra estos movimientos secuenciales:
movimientos_realizados = [
    {"pasos": 10, "direccion": "norte"},
    {"pasos": 5, "direccion": "este"},
    {"pasos": 12, "direccion": "noreste"},
]

for mov in movimientos_realizados:
    pila_movimientos.apilar(mov)

print("\n=== RESULTADOS ACTIVIDAD 20 ===")

print("\n--- Camino de Ida Registrado del Robot ---")
# Mostramos el camino original usando un clon para no destruir los datos
pila_movimientos.barrido() 

# 2. Algoritmo para generar la secuencia de retorno
def generar_secuencia_retorno(pila_original):
    pila_retorno = Pila()
    pila_aux = Pila() 
    
    # 1. Pasamos todos los movimientos de ida a la pila auxiliar.
    # Esto los invierte: el primer paso de la ida queda en la cima de pila_aux.
    while not pila_original.pila_vacia():
        pila_aux.apilar(pila_original.desapilar())
        
    # 2. Ahora vaciamos pila_aux. Esto nos da los movimientos en el orden original de ida.
    # Aprovechamos para restaurar la de ida y construir la de vuelta al mismo tiempo.
    while not pila_aux.pila_vacia():
        movimiento = paux = pila_aux.desapilar()
        
        # Devolvemos el movimiento a la pila original de ida
        pila_original.apilar(movimiento)
        
        # Creamos el movimiento inverso y lo mandamos a la de retorno.
        # Como procesamos el paso 1 primero, este va al fondo, y el paso 3 quedará en la cima.
        movimiento_inverso = {
            "pasos": movimiento["pasos"],
            "direccion": obtener_direccion_opuesta(movimiento["direccion"])
        }
        pila_retorno.apilar(movimiento_inverso)
        
    return pila_retorno

# Generamos y mostramos el camino de vuelta
pila_vuelta = generar_secuencia_retorno(pila_movimientos)

print("\n--- Secuencia de Movimientos para Volver del Robot ---")
pila_vuelta.barrido()


#-------------------------------------------------------------------------------------------------- 


# Act.24) Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

# a) determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno
# la cima de la pila;
# b) determinar los personajes que participaron en más de 5 películas de la saga, además indicar 
# la cantidad de películas en la que aparece;
# c) determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d) mostrar todos los personajes cuyos nombre empiezan con C, D y G.

# Inicialización y carga de datos de prueba
pila_mcu = Pila()

personajes = [
    {"nombre": "Iron Man", "cant_peliculas": 10},
    {"nombre": "Viuda Negra", "cant_peliculas": 8},
    {"nombre": "Thor", "cant_peliculas": 9},
    {"nombre": "Groot", "cant_peliculas": 5},
    {"nombre": "Capitan America", "cant_peliculas": 11},
    {"nombre": "Rocket Raccoon", "cant_peliculas": 6},
    {"nombre": "Doctor Strange", "cant_peliculas": 4},
]

# Apilamos los personajes (el último en entrar quedará en la cima)
for p in personajes:
    pila_mcu.apilar(p)

# Resolviendo las consignas de la actividad
def resolver_ejercicios(pila):
    pila_aux = Pila()
    posicion_actual = 1
    
    # Variables para almacenar resultados parciales
    pos_rocket = None
    pos_groot = None
    mas_de_5_peliculas = []
    peliculas_black_widow = 0
    nombres_cdg = []

    # Recorrido y vaciado controlado de la pila principal
    while not pila.pila_vacia():
        personaje = pila.desapilar()
        nombre = personaje["nombre"]
        peliculas = personaje["cant_peliculas"]
        
        # a) Determinar posición de Rocket Raccoon y Groot
        if nombre == "Rocket Raccoon":
            pos_rocket = posicion_actual
        elif nombre == "Groot":
            pos_groot = posicion_actual
            
        # b) Personajes con más de 5 películas
        if peliculas > 5:
            mas_de_5_peliculas.append((nombre, peliculas))
            
        # c) Cantidad de películas de la Viuda Negra (Black Widow)
        if nombre in ["Black Widow", "Viuda Negra"]:
            peliculas_black_widow += peliculas
            
        # d) Mostrar personajes cuyos nombres empiezan con C, D y G
        if nombre[0].upper() in ["C", "D", "G"]:
            nombres_cdg.append(nombre)
            
        # Guardamos en la pila auxiliar para no perder el elemento
        pila_aux.apilar(personaje)
        posicion_actual += 1

    # Reconstrucción de la pila original para dejarla intacta
    while not pila_aux.pila_vacia():
        pila.apilar(pila_aux.desapilar())

    # --- Presentación de Resultados ---
    print("\n=== RESULTADOS ACTIVIDAD 24 ===")
    
    print("\na) Posiciones desde la cima (1 = Cima):")
    print(f"   - Rocket Raccoon: {pos_rocket if pos_rocket else 'No encontrado'}")
    print(f"   - Groot: {pos_groot if pos_groot else 'No encontrado'}")
    
    print("\nb) Personajes con más de 5 películas:")
    for nom, cant in mas_de_5_peliculas:
        print(f"   - {nom}: {cant} películas")
        
    print(f"\nc) Cantidad de películas de la Viuda Negra: {peliculas_black_widow}")
    
    print("\nd) Personajes que empiezan con C, D o G:")
    for nom in nombres_cdg:
        print(f"   - {nom}")

# Ejecutamos la función de resolución
resolver_ejercicios(pila_mcu)

