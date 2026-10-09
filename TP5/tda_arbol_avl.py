# CAMBIO 1 (agregado): se importa el TDA Cola (tda_Cola.py, misma carpeta)
# porque por_nivel lo necesita.
from tda_Cola import Cola, arribo, atencion, cola_vacia


class nodoArbol(object):
    """Clase nodo árbol."""

    # CAMBIO 2 (modificado): el nodo original solo recibía "info", pero
    # insertar_nodo lo llamaba como nodoArbol(dato, pos) y eliminar_nodo usa
    # el campo "nrr". Se agrega el parámetro opcional "nrr" y el campo
    # self.nrr (número relativo de registro, mencionado en el capítulo).
    def __init__(self, info, nrr=None):
        """Crea un nodo con la información cargada."""
        self.izq = None
        self.der = None
        self.info = info
        self.altura = 0
        self.nrr = nrr


def altura(raiz):
    """Devuelve la altura de un nodo."""
    if(raiz is None):
        return -1
    else:
        return raiz.altura


def actualizaraltura(raiz):
    """Actualiza la altura de un nodo."""
    if(raiz is not None):
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1


def rotar_simple(raiz, control):
    """Realiza una rotación simple de nodos a la derecha o a la izquierda."""
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizaraltura(raiz)
    actualizaraltura(aux)
    raiz = aux
    return raiz


def rotar_doble(raiz, control):
    """Realiza una rotación doble de nodos a la derecha o a la izquierda."""
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz


def balancear(raiz):
    """Determina que rotación hay que hacer para balancear el árbol."""
    if(raiz is not None):
        if(altura(raiz.izq)-altura(raiz.der) == 2):
            if(altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif(altura(raiz.der)-altura(raiz.izq) == 2):
            if(altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz


# CAMBIO 3 (modificado): "pos" ahora es opcional (pos=None). En el ejemplo
# de la figura 33 se llama insertar_nodo(raiz, pais) con solo dos argumentos,
# lo que fallaba con la firma original (raiz, dato, pos).
def insertar_nodo(raiz, dato, pos=None):
    """Inserta un dato al árbol."""
    if(raiz is None):
        raiz = nodoArbol(dato, pos)
    elif(dato < raiz.info):
        raiz.izq = insertar_nodo(raiz.izq, dato, pos)
    else:
        raiz.der = insertar_nodo(raiz.der, dato, pos)
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz


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
                # CAMBIO 4: se llama a "reemplazar" (antes "remplazar"),
                # igual que en tda_Arbol.py.
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info, raiz.nrr = aux.info, aux.nrr
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz, x


# CAMBIO 5 (agregado): el libro no muestra "reemplazar" en la parte AVL,
# pero eliminar_nodo la necesita. Se toma la del árbol binario de búsqueda
# (tda_Arbol.py). Además, en su rama recursiva se agregan balancear y
# actualizaraltura: sin esto, al quitar la hoja mayor del subárbol izquierdo
# las alturas de los nodos del camino quedaban desactualizadas y el árbol
# podía desbalancearse.
def reemplazar(raiz):
    """Determina el nodo que remplazará al que se elimina."""
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = reemplazar(raiz.der)
        raiz = balancear(raiz)
        actualizaraltura(raiz)
    return raiz, aux


# CAMBIO 6 (agregado): el ejemplo de la figura 33 importa "buscar" e
# "inorden" de este módulo, por lo que se incluyen estas funciones (y el
# resto de los eventos del TDA) tal cual están en tda_Arbol.py.
def arbol_vacio(raiz):
    """Devuelve true si el árbol esta vacio."""
    return raiz is None


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


def por_nivel(raiz):
    # (mismo ajuste que en tda_Arbol.py: el docstring original decía
    # "postorden", pero la función hace el barrido por nivel.)
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
