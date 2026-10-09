# CAMBIO 1 (modificado): por_nivel necesita el TDA Cola (Cola, arribo,
# atencion y cola_vacia). En lugar de la cola mínima que se había agregado
# antes, ahora se importan desde el archivo tda_Cola.py, que debe estar en
# la misma carpeta que este archivo.
from tda_Cola import Cola, arribo, atencion, cola_vacia


class nodoArbol(object):
    """Clase nodo árbol."""

    def __init__(self, info):
        """Crea un nodo con la información cargada."""
        self.izq = None
        self.der = None
        self.info = info


def eliminar_nodo(raiz, clave):
    """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
    x = None
    if(raiz is not None):
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif(clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                # CAMBIO 3: la función "remplazar" ahora se llama "reemplazar".
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x


def insertar_nodo(raiz, dato):
    """Inserta un dato al árbol."""
    if(raiz is None):
        raiz = nodoArbol(dato)
    elif(dato < raiz.info):
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz


# CAMBIO 2: la función "arbolvacio" ahora se llama "arbol_vacio".
def arbol_vacio(raiz):
    """Devuelve true si el árbol esta vacio."""
    return raiz is None


# CAMBIO 3: la función "remplazar" ahora se llama "reemplazar" (también en
# su llamada recursiva y en la llamada desde eliminar_nodo).
def reemplazar(raiz):
    """Determina el nodo que remplazará al que se elimina."""
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = reemplazar(raiz.der)
    return raiz, aux


def por_nivel(raiz):
    # CAMBIO 2 (corregido): el docstring original decía "barrido postorden",
    # pero esta función hace el barrido por nivel (usando una cola).
    """Realiza el barrido por nivel del árbol."""
    pendientes = Cola()
    arribo(pendientes, raiz)
    while(not cola_vacia(pendientes)):
        nodo = atencion(pendientes)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(pendientes, nodo.izq)
        if(nodo.der is not None):
            arribo(pendientes, nodo.der)


def buscar(raiz, clave):
    """Devuelve la direccion del elemento buscado."""
    pos = None
    if(raiz is not None):
        if(raiz.info == clave):
            pos = raiz
        elif clave < raiz.info:
            pos = buscar(raiz.izq, clave)
        else:
            pos = buscar(raiz.der, clave)
    return pos


def inorden(raiz):
    """Realiza el barrido inorden del árbol."""
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def preorden(raiz):
    """Realiza el barrido preorden del árbol."""
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def postorden(raiz):
    """Realiza el barrido postorden del árbol."""
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)
