from tda_arbol_avl import insertar_nodo, eliminar_nodo, buscar, inorden, por_nivel


# Clase auxiliar usada por los dos ejercicios:
# Tabla para reemplazar las letras con tilde por la misma letra sin tilde.
# Se arma con str.maketrans (método propio de las cadenas).
TILDES = str.maketrans("áéíóúüñÁÉÍÓÚÜÑ", "aeiouunAEIOUUN")


def _clave_orden(texto):
    # Quita las tildes y pasa a minúsculas para ordenar en español.
    return texto.translate(TILDES).lower()


class Nombre(str):
    # Cadena que se compara sin tener en cuenta tildes ni mayúsculas.
    def __lt__(self, otro):
        return _clave_orden(self) < _clave_orden(otro)

    def __gt__(self, otro):
        return _clave_orden(self) > _clave_orden(otro)

    def __le__(self, otro):
        return _clave_orden(self) <= _clave_orden(otro)

    def __ge__(self, otro):
        return _clave_orden(self) >= _clave_orden(otro)


#5) Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe 
# (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que 
# indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
#   I. determinar cuántos nodos tiene cada árbol;
#   II. realizar un barrido ordenado alfabéticamente de cada árbol.

# EJERCICIO 5.
# Árbol con los superhéroes y villanos de la saga Marvel Cinematic Universe
# (MCU): listados, conteo, corrección de un nombre y generación de un bosque.
# Cada nodo guarda el nombre en el campo info y en el campo nrr un booleano: 
# True si es héroe, False si es villano.
HEROES_MCU = [
    "Iron Man", "Capitán América", "Thor", "Hulk", "Black Widow", "Hawkeye",
    "Spider-Man", "Black Panther", "Ant-Man", "Wasp", "Capitana Marvel",
    "Scarlet Witch", "Vision", "Falcon", "Winter Soldier", "War Machine",
    "Star-Lord", "Gamora", "Drax", "Rocket Raccoon", "Groot", "Mantis",
    "Shang-Chi", "Wong", "Cassie Lang",
    # Mal cargado a propósito: el nombre correcto es "Doctor Strange" y se corrige en la consigna e.
    "Dr Strange",
]

VILLANOS_MCU = [
    "Thanos", "Loki", "Ultron", "Red Skull", "Hela", "Killmonger", "Ronan",
    "Ego", "Vulture", "Mysterio", "Iron Monger", "Whiplash", "Abomination",
    "Kaecilius", "Dormammu", "Ghost", "Malekith", "Surtur", "Baron Zemo",
    "Kang", "Crossbones", "Yon-Rogg", "Taskmaster", "Ebony Maw",
]





def cargar_mcu():
    # a) Carga el árbol con los héroes (True) y los villanos (False).
    raiz = None
    for nombre in HEROES_MCU:
        raiz = insertar_nodo(raiz, Nombre(nombre), True)
    for nombre in VILLANOS_MCU:
        raiz = insertar_nodo(raiz, Nombre(nombre), False)
    return raiz


def listar_villanos(raiz):
    # b) Muestra los villanos ordenados alfabéticamente (barrido inorden).
    if raiz is not None:
        listar_villanos(raiz.izq)
        if not raiz.nrr:
            print("  ", raiz.info)
        listar_villanos(raiz.der)


def listar_heroes_con_inicial(raiz, letra):
    # c) Muestra los superhéroes cuyo nombre empieza con la letra dada.
    if raiz is not None:
        listar_heroes_con_inicial(raiz.izq, letra)
        if raiz.nrr and _clave_orden(raiz.info).startswith(_clave_orden(letra)):
            print("  ", raiz.info)
        listar_heroes_con_inicial(raiz.der, letra)


def contar_heroes(raiz):
    # d) Devuelve cuántos superhéroes hay en el árbol.
    if raiz is None:
        return 0
    cantidad = 1 if raiz.nrr else 0
    return cantidad + contar_heroes(raiz.izq) + contar_heroes(raiz.der)


def buscar_por_proximidad(raiz, texto, encontrados=None):
    # e) Devuelve los nodos cuyo nombre contiene el texto (sin distinguir
    # mayúsculas ni tildes).
    if encontrados is None:
        encontrados = []
    if raiz is not None:
        buscar_por_proximidad(raiz.izq, texto, encontrados)
        if _clave_orden(texto) in _clave_orden(raiz.info):
            encontrados.append(raiz)
        buscar_por_proximidad(raiz.der, texto, encontrados)
    return encontrados


def corregir_nombre(raiz, texto, nombre_correcto):
    # e) Busca por proximidad el nodo mal cargado y le cambia el nombre.
    encontrados = [(n.info, n.nrr) for n in buscar_por_proximidad(raiz, texto)]
    for nombre_mal, es_heroe in encontrados:
        raiz, _ = eliminar_nodo(raiz, Nombre(nombre_mal))
        raiz = insertar_nodo(raiz, Nombre(nombre_correcto), es_heroe)
    return raiz, [nombre for nombre, _ in encontrados]


def listar_heroes_descendente(raiz):
    # f) Muestra los superhéroes ordenados de Z a A (inorden invertido).
    if raiz is not None:
        listar_heroes_descendente(raiz.der)
        if raiz.nrr:
            print("  ", raiz.info)
        listar_heroes_descendente(raiz.izq)


def generar_bosque(raiz, bosque=None):
    # g) Genera el bosque: un árbol con los superhéroes y otro con los
    # villanos. Devuelve un diccionario con las dos raíces.
    if bosque is None:
        bosque = {"heroes": None, "villanos": None}
    if raiz is not None:
        generar_bosque(raiz.izq, bosque)
        clave = "heroes" if raiz.nrr else "villanos"
        bosque[clave] = insertar_nodo(bosque[clave], raiz.info, raiz.nrr)
        generar_bosque(raiz.der, bosque)
    return bosque


def contar_nodos(raiz):
    # g-I) Devuelve la cantidad de nodos de un árbol.
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.izq) + contar_nodos(raiz.der)


def ejercicio_5():
    raiz = cargar_mcu()

    print("b) Villanos ordenados alfabéticamente:")
    listar_villanos(raiz)

    print("\nc) Superhéroes que empiezan con C:")
    listar_heroes_con_inicial(raiz, "C")

    print("\nd) Cantidad de superhéroes:", contar_heroes(raiz))

    print("\ne) Corrección de Doctor Strange (búsqueda por proximidad):")
    print("   Coincidencias con 'Strange':",
          [n.info for n in buscar_por_proximidad(raiz, "Strange")])
    raiz, corregidos = corregir_nombre(raiz, "Strange", "Doctor Strange")
    print("   Nombre corregido:", corregidos, "->", "Doctor Strange")
    nodo = buscar(raiz, Nombre("Doctor Strange"))
    print("   Ahora está cargado como:", nodo.info,
          "(héroe)" if nodo.nrr else "(villano)")

    print("\nf) Superhéroes ordenados de manera descendente:")
    listar_heroes_descendente(raiz)

    print("\ng) Bosque: un árbol de superhéroes y otro de villanos")
    bosque = generar_bosque(raiz)
    arboles = (("Superhéroes", bosque["heroes"]),
               ("Villanos", bosque["villanos"]))
    print("   I) Cantidad de nodos de cada árbol:")
    for titulo, arbol in arboles:
        print(f"      {titulo}: {contar_nodos(arbol)}")
    print("   II) Barrido ordenado alfabéticamente de cada árbol:")
    for titulo, arbol in arboles:
        print(f"      --- {titulo} ---")
        inorden(arbol)
    return raiz




# EJERCICIO 23.
# Árbol con las criaturas de la mitología griega y los héroes o dioses que
# las derrotaron (tabla de la guía): listados, descripciones, capturas,
# búsquedas por coincidencia, bajas y modificaciones.

CRIATURAS = [
    ("Ceto", None), ("Tifón", "Zeus"), ("Equidna", "Argos Panoptes"),
    ("Dino", None), ("Pefredo", None), ("Enio", None), ("Escila", None),
    ("Caribdis", None), ("Euríale", None), ("Esteno", None),
    ("Medusa", "Perseo"), ("Ladón", "Heracles"), ("Águila del Cáucaso", None),
    ("Quimera", "Belerofonte"), ("Hidra de Lerna", "Heracles"),
    ("León de Nemea", "Heracles"), ("Esfinge", "Edipo"),
    ("Dragón de la Cólquida", None), ("Cerbero", None),
    ("Cerda de Cromión", "Teseo"), ("Ortro", "Heracles"),
    ("Toro de Creta", "Teseo"), ("Jabalí de Calidón", "Atalanta"),
    ("Carcinos", None), ("Gerión", "Heracles"), ("Cloto", None),
    ("Láquesis", None), ("Átropos", None), ("Minotauro de Creta", "Teseo"),
    ("Harpías", None), ("Argos Panoptes", "Hermes"),
    ("Aves del Estínfalo", None), ("Talos", "Medea"), ("Sirenas", None),
    ("Pitón", "Apolo"), ("Cierva de Cerinea", None), ("Basilisco", None),
    ("Jabalí de Erimanto", None),
]

# Descripciones que se cargan en la consigna b.
DESCRIPCIONES = {
    "Talos": "Gigante de bronce que custodiaba la isla de Creta.",
    "Cerbero": "Perro de tres cabezas que vigila la entrada del Inframundo.",
    "Hidra de Lerna": "Serpiente acuática con varias cabezas que se regeneraban.",
    "Medusa": "Gorgona con serpientes por cabello cuya mirada petrificaba.",
    "Quimera": "Monstruo con cabeza de león, cuerpo de cabra y cola de serpiente.",
    "Minotauro de Creta": "Mitad hombre y mitad toro, encerrado en el laberinto.",
    "León de Nemea": "León de piel invulnerable, primer trabajo de Heracles.",
    "Esfinge": "Criatura alada con rostro humano que planteaba enigmas.",
}


def nuevo_registro(derrotado_por):
    # Devuelve el diccionario de datos que se guarda en el campo nrr.
    return {"derrotado_por": derrotado_por, "descripcion": "", "capturada": None}


def cargar_criaturas():
    # Genera el árbol con los datos de la tabla.
    raiz = None
    for nombre, vencedor in CRIATURAS:
        raiz = insertar_nodo(raiz, Nombre(nombre), nuevo_registro(vencedor))
    return raiz


def listar_derrotas(raiz):
    # a) Listado inorden de las criaturas y quienes las derrotaron.
    if raiz is not None:
        listar_derrotas(raiz.izq)
        vencedor = raiz.nrr["derrotado_por"] or "nadie (sin derrotar)"
        print(f"   {raiz.info} - derrotada por: {vencedor}")
        listar_derrotas(raiz.der)


def cargar_descripcion(raiz, nombre, descripcion):
    # b) Carga la descripción de una criatura. Devuelve False si no existe.
    nodo = buscar(raiz, Nombre(nombre))
    if nodo is None:
        return False
    nodo.nrr["descripcion"] = descripcion
    return True


def mostrar_criatura(raiz, nombre):
    # c) Muestra toda la información de una criatura.
    nodo = buscar(raiz, Nombre(nombre))
    if nodo is None:
        print("   No se encontró la criatura", nombre)
    else:
        datos = nodo.nrr
        print("   Criatura:     ", nodo.info)
        print("   Derrotada por:", datos["derrotado_por"] or "nadie")
        print("   Capturada por:", datos["capturada"] or "nadie")
        print("   Descripción:  ", datos["descripcion"] or "(sin descripción)")


def contar_derrotas(raiz, conteo):
    # Cuenta en el diccionario conteo cuántas criaturas derrotó cada uno.
    if raiz is not None:
        contar_derrotas(raiz.izq, conteo)
        vencedor = raiz.nrr["derrotado_por"]
        if vencedor is not None:
            conteo[vencedor] = conteo.get(vencedor, 0) + 1
        contar_derrotas(raiz.der, conteo)


def tres_mayores_vencedores(raiz):
    # d) Devuelve los 3 héroes o dioses que derrotaron más criaturas y, si el
    # tercer puesto está empatado, la lista de todos los empatados.
    conteo = {}
    contar_derrotas(raiz, conteo)
    # Orden: más derrotas primero y, ante igualdad, alfabético.
    ordenado = sorted(conteo.items(), key=lambda par: (-par[1], par[0]))
    top = ordenado[:3]
    empatados = []
    if len(top) == 3:
        corte = top[2][1]
        empatados = [n for n, c in ordenado if c == corte]
        if len(empatados) == sum(1 for _, c in top if c == corte):
            empatados = []  # no hay nadie más empatado fuera del podio
    return top, empatados


def listar_derrotadas_por(raiz, heroe):
    # e) Lista las criaturas derrotadas por un héroe o dios.
    if raiz is not None:
        listar_derrotadas_por(raiz.izq, heroe)
        if raiz.nrr["derrotado_por"] == heroe:
            print("  ", raiz.info)
        listar_derrotadas_por(raiz.der, heroe)


def listar_no_derrotadas(raiz):
    # f) Lista las criaturas que no han sido derrotadas.
    if raiz is not None:
        listar_no_derrotadas(raiz.izq)
        if raiz.nrr["derrotado_por"] is None:
            print("  ", raiz.info)
        listar_no_derrotadas(raiz.der)


def registrar_captura(raiz, nombre, heroe):
    # g, h) Indica en el nodo de la criatura quién la capturó.
    nodo = buscar(raiz, Nombre(nombre))
    if nodo is None:
        return False
    nodo.nrr["capturada"] = heroe
    return True


def buscar_por_coincidencia(raiz, texto, encontrados=None):
    # i) Devuelve los nodos cuyo nombre contiene el texto (sin distinguir mayúsculas ni tildes).
    if encontrados is None:
        encontrados = []
    if raiz is not None:
        buscar_por_coincidencia(raiz.izq, texto, encontrados)
        if _clave_orden(texto) in _clave_orden(raiz.info):
            encontrados.append(raiz)
        buscar_por_coincidencia(raiz.der, texto, encontrados)
    return encontrados


def registrar_derrota(raiz, nombre, heroe, nota=""):
    # k) Modifica el nodo de una criatura indicando quién la derrotó y, opcionalmente, 
    # agrega una nota a la descripción.
    nodo = buscar(raiz, Nombre(nombre))
    if nodo is None:
        return False
    nodo.nrr["derrotado_por"] = heroe
    if nota:
        nodo.nrr["descripcion"] = (nodo.nrr["descripcion"] + " " + nota).strip()
    return True


def renombrar_criatura(raiz, nombre_actual, nombre_nuevo):
    # l) Cambia el nombre de una criatura.
    nodo = buscar(raiz, Nombre(nombre_actual))
    if nodo is None:
        return raiz, False
    datos = nodo.nrr
    raiz, _ = eliminar_nodo(raiz, Nombre(nombre_actual))
    raiz = insertar_nodo(raiz, Nombre(nombre_nuevo), datos)
    return raiz, True


def listar_capturadas_por(raiz, heroe):
    # n) Muestra las criaturas capturadas por un héroe o dios.
    if raiz is not None:
        listar_capturadas_por(raiz.izq, heroe)
        if raiz.nrr["capturada"] == heroe:
            print("  ", raiz.info)
        listar_capturadas_por(raiz.der, heroe)


def ejercicio_23():
    raiz = cargar_criaturas()

    print("a) Criaturas (inorden) y quienes las derrotaron:")
    listar_derrotas(raiz)

    print("\nb) Carga de descripciones:")
    for nombre, descripcion in DESCRIPCIONES.items():
        cargar_descripcion(raiz, nombre, descripcion)
    print(f"   Se cargaron {len(DESCRIPCIONES)} descripciones.")

    print("\nc) Información de la criatura Talos:")
    mostrar_criatura(raiz, "Talos")

    print("\nd) Los 3 que derrotaron más criaturas:")
    top, empatados = tres_mayores_vencedores(raiz)
    for puesto, (nombre, cantidad) in enumerate(top, 1):
        print(f"   {puesto}. {nombre}: {cantidad}")
    if empatados:
        print("   Nota: el tercer puesto está empatado entre:",
              ", ".join(empatados))

    print("\ne) Criaturas derrotadas por Heracles:")
    listar_derrotadas_por(raiz, "Heracles")

    print("\nf) Criaturas que no han sido derrotadas:")
    listar_no_derrotadas(raiz)

    print("\ng) Cada nodo tiene el campo 'capturada' (al inicio, nadie).")

    print("\nh) Heracles atrapa a Cerbero, Toro de Creta, Cierva de Cerinea "
          "y Jabalí de Erimanto:")
    for nombre in ("Cerbero", "Toro de Creta", "Cierva de Cerinea",
                   "Jabalí de Erimanto"):
        registrar_captura(raiz, nombre, "Heracles")
        print("   Capturada:", nombre)

    print("\ni) Búsquedas por coincidencia:")
    for texto in ("Jabalí", "cer"):
        nombres = [n.info for n in buscar_por_coincidencia(raiz, texto)]
        print(f"   '{texto}':", ", ".join(nombres))

    print("\nj) Eliminar al Basilisco y a las Sirenas:")
    for nombre in ("Basilisco", "Sirenas"):
        raiz, eliminado = eliminar_nodo(raiz, Nombre(nombre))
        print("   Eliminado:" if eliminado else "   No encontrado:", nombre)

    print("\nk) Heracles derrotó a varias Aves del Estínfalo:")
    registrar_derrota(raiz, "Aves del Estínfalo", "Heracles",
                      "Heracles derrotó a varias de ellas.")
    mostrar_criatura(raiz, "Aves del Estínfalo")

    print("\nl) Cambiar el nombre de Ladón por Dragón Ladón:")
    raiz, cambiado = renombrar_criatura(raiz, "Ladón", "Dragón Ladón")
    print("   Cambio realizado:", cambiado)
    mostrar_criatura(raiz, "Dragón Ladón")

    print("\nm) Listado por nivel del árbol:")
    por_nivel(raiz)

    print("\nn) Criaturas capturadas por Heracles:")
    listar_capturadas_por(raiz, "Heracles")
    return raiz




# Título y ejecución de los ejercicios 5 y 23.
if __name__ == "__main__":
    print("=" * 60)
    print("EJERCICIO 5")
    print("=" * 60)
    ejercicio_5()
    print("\n" + "=" * 60)
    print("EJERCICIO 23")
    print("=" * 60)
    ejercicio_23()
