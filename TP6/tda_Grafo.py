from math import inf
from tda_Cola import Cola, arribo, atencion, cola_vacia
from tda_Pila import Pila, apilar
from tda_Monticulo import Heap, heap_vacio, cambiar_prioridad, buscar_h
from tda_Monticulo import arribo as arribo_h
from tda_Monticulo import quitar as atencion_h


class nodoArista(object):
    """Clase nodo arista."""
    def __init__(self, info, destino):
        """Crea un nodo arista con la información cargada."""
        self.info = info
        self.destino = destino
        self.sig = None


class nodoVertice(object):
    """Clase nodo vértice."""

    def __init__(self, info):
        """Crea un nodo vértice con la información cargada."""
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()


class Grafo(object):
    """Clase grafo implementación lista de listas de adyacencia."""

    def __init__(self, dirigido=True):
        """Crea un grafo vacio."""
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


class Arista(object):
    """Clase lista de aristas implementación sobre lista."""

    def __init__(self):
        """Crea una lista de aristas vacia."""
        self.inicio = None
        self.tamanio = 0


def insertar_vertice(grafo, dato):
    """Inserta un vértice al grafo."""
    nodo = nodoVertice(dato)
    if (grafo.inicio is None or grafo.inicio.info > dato):
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info < nodo.info):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def insertar_arista(grafo, dato, origen, destino):
    """Inserta una arista desde el vértice origen al destino."""
    # Nota: origen y destino son nodos vértice (resultado de buscar_vertice).
    agregar_arista(origen.adyacentes, dato, destino.info)
    # Si el grafo no es dirigido la arista se agrega también en sentido inverso.
    if(not grafo.dirigido):
        agregar_arista(destino.adyacentes, dato, origen.info)


def agregar_arista(origen, dato, destino):
    """Agrega la arista desde el vértice origen al destino."""
    nodo = nodoArista(dato, destino)
    if (origen.inicio is None or origen.inicio.destino > destino):
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while(act is not None and act.destino < nodo.destino):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1


def eliminar_vertice(grafo, clave):
    """Elimina un vertice del grafo y lo devuelve si lo encuentra."""
    x = None
    if(grafo.inicio is None):
        return x
    if(grafo.inicio.info == clave):
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if(x is not None):
        aux = grafo.inicio
        while(aux is not None):
            if(aux.adyacentes.inicio is not None):
                eliminar_arista(aux.adyacentes, clave)
            aux = aux.sig
    return x


def buscar_vertice(grafo, buscado):
    """Devuelve la direccion del elemento buscado."""
    aux = grafo.inicio
    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux


def buscar_arista(vertice, buscado):
    """Devuelve la direccion del elemento buscado."""
    aux = vertice.adyacentes.inicio
    while(aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux


def tamanio(grafo):
    """Devuelve el numero de vertices en el grafo."""
    return grafo.tamanio


def grafo_vacio(grafo):
    """Devuelve true si el grafo esta vacio."""
    return grafo.inicio is None


def eliminar_arista(vertice, destino):
    """Elimina una arista del vertice y lo devuelve si lo encuentra."""
    x = None
    if(vertice.inicio is None):
        return x
    if(vertice.inicio.destino == destino):
        x = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    else:
        ant = vertice.inicio
        act = vertice.inicio.sig
        while(act is not None and act.destino != destino):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            vertice.tamanio -= 1
    return x


# Nota: antes de llamar a existe_paso (o a los barridos) conviene usar
# marcar_no_visitado, porque los vértices conservan la marca "visitado".
def existe_paso(grafo, origen, destino):
    """Determina si existe un camino entre origen y destino (profundidad)."""
    resultado = False
    if(not origen.visitado):
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while(vadyacentes is not None and not resultado):
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if(adyacente is not None):
                if(adyacente.info == destino.info):
                    return True
                elif(not adyacente.visitado):
                    resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado


def adyacentes(vertice):
    """Muestra los adyacentes del vertice."""
    aux = vertice.adyacentes.inicio
    while(aux is not None):
        print(aux.destino, aux.info)
        aux = aux.sig


def es_adyacente(vertice, destino):
    """Determina si el destino es adyacente directo."""
    resultado = False
    aux = vertice.adyacentes.inicio
    while(aux is not None and not resultado):
        if(aux.destino == destino):
            resultado = True
        aux = aux.sig
    return resultado


def marcar_no_visitado(grafo):
    """Marca todos los vertices del grafo como no visitados."""
    aux = grafo.inicio
    while(aux is not None):
        aux.visitado = False
        aux = aux.sig


def barrido_vertices(grafo):
    """Realiza un barrido del grafo mostrando sus valores."""
    aux = grafo.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig


def barrido_profundidad(grafo, vertice):
    """Barrido en profundidad del grafo."""
    while(vertice is not None):
        if(not vertice.visitado):
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while(adyacentes is not None):
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if(adyacente is not None and not adyacente.visitado):
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig


def barrido_amplitud(grafo, vertice):
    """Barrido en amplitud del grafo."""
    cola = Cola()
    while(vertice is not None):
        if(not vertice.visitado):
            vertice.visitado = True
            arribo(cola, vertice)
            while(not cola_vacia(cola)):
                nodo = atencion(cola)
                print(nodo.info)
                adyacentes = nodo.adyacentes.inicio
                while(adyacentes is not None):
                    adyacente = buscar_vertice(grafo, adyacentes.destino)
                    if(adyacente is not None and not adyacente.visitado):
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.sig
        vertice = vertice.sig


def dijkstra(grafo, origen, destino):
    """Algoritmo de Dijkstra para hallar el camino mas corto."""
    no_visitados = Heap(tamanio(grafo), True)
    camino = Pila()
    aux = grafo.inicio
    while(aux is not None):
        if(aux.info == origen):
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig

    while(not heap_vacio(no_visitados)):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while(aux is not None):
            pos = buscar_h(no_visitados, aux.destino)
            if(pos is not None):
                if(no_visitados.vector[pos][0] > dato[0] + aux.info):
                    no_visitados.vector[pos][1][1] = dato[1][0].info
                    cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino



def prim(grafo, origen=None):
    """Algoritmo de Prim para hallar el árbol de expansión mínimo."""
    if(grafo.inicio is None):
        return []
    if(origen is None):
        inicio = grafo.inicio
    else:
        inicio = buscar_vertice(grafo, origen)
        if(inicio is None):
            return []
    bosque = [[inicio.info]]
    aristas = []
    adyacentes = inicio.adyacentes.inicio
    while(adyacentes is not None):
        aristas.append([inicio.info, adyacentes.destino, adyacentes.info])
        adyacentes = adyacentes.sig
    while(len(bosque[0]) // 2 < tamanio(grafo)-1):
        menor = inf
        menor_arista = None
        tipo = None
        for arista in aristas:
            origen_a = arista[0]
            destino = arista[1]
            if(origen_a not in bosque[0] and destino in bosque[0]):
                if(arista[2] < menor):
                    menor, menor_arista = arista[2], arista
                    tipo = True
            if(origen_a in bosque[0] and destino not in bosque[0]):
                if(arista[2] < menor):
                    menor, menor_arista = arista[2], arista
                    tipo = False

        if(menor_arista is None):
            break
        arista = aristas.pop(aristas.index(menor_arista))
        if(len(bosque[0]) != 1):
            bosque[0] += [arista[0], arista[1]]
        else:
            bosque.pop()
            bosque.append([arista[0], arista[1]])
        aux = None
        if(tipo):
            aux = buscar_vertice(grafo, arista[0])
        else:
            aux = buscar_vertice(grafo, arista[1])
        adyacentes = aux.adyacentes.inicio
        while(adyacentes is not None):
            aristas.append([aux.info, adyacentes.destino, adyacentes.info])
            adyacentes = adyacentes.sig
    return bosque


def kruskal(grafo, origen=None):
    """Algoritmo de Kruskal para hallar el árbol de expansión mínimo."""
    bosque = []
    aristas = Heap(tamanio(grafo) ** 2, True)
    aux = grafo.inicio
    while(aux is not None):
        bosque.append([aux.info])
        adyacentes = aux.adyacentes.inicio
        while(adyacentes is not None):
            arribo_h(aristas, [aux.info, adyacentes.destino], adyacentes.info)
            adyacentes = adyacentes.sig
        aux = aux.sig

    while(len(bosque) > 1 and not heap_vacio(aristas)):
        dato = atencion_h(aristas)
        origen_a = None
        for elemento in bosque:
            if(dato[1][0] in elemento):
                origen_a = bosque.pop(bosque.index(elemento))
        destino = None
        for elemento in bosque:
            if(dato[1][1] in elemento):
                destino = bosque.pop(bosque.index(elemento))
        if(origen_a is not None and destino is not None):
            if(len(origen_a) > 1 and len(destino) == 1):
                destino.insert(0, dato[1][0])
            elif(len(destino) > 1 and len(origen_a) == 1):
                origen_a.append(dato[1][1])
            elif(len(destino) > 1 and len(origen_a) > 1):
                origen_a += [dato[1][0], dato[1][1]]
            bosque.append(origen_a+destino)
        elif(origen_a is not None):
            bosque.append(origen_a)
    return bosque