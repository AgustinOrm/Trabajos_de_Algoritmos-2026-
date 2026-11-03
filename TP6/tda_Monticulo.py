class Heap(object):
    """Crea un montículo."""

    # MEJORA: el montículo solo podía ser máximo. Dijkstra, Prim y Kruskal
    # necesitan un montículo MÍNIMO (el libro lo indica), por lo que se agrega
    # el parámetro opcional "minimo". Por defecto es False (montículo máximo),
    # así que todo el código anterior sigue funcionando igual.
    def __init__(self, tamanio, minimo=False):
        """Crea el vector vacío para el montículo."""
        self.tamanio = 0
        self.vector = [None] * tamanio
        self.minimo = minimo


# Se agrega crear_monticulo porque está en la lista de funciones del TDA
# (crear_montículo(tamaño)), pero en el código original solo existía la
# clase Heap. Se mantiene la clase tal cual y esta función la envuelve.
def crear_monticulo(tamanio, minimo=False):
    """Crea y devuelve un montículo vacío del tamaño indicado."""
    return Heap(tamanio, minimo)


# La función intercambio no está definida en el libro (solo se menciona la
# palabra en los algoritmos de burbuja y selección) pero flotar, hundir y
# quitar la utilizan, por lo que se crea.
def intercambio(vector, i, j):
    """Intercambia los elementos de las posiciones i y j del vector."""
    vector[i], vector[j] = vector[j], vector[i]


# MEJORA (función auxiliar interna): cuando el montículo se usa como cola de
# prioridad los elementos son listas [prioridad, dato]. Comparar la lista
# completa fallaba cuando dos prioridades eran iguales (por ejemplo varios
# "inf" en Dijkstra), porque Python pasaba a comparar los datos, que son
# nodos que no se pueden comparar (TypeError). Ahora se compara solo la
# prioridad; si el elemento no es una lista (heapsort con números) se compara
# el valor directamente.
def _clave(dato):
    """Devuelve el valor por el cual se compara un elemento."""
    if isinstance(dato, list):
        return dato[0]
    return dato


# MEJORA (función auxiliar interna): indica si el elemento a debe estar más
# cerca de la cima que el elemento b, según el montículo sea máximo o mínimo.
def _mejor(heap, a, b):
    """Devuelve true si a debe ubicarse por encima de b."""
    if heap.minimo:
        return _clave(a) < _clave(b)
    return _clave(a) > _clave(b)


# Mejora: el original escribía en heap.vector[heap.tamanio] sin controlar
# nada, por lo que con el montículo lleno daba IndexError. Ahora se controla
# con heap_lleno y se devuelve True/False según se haya podido agregar.
def agregar(heap, dato):
    """Agrega un dato en el montículo."""
    if heap_lleno(heap):
        return False
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1
    return True


# Mejora: el original con el montículo vacío intercambiaba la posición 0 con
# la -1 y dejaba el tamaño en -1. Ahora, si está vacío, devuelve None
# (igual que eliminar del TDA lista cuando no encuentra el elemento).
# Nota: en la lista de funciones aparece quitar(montículo, dato), pero el
# código del libro (y su uso real) es quitar(heap): no necesita "dato".
def quitar(heap):
    """Quita el elemento en la cima del montículo."""
    if heap_vacio(heap):
        return None
    intercambio(heap.vector, 0, heap.tamanio-1)
    dato = heap.vector[heap.tamanio-1]
    heap.tamanio -= 1
    hundir(heap, 0)
    return dato


def cantidad_elementos(heap):
    """Devuelve la cantidad de elementos en el montículo."""
    return heap.tamanio


# Se agrega tamanio porque está en la lista de funciones del TDA
# (tamaño(montículo)). Se mantiene cantidad_elementos del original.
def tamanio(heap):
    """Devuelve la cantidad de elementos en el montículo."""
    return cantidad_elementos(heap)


def heap_vacio(heap):
    """Devuelve true si el montículo está vacío."""
    return heap.tamanio == 0


# Se agrega monticulo_vacio con el nombre de la lista de funciones del TDA.
# Se mantiene heap_vacio del original.
def monticulo_vacio(heap):
    """Devuelve true si el montículo no contiene elementos."""
    return heap_vacio(heap)


def heap_lleno(heap):
    """Devuelve true si el montículo está lleno."""
    return heap.tamanio == len(heap.vector)


# Se agrega monticulo_lleno con el nombre de la lista de funciones del TDA.
# Se mantiene heap_lleno del original.
def monticulo_lleno(heap):
    """Devuelve true si el montículo no puede almacenar más elementos."""
    return heap_lleno(heap)


# MEJORA: la comparación estaba fija para montículo máximo. Ahora usa _mejor,
# que respeta el tipo (máximo o mínimo) y compara solo la prioridad.
def flotar(heap, indice):
    """Flota el elemento en la posición índice."""
    while(indice > 0 and
          _mejor(heap, heap.vector[indice], heap.vector[(indice - 1) // 2])):
        padre = (indice - 1) // 2
        intercambio(heap.vector, indice, padre)
        indice = padre


# MEJORA: igual que flotar, ahora elige el hijo "mejor" (mayor en máximo,
# menor en mínimo) usando _mejor en lugar de los operadores > y <.
def hundir(heap, indice):
    """Hunde el elemento en la posición índice."""
    hijo_izq = (indice * 2) + 1
    control = True
    while(control and hijo_izq < heap.tamanio):
        hijo_der = hijo_izq + 1
        aux = hijo_izq
        if(hijo_der < heap.tamanio):
            if _mejor(heap, heap.vector[hijo_der], heap.vector[hijo_izq]):
                aux = hijo_der

        if _mejor(heap, heap.vector[aux], heap.vector[indice]):
            intercambio(heap.vector, indice, aux)
            indice = aux
            hijo_izq = (indice * 2) + 1
        else:
            control = False


# Se asume que el vector está completamente cargado.
def monticulizar(heap):
    """Transforma un vector en un montículo."""
    if heap.tamanio == 0:
        heap.tamanio = len(heap.vector)
    for i in range(1, heap.tamanio):
        flotar(heap, i)


def arribo(heap, dato, prioridad):
    """Arriba el dato a la cola utilizando prioridad."""
    # Devuelve el resultado de agregar (False si el montículo está lleno).
    return agregar(heap, [prioridad, dato])


# Devuelve solo el dato.
def atencion(heap):
    """Atiende el elemento en el frente de la cola y lo devuelve."""
    # Si la cola está vacía devuelve None en lugar de fallar al
    # intentar acceder a la posición [1] de None.
    if heap_vacio(heap):
        return None
    return quitar(heap)[1]


# Dijkstra llama a buscar_h. Busca, entre los
# elementos cargados, la posición del que guarda el vértice con la clave
# indicada. Se asume la estructura que usa Dijkstra: [prioridad, [vertice, anterior]].
# Devuelve el índice, o None si no está (por ejemplo si ya fue atendido).
def buscar_h(heap, clave):
    """Devuelve la posición del vértice con esa clave, o None si no está."""
    for i in range(heap.tamanio):
        if heap.vector[i][1][0].info == clave:
            return i
    return None


# Si la nueva prioridad "mejora" el lugar del elemento (sube en máximo, baja en mínimo) 
# se flota y si lo "empeora" se hunde.
def cambiar_prioridad(heap, indice, prioridad):
    """Cambia la prioridad de un elemento y lo acomoda en el montículo."""
    if indice < 0 or indice >= heap.tamanio:
        return False
    prioridad_anterior = heap.vector[indice][0]
    heap.vector[indice][0] = prioridad
    if heap.minimo:
        mejora = prioridad < prioridad_anterior
        empeora = prioridad > prioridad_anterior
    else:
        mejora = prioridad > prioridad_anterior
        empeora = prioridad < prioridad_anterior
    if(mejora):
        flotar(heap, indice)
    elif(empeora):
        hundir(heap, indice)
    return True


# Con montículo máximo el vector queda de menor a mayor; con mínimo queda de mayor a menor.
def heapsort(heap):
    """Método de ordenamiento heapsort."""
    monticulizar(heap)
    aux = heap.tamanio
    for i in range(heap.tamanio):
        quitar(heap)
    heap.tamanio = aux