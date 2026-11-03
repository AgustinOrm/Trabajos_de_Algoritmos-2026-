#Clase nodo pila.
class nodoPila(object):
    info, sig = None, None

#Clase Pila.
class Pila(object):
    
    #Crea una pila vacia. (Constructor de la Clase)
    def __init__(self):
        self.cima = None
        self.tamanio = 0
    
#Métodos para alterar la Clase:

#Apila el dato sobre la cima de la pila.
def apilar(pila, dato):  
    nodo = nodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1

#Desapila el elemento en la cima de la pila y lo devuelve.
def desapilar(pila):
    x = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return x

#Devuelve true si la pila esta vacia.
def pila_vacia(pila):
    return pila.cima is None

#Devuelve el valor almacenado en la cima de la pila.
def en_cima(pila):
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None

#Devuelve el numero de elementos en la pila.
def tamanio(pila):
    return pila.tamanio

#Muestra el contenido de una pila sin perder datos.
def barrido(pila):
    paux = Pila()
    while(not pila_vacia(pila)):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)
    
    while(not pila_vacia(paux)):
        dato = desapilar(paux)
        apilar(pila, dato)
