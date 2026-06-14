class nodoCola(object):
    """Clase nodo cola."""
    def __init__(self):
        self.info = None  # Almacena el dato
        self.sig = None   # Puntero al siguiente nodo


class Cola(object):
    """Clase Cola."""
    def __init__(self):
        """Crea una cola vacía."""
        self.frente = None
        self.final = None
        self.tamanio = 0


def arribo(cola, dato):
    """Arriba el dato al final de la cola."""
    nodo = nodoCola()
    nodo.info = dato
    
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
        
    cola.final = nodo
    cola.tamanio += 1


def atencion(cola):
    """Atiende el elemento en el frente de la cola y lo devuelve."""
    if cola_vacia(cola):
        return None
        
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    
    if cola.frente is None:
        cola.final = None
        
    cola.tamanio -= 1
    return dato


def cola_vacia(cola):
    """Devuelve true si la cola está vacía."""
    return cola.frente is None


def en_frente(cola):
    """Devuelve el valor almacenado en el frente de la cola sin eliminarlo."""
    if not cola_vacia(cola):
        return cola.frente.info
    return None


def tamanio(cola):
    """Devuelve el número de elementos en la cola."""
    return cola.tamanio


def mover_al_final(cola):
    """Mueve el elemento del frente de la cola al final."""
    dato = atencion(cola)
    if dato is not None:
        arribo(cola, dato)
    return dato


# def barrido(cola):
#     """Muestra el contenido de una cola sin perder datos."""
#     caux = Cola()
#     while(not cola_vacia(cola)):
#         dato = atencion(cola)
#         print(dato)
#         arribo(caux, dato)
#     while(not cola_vacia(caux)):
#         dato = atencion(caux)
#         arribo(cola, dato)


def barrido_cola(cola):
    """Muestra el contenido de una cola sin perder datos."""
    i = 0
    num_elementos = tamanio(cola)
    while i < num_elementos:
        dato = mover_al_final(cola)
        print(dato)
        i += 1