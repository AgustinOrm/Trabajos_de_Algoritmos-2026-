#Clase nodo cola.
class nodoCola(object):
    info, sig = None, None

#Clase Cola.
class Cola(object):
    #Crea una cola vacia. (Constructor)
    def __init__(self):
        self.frente, self.final = None, None
        self.tamamio = 0

#Arriba el dato al final de la cola.
def arribo(cola, dato):
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamamio += 1

#Atiende el elemento en el frente de la cola y lo devuelve.
def atencion(cola):
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamamio -= 1
    return dato

#Devuelve true si la cola esta vacia.
def cola_vacia(cola):
    return cola.frente is None

#Devuelve el valor almacenado en el frente de la cola.
def en_frente(cola):
    return cola.frente.info

#Devuelve el numero de elementos en la cola.
def tamanio(cola):
    return cola.tamamio

#Mueve el elemento del frente de la cola al final.
def mover_al_final(cola):
    dato = atencion(cola)
    arribo(cola, dato)
    return dato

# #Muestra el contenido de una cola sin perder datos.
# def barrido(cola):
#     caux = Cola()
#     while(not cola_vacia(cola)):
#         dato = atencion(cola)
#         print(dato)
#         arribo(caux, dato)

#     while(not cola_vacia(caux)):
#         dato = atencion(caux)
#         arribo(cola, dato)

#Muestra el contenido de una cola sin perder datos.
def barrido(cola):
    i = 0
    while(i < tamanio(cola)):
        dato = mover_al_final(cola)
        print(dato)
        i += 1
