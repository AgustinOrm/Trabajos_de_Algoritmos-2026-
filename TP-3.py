# TRABAJO N°3: Realizar la Act.10 y act.22 de la guía de Cola. (La act.16 dejarla pendiente.)

# Act.10) Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

# Importamos los Tda de Pila y Cola.
from tda_cola import Cola, arribo, atencion, tamanio
from tda_pila import Pila, apilar, tamanio as tamanio_pila


# Punto a) Función que elimine de la cola todas las notificaciones de Facebook
# def eliminar_notificaciones_facebook(cola_notif):

#     # Obtenemos la cantidad exacta de elementos originales en la cola.
#     num_elementos = tamanio(cola_notif)
    
#     # Iteramos sobre la cantidad de elementos originales.
#     for _ in range(num_elementos):
#         # Extraemos el elemento que está en el frente de la cola.
#         notificacion = atencion(cola_notif)
        
#         # Si la aplicación que emitió la notificación 'NO' es Facebook:
#         if notificacion['app'] != 'Facebook':
#             # La volvemos a insertar al final de la cola para conservarla.
#             arribo(cola_notif, notificacion)
#         # Si 'ES' de Facebook, no hacemos nada.


# # Punto b) Función que muestre notificaciones de Twitter con la palabra 'Python'
# def mostrar_twitter_python(cola_notif):

#     # Obtenemos el tamaño para asegurar un barrido sin ciclos infinitos.
#     num_elementos = tamanio(cola_notif)
    
#     print("--- Notificaciones de Twitter sobre Python ---")
#     for _ in range(num_elementos):
#         # Atendemos el elemento del frente.
#         notificacion = atencion(cola_notif)
        
#         # Evaluamos ambas condiciones exigidas en el enunciado.
#         # 1) Que la app sea Twitter.
#         # 2) Que el mensaje incluya 'Python'.
#         if notificacion['app'] == 'Twitter' and 'Python' in notificacion['mensaje']:
#             print(f"[{notificacion['hora']}] {notificacion['mensaje']}")
            
#         # Para no perder los datos, la reinsertamos al final.
#         arribo(cola_notif, notificacion)


# # Punto c) Pila temporal para notificaciones entre las 11:43 y las 15:57
# def contar_notificaciones_por_horario(cola_notif):

#     # Creamos la pila para almacenar temporalmente los datos.
#     pila_temporal = Pila()
#     num_elementos = tamanio(cola_notif)
    
#     for _ in range(num_elementos):
#         # Extraemos la notificación del frente de la cola.
#         notificacion = atencion(cola_notif)
        
#         # Con operadores lógicos para determinar rangos de tiempo.
#         if "11:43" <= notificacion['hora'] <= "15:57":
#             # Si entra en el rango, la apilamos temporalmente en la estructura auxiliar.
#             apilar(pila_temporal, notificacion)
            
#         # Reinsertamos a la cola para mantener su estado original.
#         arribo(cola_notif, notificacion)
        
#     # Usamos el método del TDA_Pila que nos devuelve la cantidad de elementos.
#     cantidad_en_rango = tamanio_pila(pila_temporal)
#     print(f"\nCantidad de notificaciones entre las 11:43 y las 15:57: {cantidad_en_rango}")
    
#     return cantidad_en_rango


# # Prueba del Código:
# if __name__ == "__main__":

#     # Instanciamos la cola y cargamos datos de prueba:
#     mi_smartphone = Cola()
    
#     arribo(mi_smartphone, {'hora': '10:15', 'app': 'Facebook', 'mensaje': 'Juan comentó "Me gusta Python".'})
#     arribo(mi_smartphone, {'hora': '12:00', 'app': 'Twitter', 'mensaje': 'Nuevo curso de Java disponible.'})
#     arribo(mi_smartphone, {'hora': '14:30', 'app': 'Instagram', 'mensaje': 'A María le gusta tu reel.'})
#     arribo(mi_smartphone, {'hora': '15:10', 'app': 'Twitter', 'mensaje': 'Tendencia: #Curso de Python 2026'})
#     arribo(mi_smartphone, {'hora': '16:05', 'app': 'Facebook', 'mensaje': 'Tienes 3 nuevas sugerencias de amistad.'})
#     arribo(mi_smartphone, {'hora': '18:20', 'app': 'WhatsApp', 'mensaje': 'Mamá: ¿A qué hora llegas?'})

#     print(f"Total notificaciones iniciales: {tamanio(mi_smartphone)}\n")

#     # Test a) Probar eliminación de Facebook
#     eliminar_notificaciones_facebook(mi_smartphone)
#     print(f"Total notificaciones tras eliminar Facebook: {tamanio(mi_smartphone)}\n")

#     # Test b) Probar muestra de Twitter + 'Python'
#     mostrar_twitter_python(mi_smartphone)

#     # Test c) Probar el uso de la pila temporal y conteo
#     contar_notificaciones_por_horario(mi_smartphone)



# Act.22)  Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales 
# se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, 
# {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes 
# actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

#Función que recorre la cola de personajes de Marvel una sola vez y resuelve todas las consignas 
# pedidas sin perder los datos.
def analizar_personajes_marvel(cola_mcu):

    # Obtenemos la cantidad de elementos para hacer un barrido.
    num_elementos = tamanio(cola_mcu)
    
    # Variables auxiliares para ir guardando los resultados de cada punto:
    # a)
    nombre_capitana_marvel = None
    # b)
    superheroes_femeninos = []
    # c)
    personajes_masculinos = []
    # d)
    superheroe_scott_lang = None
    # e)
    nombres_con_s = []
    # f)
    carol_danvers_encontrada = False
    superheroe_carol_danvers = None

    # Iniciamos el barrido cíclico
    for i in range(num_elementos):
        # Sacamos el primer elemento del frente de la cola.
        personaje = atencion(cola_mcu)
        
        # a) Determinar el nombre del personaje de Capitana Marvel
        if personaje['superheroe'] == 'Capitana Marvel':
            nombre_capitana_marvel = personaje['personaje']
            
        # b) Mostrar los nombres de los superhéroes femeninos 
        if personaje['genero'] == 'F':
            superheroes_femeninos.append(personaje['superheroe'])
            
        # c) Mostrar los nombres de los personajes masculinos 
        if personaje['genero'] == 'M':
            personajes_masculinos.append(personaje['personaje'])
            
        # d) Determinar el nombre del superhéroe de Scott Lang 
        if personaje['personaje'] == 'Scott Lang':
            superheroe_scott_lang = personaje['superheroe']
            
        # e) Mostrar datos de superhéroes o personajes que empiezan con 'S' 
        # Usamos el método " startswith() " de los strings para verificar la inicial
        if personaje['personaje'].startswith('S') or personaje['superheroe'].startswith('S'):
            nombres_con_s.append(personaje)
            
        # f) Determinar si Carol Danvers está en la cola y cual es su identidad como superhéroe 
        if personaje['personaje'] == 'Carol Danvers':
            carol_danvers_encontrada = True
            superheroe_carol_danvers = personaje['superheroe']
            
        # Volvemos a insertar el elemento al final de la cola para que quede exactamente
        # en el mismo orden y estado en el que estaba al principio.
        arribo(cola_mcu, personaje)


    # Mostrar los Resultados:
    print("=== RESULTADOS MCU ===\n")
    # a)
    print(f"a) El nombre de Capitana Marvel es: {nombre_capitana_marvel}")
    # b)
    print(f"b) Superhéroes femeninos: {', '.join(superheroes_femeninos)}")
    # c)
    print(f"c) Personajes masculinos: {', '.join(personajes_masculinos)}")
    # d)
    print(f"d) El nombre de superhéroe de Scott Lang es: {superheroe_scott_lang}")
    # e)
    print("e) Personajes o superhéroes que comienzan con la letra 'S':")
    for dato in nombres_con_s:
        print(f"   - {dato}")
    # f)
    if carol_danvers_encontrada:
        print(f"f) Carol Danvers 'SÍ' está en la cola. Su nombre de superhéroe es: {superheroe_carol_danvers}")
    else:
        print("f) Carol Danvers 'NO' se encuentra en la cola.")


# Prueba del Código:

if __name__ == "__main__":
    # Creamos la cola principal
    cola_marvel = Cola()
    
    # Cargamos los datos de prueba usando diccionarios
    arribo(cola_marvel, {'personaje': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'})
    arribo(cola_marvel, {'personaje': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'})
    arribo(cola_marvel, {'personaje': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'})
    arribo(cola_marvel, {'personaje': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'})
    arribo(cola_marvel, {'personaje': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'})
    arribo(cola_marvel, {'personaje': 'Wanda Maximoff', 'superheroe': 'Scarlet Witch', 'genero': 'F'})
    arribo(cola_marvel, {'personaje': 'Stephen Strange', 'superheroe': 'Doctor Strange', 'genero': 'M'})
    arribo(cola_marvel, {'personaje': 'Peter Parker', 'superheroe': 'Spider-Man', 'genero': 'M'})

    # Ejecutamos nuestra función principal
    analizar_personajes_marvel(cola_marvel)
    