from tda_Grafo import Grafo, insertar_vertice, insertar_arista, buscar_vertice, marcar_no_visitado, barrido_profundidad, barrido_amplitud, dijkstra, kruskal, eliminar_arista
from tda_Pila import desapilar, pila_vacia


# 5) Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios para resolver las tareas, listadas a 
# continuación:
# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
# Red Hat, Debian, Arch;
# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
# Red Hat, Fedora hasta la impresora;
# d. encontrar el árbol de expansión mínima;
# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
# f. indicar desde que computadora del switch 01 es el camino más corto
# al servidor “MongoDB”;
# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
# h. debe utilizar un grafo no dirigido.


# # a) y h) Crear grafo no dirigido y almacenar tipos.
# grafo = Grafo(dirigido=False)
# equipos = {
#     "Ubuntu": "pc", "Debian": "notebook", "Impresora": "impresora", "Mint": "pc",
#     "Switch 1": "switch", "Router 1": "router", "Router 2": "router", "Router 3": "router",
#     "Red Hat": "notebook", "Guaraní": "servidor", "Switch 2": "switch", "Manjaro": "pc",
#     "Fedora": "pc", "Parrot": "pc", "MongoDB": "servidor", "Arch": "notebook"
# }

# for equipo in equipos.keys():
#     insertar_vertice(grafo, equipo)

# conexiones = [
#     ("Ubuntu", "Switch 1", 18), ("Debian", "Switch 1", 17), ("Impresora", "Switch 1", 22), ("Mint", "Switch 1", 80),
#     ("Switch 1", "Router 1", 29), ("Router 1", "Router 2", 37), ("Router 1", "Router 3", 43), ("Router 2", "Router 3", 50),
#     ("Red Hat", "Router 2", 25), ("Guaraní", "Router 2", 9), ("Router 3", "Switch 2", 61), ("Manjaro", "Switch 2", 40),
#     ("Fedora", "Switch 2", 3), ("Parrot", "Switch 2", 12), ("MongoDB", "Switch 2", 5), ("Arch", "Switch 2", 56)
# ]

# for origen, destino, peso in conexiones:
#     nodo_origen = buscar_vertice(grafo, origen)
#     nodo_destino = buscar_vertice(grafo, destino)
#     insertar_arista(grafo, peso, nodo_origen, nodo_destino)

# # b) Barrido en profundidad y amplitud desde notebooks.
# notebooks = ["Red Hat", "Debian", "Arch"]
# print("\nb) Barrido Profundidad y Amplitud. ")
# for nb in notebooks:
#     vertice = buscar_vertice(grafo, nb)
#     if vertice:
#         print(f"\nProfundidad desde {nb}:")
#         marcar_no_visitado(grafo)
#         barrido_profundidad(grafo, vertice)
        
#         print(f"\nAmplitud desde {nb}:")
#         marcar_no_visitado(grafo)
#         barrido_amplitud(grafo, vertice)

# # Función auxiliar para recuperar la distancia desde el camino de Dijkstra
# def obtener_distancia(pila_dijkstra, destino):
#     while not pila_vacia(pila_dijkstra):
#         dato = desapilar(pila_dijkstra)
#         if dato[1][0].info == destino:
#             return dato[0]
#     return float('inf')

# # c) Camino más corto para imprimir desde Manjaro, Red Hat, Fedora.
# imprimir_desde = ["Manjaro", "Red Hat", "Fedora"]
# print("\nc) Camino más corto a la Impresora. ")
# for pc in imprimir_desde:
#     camino = dijkstra(grafo, pc, "Impresora")
#     dist = obtener_distancia(camino, "Impresora")
#     print(f"Desde {pc} hasta Impresora: {dist} de distancia.")

# # d) Árbol de expansión mínima.
# print("\nd) Árbol de expansión mínima (Kruskal). ")
# bosque = kruskal(grafo)
# for arbol in bosque:
#     print(arbol)

# # e) PC (no notebook) con camino más corto a "Guaraní".
# pcs = [nombre for nombre, tipo in equipos.items() if tipo == "pc"]
# menor_dist_guarani = float('inf')
# pc_mas_cercana_guarani = ""

# for pc in pcs:
#     camino = dijkstra(grafo, pc, "Guaraní")
#     dist = obtener_distancia(camino, "Guaraní")
#     if dist < menor_dist_guarani:
#         menor_dist_guarani = dist
#         pc_mas_cercana_guarani = pc

# print(f"\ne) PC más corta a Guaraní. ")
# print(f"{pc_mas_cercana_guarani} con distancia {menor_dist_guarani}")

# # f) Computadora del Switch 1 más corta a "MongoDB".
# # Equipos conectados a Switch 1 son Ubuntu, Debian, Mint. Computadoras = pcs o notebooks.
# computadoras_sw1 = ["Ubuntu", "Debian", "Mint"]
# menor_dist_mongo = float('inf')
# comp_mas_cercana_mongo = ""

# for comp in computadoras_sw1:
#     camino = dijkstra(grafo, comp, "MongoDB")
#     dist = obtener_distancia(camino, "MongoDB")
#     if dist < menor_dist_mongo:
#         menor_dist_mongo = dist
#         comp_mas_cercana_mongo = comp

# print(f"\nf) Computadora en Switch 1 más corta a MongoDB. ")
# print(f"{comp_mas_cercana_mongo} con distancia {menor_dist_mongo}")

# # g) Cambiar impresora a Router 2 y rehacer punto b.
# print("\ng) Cambio de conexión de Impresora y rehacer punto b. ")
# # Eliminar conexión Switch 1 - Impresora (en ambos sentidos al ser no dirigido)
# v_impresora = buscar_vertice(grafo, "Impresora")
# v_sw1 = buscar_vertice(grafo, "Switch 1")

# # Se pasa la lista de adyacentes en lugar del nodo vértice
# eliminar_arista(v_impresora.adyacentes, "Switch 1")
# eliminar_arista(v_sw1.adyacentes, "Impresora")

# # Conectar Impresora a Router 2
# v_router2 = buscar_vertice(grafo, "Router 2")
# # Asignamos un peso representativo, ej: 10
# insertar_arista(grafo, 10, v_impresora, v_router2)

# for nb in notebooks:
#     vertice = buscar_vertice(grafo, nb)
#     if vertice:
#         print(f"\nProfundidad desde {nb}:")
#         marcar_no_visitado(grafo)
#         barrido_profundidad(grafo, vertice)
        
#         print(f"\nAmplitud desde {nb}:")
#         marcar_no_visitado(grafo)
#         barrido_amplitud(grafo, vertice)





# 14) Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.


# # a) Crear grafo no dirigido y vértices de ambientes.
# grafo = Grafo(dirigido=False)
# ambientes = [
#     "cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
#     "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"
# ]

# for ambiente in ambientes:
#     insertar_vertice(grafo, ambiente)

# # b) Cargar aristas (al menos 3 por vértice, 2 vértices con 5 aristas).
# # Vértices con 5 aristas: 'sala de estar' y 'comedor'
# conexiones = [
#     ("sala de estar", "comedor", 4),
#     ("sala de estar", "cocina", 3),
#     ("sala de estar", "habitación 1", 4),
#     ("sala de estar", "habitación 2", 5),
#     ("sala de estar", "baño 1", 3), 
#     ("comedor", "cocina", 3),
#     ("comedor", "patio", 4),
#     ("comedor", "quincho", 6),
#     ("comedor", "terraza", 5),
#     ("cocina", "baño 1", 3), 
#     ("cochera", "patio", 5),
#     ("cochera", "quincho", 4),
#     ("cochera", "terraza", 6),
#     ("quincho", "patio", 3), 
#     ("baño 1", "habitación 1", 6),
#     ("baño 2", "habitación 2", 4),
#     ("baño 2", "terraza", 4),
#     ("baño 2", "habitación 1", 3), 
#     ("habitación 2", "terraza", 3)
# ]

# for origen, destino, peso in conexiones:
#     nodo_origen = buscar_vertice(grafo, origen)
#     nodo_destino = buscar_vertice(grafo, destino)
#     insertar_arista(grafo, peso, nodo_origen, nodo_destino)

# # c) Árbol de expansión mínima y metros de cable.
# def metros_cable_mst(conexiones, ambientes):
#     # Función auxiliar para sumar los pesos (metros) del MST.
#     aristas_ordenadas = sorted(conexiones, key=lambda x: x[2])
#     padre = {nodo: nodo for nodo in ambientes}
    
#     def encontrar(nodo):
#         if padre[nodo] == nodo:
#             return nodo
#         return encontrar(padre[nodo])
        
#     def unir(nodo1, nodo2):
#         raiz1 = encontrar(nodo1)
#         raiz2 = encontrar(nodo2)
#         if raiz1 != raiz2:
#             padre[raiz2] = raiz1
#             return True
#         return False

#     metros_totales = 0
#     aristas_mst = []
#     for origen, destino, peso in aristas_ordenadas:
#         if unir(origen, destino):
#             metros_totales += peso
#             aristas_mst.append((origen, destino, peso))
            
#     return metros_totales, aristas_mst

# metros_totales, aristas_mst = metros_cable_mst(conexiones, ambientes)
# print("c) Árbol de expansión mínima (Metros de cable eléctrico). ")
# print(f"Metros totales necesarios: {metros_totales} metros")
# for o, d, p in aristas_mst:
#     print(f"  {o} - {d}: {p}m")

# # d) Camino más corto desde habitación 1 hasta sala de estar.
# print("\nd) Camino más corto para cable de red (Smart TV). ")
# # dijkstra devuelve una Pila donde el dato es [distancia, [nodo_actual, nodo_anterior]]
# camino = dijkstra(grafo, "habitación 1", "sala de estar")

# metros_red = float('inf')
# while not pila_vacia(camino):
#     dato = desapilar(camino)
#     if dato[1][0].info == "sala de estar":
#         metros_red = dato[0]
#         break

# print(f"Metros de cable de red necesarios desde habitación 1 a sala de estar: {metros_red} metros")