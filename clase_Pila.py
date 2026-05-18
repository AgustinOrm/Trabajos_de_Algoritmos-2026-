class nodoPila(object):
# Clase nodo pila.

    info, sig = None, None

class Pila(object):
# Clase Pila.

    def __init__(self):
    # Crea una pila vacia.

        self.cima = None
        self.tamanio = 0

    def apilar(pila, dato):
    # Apila el dato sobre la cima de la pila.

        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = pila.cima
        pila.cima = nodo
        pila.tamanio += 1

    def desapilar(pila):
    #Desapila el elemento en la cima de la pila y lo devuelve.

        x = pila.cima.info
        pila.cima = pila.cima.sig
        pila.tamanio -= 1
        return x

    def pila_vacia(pila):
    # Devuelve true si la pila esta vacia.
        return pila.cima is None

    def en_cima(pila):
    # Devuelve el valor almacenado en la cima de la pila.
        if pila.cima is not None:
            return pila.cima.info
        else:
            return None

    def tamanio(pila):
    # Devuelve el numero de elementos en la pila.
        return pila.tamanio

    def barrido(pila):
    # Muestra el contenido de una pila sin perder datos.
        paux = Pila()
        while(not pila.pila_vacia()):
            dato = pila.desapilar()
            print(dato)
            paux.apilar(dato)

        while(not paux.pila_vacia()):
            dato = paux.desapilar()
            pila.apilar(dato)

