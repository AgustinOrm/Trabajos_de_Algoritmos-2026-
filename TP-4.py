from tda_Lista import Lista, insertar, buscar, barrido, tamanio, eliminar


# #6) Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# # casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias 
# # para poder realizar las siguientes actividades:
# # a. eliminar el nodo que contiene la información de Linterna Verde;
# # b. mostrar el año de aparición de Wolverine;
# # c. cambiar la casa de Dr. Strange a Marvel;
# # d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# # “traje” o “armadura”;
# # e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# # sea anterior a 1963;
# # f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# # g. mostrar toda la información de Flash y Star-Lord;
# # h. listar los superhéroes que comienzan con la letra B, M y S;
# # i. determinar cuántos superhéroes hay de cada casa de comic.


# # #Ejercicio 6.
# class Superheroe(object):

#     def __init__(self, nombre, aparicion, casa, biografia):
#         self.nombre = nombre
#         self.aparicion = aparicion
#         self.casa = casa
#         self.biografia = biografia

#     def __str__(self):
#         return '{} | aparición: {} | casa: {} | bio: {}'.format(
#             self.nombre, self.aparicion, self.casa, self.biografia)


# # a. eliminar el nodo que contiene la información de Linterna Verde
# def eliminar_superheroe(lista, nombre):
#     return eliminar(lista, nombre, 'nombre')


# # b. mostrar el año de aparición de Wolverine
# def anio_aparicion(lista, nombre):
#     pos = buscar(lista, nombre, 'nombre')
#     if pos is not None:
#         return pos.info.aparicion
#     return None


# # c. cambiar la casa de Dr. Strange a Marvel
# def cambiar_casa(lista, nombre, casa):
#     pos = buscar(lista, nombre, 'nombre')
#     if pos is not None:
#         pos.info.casa = casa
#         return True
#     return False


# # d. nombres de superhéroes cuya biografía menciona "traje" o "armadura"
# def mencionan_traje_o_armadura(lista):
#     aux = lista.inicio
#     while(aux is not None):
#         bio = aux.info.biografia.lower()
#         if 'traje' in bio or 'armadura' in bio:
#             print(aux.info.nombre)
#         aux = aux.sig


# # e. nombre y casa de los superhéroes con aparición anterior a 1963
# def aparecieron_antes_de(lista, anio):
#     aux = lista.inicio
#     while(aux is not None):
#         if aux.info.aparicion < anio:
#             print(aux.info.nombre, '-', aux.info.casa)
#         aux = aux.sig


# # f. casa a la que pertenece un superhéroe
# def mostrar_casa(lista, nombre):
#     pos = buscar(lista, nombre, 'nombre')
#     if pos is not None:
#         print(nombre, 'pertenece a', pos.info.casa)
#     else:
#         print(nombre, 'no se encontró en la lista')


# # g. toda la información de un superhéroe
# def mostrar_info(lista, nombre):
#     pos = buscar(lista, nombre, 'nombre')
#     if pos is not None:
#         print(pos.info)
#     else:
#         print(nombre, 'no se encontró en la lista')


# # h. superhéroes cuyo nombre comienza con alguna de las letras dadas
# def listar_por_inicial(lista, letras):
#     aux = lista.inicio
#     while(aux is not None):
#         if aux.info.nombre[0].upper() in letras:
#             print(aux.info.nombre)
#         aux = aux.sig


# # i. cuántos superhéroes hay de cada casa
# def contar_por_casa(lista):
#     marvel = dc = 0
#     aux = lista.inicio
#     while(aux is not None):
#         if aux.info.casa == 'Marvel':
#             marvel += 1
#         elif aux.info.casa == 'DC':
#             dc += 1
#         aux = aux.sig
#     return marvel, dc


# def cargar_datos(lista):
#     datos = [
#         Superheroe('Linterna Verde', 1940, 'DC',
#                    'Recibe un anillo de poder y viste un traje verde.'),
#         Superheroe('Wolverine', 1974, 'Marvel',
#                    'Mutante con garras de adamantium y factor de curación.'),
#         Superheroe('Dr. Strange', 1963, 'DC',
#                    'Cirujano que se convierte en hechicero supremo.'),
#         Superheroe('Capitana Marvel', 1968, 'Marvel',
#                    'Piloto con poderes cósmicos y de vuelo.'),
#         Superheroe('Mujer Maravilla', 1941, 'DC',
#                    'Princesa amazona con un lazo de la verdad.'),
#         Superheroe('Flash', 1940, 'DC',
#                    'Velocista que se conecta con la Fuerza de la Velocidad.'),
#         Superheroe('Star-Lord', 1976, 'Marvel',
#                    'Aventurero espacial líder de los Guardianes de la Galaxia.'),
#         Superheroe('Iron Man', 1963, 'Marvel',
#                    'Genio millonario que construye una armadura de combate.'),
#         Superheroe('Batman', 1939, 'DC',
#                    'Detective de Gotham que usa un traje con forma de murciélago.'),
#         Superheroe('Superman', 1938, 'DC',
#                    'Último hijo de Krypton con superfuerza y vuelo.'),
#         Superheroe('Spider-Man', 1962, 'Marvel',
#                    'Joven con poderes arácnidos y un traje rojo y azul.'),
#         Superheroe('Black Widow', 1964, 'Marvel',
#                    'Espía entrenada en combate y operaciones encubiertas.'),
#         Superheroe('Black Panther', 1966, 'Marvel',
#                    'Rey de Wakanda con un traje de vibranium.'),
#         Superheroe('Aquaman', 1941, 'DC',
#                    'Rey de Atlantis que se comunica con la vida marina.'),
#         Superheroe('Shazam', 1940, 'DC',
#                    'Joven que se transforma en héroe al decir una palabra mágica.'),
#         Superheroe('Storm', 1975, 'Marvel',
#                    'Mutante capaz de controlar el clima.'),
#     ]
#     for heroe in datos:
#         insertar(lista, heroe, 'nombre')


# if __name__ == '__main__':
#     superheroes = Lista()
#     cargar_datos(superheroes)

#     print('a. Eliminar a Linterna Verde')
#     eliminado = eliminar_superheroe(superheroes, 'Linterna Verde')
#     print('   Eliminado:', eliminado.nombre if eliminado else 'no encontrado')

#     print('\nb. Año de aparición de Wolverine')
#     print('  ', anio_aparicion(superheroes, 'Wolverine'))

#     print('\nc. Cambiar la casa de Dr. Strange a Marvel')
#     mostrar_casa(superheroes, 'Dr. Strange')
#     cambiar_casa(superheroes, 'Dr. Strange', 'Marvel')
#     mostrar_casa(superheroes, 'Dr. Strange')

#     print('\nd. Biografía con "traje" o "armadura"')
#     mencionan_traje_o_armadura(superheroes)

#     print('\ne. Aparición anterior a 1963')
#     aparecieron_antes_de(superheroes, 1963)

#     print('\nf. Casa de Capitana Marvel y Mujer Maravilla')
#     mostrar_casa(superheroes, 'Capitana Marvel')
#     mostrar_casa(superheroes, 'Mujer Maravilla')

#     print('\ng. Información de Flash y Star-Lord')
#     mostrar_info(superheroes, 'Flash')
#     mostrar_info(superheroes, 'Star-Lord')

#     print('\nh. Superhéroes que comienzan con B, M y S')
#     listar_por_inicial(superheroes, 'BMS')

#     print('\ni. Cantidad de superhéroes por casa')
#     cant_marvel, cant_dc = contar_por_casa(superheroes)
#     print('   Marvel:', cant_marvel)
#     print('   DC:', cant_dc)






# #15) Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, 
# # cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además 
# # la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# # las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# # a. obtener la cantidad de Pokémons de un determinado entrenador;
# # b. listar los entrenadores que hayan ganado más de tres torneos;
# # c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# # d. mostrar todos los datos de un entrenador y sus Pokémos;
# # e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# # f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# # (tipo y subtipo);
# # g. el promedio de nivel de los Pokémons de un determinado entrenador;
# # h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# # i. mostrar los entrenadores que tienen Pokémons repetidos;
# # j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# # k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# # como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# # deberán mostrar los datos de ambos;


# #Ejercicio 15.
# class Entrenador(object):

#     def __init__(self, nombre, torneos_ganados, batallas_perdidas,
#                  batallas_ganadas):
#         self.nombre = nombre
#         self.torneos_ganados = torneos_ganados
#         self.batallas_perdidas = batallas_perdidas
#         self.batallas_ganadas = batallas_ganadas

#     def __str__(self):
#         return ('{} | torneos ganados: {} | batallas perdidas: {} | '
#                 'batallas ganadas: {}').format(
#                     self.nombre, self.torneos_ganados,
#                     self.batallas_perdidas, self.batallas_ganadas)


# class Pokemon(object):

#     def __init__(self, nombre, nivel, tipo, subtipo=None):
#         self.nombre = nombre
#         self.nivel = nivel
#         self.tipo = tipo
#         self.subtipo = subtipo

#     def __str__(self):
#         return '{} | nivel: {} | tipo: {} | subtipo: {}'.format(
#             self.nombre, self.nivel, self.tipo, self.subtipo)




# def cargar_entrenador(lista, entrenador):
#     #Inserta al entrenador (ordenado por nombre) y le crea su sublista.
#     insertar(lista, entrenador, 'nombre')
#     nodo = buscar(lista, entrenador.nombre, 'nombre')
#     nodo.sublista = Lista()


# def cargar_pokemon(lista, nombre_entrenador, pokemon):
#     #Inserta el Pokémon (ordenado por nombre) en la sublista del entrenador.
#     nodo = buscar(lista, nombre_entrenador, 'nombre')
#     if nodo is not None:
#         insertar(nodo.sublista, pokemon, 'nombre')
#         return True
#     return False




# # a. cantidad de Pokémons de un entrenador
# def cantidad_pokemons(lista, nombre_entrenador):
#     nodo = buscar(lista, nombre_entrenador, 'nombre')
#     if nodo is not None:
#         return tamanio(nodo.sublista)
#     return None


# # b. entrenadores que ganaron más de tres torneos
# def mas_de_tres_torneos(lista):
#     aux = lista.inicio
#     while(aux is not None):
#         if aux.info.torneos_ganados > 3:
#             print(aux.info.nombre, '-', aux.info.torneos_ganados, 'torneos')
#         aux = aux.sig


# # c. Pokémon de mayor nivel del entrenador con más torneos ganados
# def pokemon_mayor_nivel_del_campeon(lista):
#     maximo = -1
#     aux = lista.inicio
#     while(aux is not None):
#         if aux.info.torneos_ganados > maximo:
#             maximo = aux.info.torneos_ganados
#         aux = aux.sig

#     aux = lista.inicio
#     while(aux is not None):
#         if aux.info.torneos_ganados == maximo:
#             mayor = None
#             poke = aux.sublista.inicio
#             while(poke is not None):
#                 if mayor is None or poke.info.nivel > mayor.nivel:
#                     mayor = poke.info
#                 poke = poke.sig
#             print(aux.info.nombre, '({} torneos)'.format(maximo))
#             print('   ', mayor if mayor else 'No tiene Pokémons')
#         aux = aux.sig


# # d. todos los datos de un entrenador y sus Pokémons
# def mostrar_entrenador(lista, nombre_entrenador):
#     nodo = buscar(lista, nombre_entrenador, 'nombre')
#     if nodo is not None:
#         print(nodo.info)
#         print('Pokémons:')
#         barrido(nodo.sublista)
#     else:
#         print('No se encontró al entrenador', nombre_entrenador)


# # e. entrenadores con porcentaje de batallas ganadas mayor a un valor
# def porcentaje_ganadas(entrenador):
#     total = entrenador.batallas_ganadas + entrenador.batallas_perdidas
#     if total == 0:
#         return 0
#     return entrenador.batallas_ganadas * 100 / total


# def mayor_porcentaje_batallas(lista, minimo):
#     aux = lista.inicio
#     while(aux is not None):
#         porcentaje = porcentaje_ganadas(aux.info)
#         if porcentaje > minimo:
#             print('{} - {:.1f}%'.format(aux.info.nombre, porcentaje))
#         aux = aux.sig


# # f. entrenadores con Pokémons de tipo fuego y planta, o agua/volador
# def tiene_tipo(sublista, tipo):
#     poke = sublista.inicio
#     while(poke is not None and poke.info.tipo != tipo):
#         poke = poke.sig
#     return poke is not None


# def tiene_tipo_subtipo(sublista, tipo, subtipo):
#     poke = sublista.inicio
#     while(poke is not None and
#           not (poke.info.tipo == tipo and poke.info.subtipo == subtipo)):
#         poke = poke.sig
#     return poke is not None


# def entrenadores_por_tipos(lista):
#     aux = lista.inicio
#     while(aux is not None):
#         fuego_y_planta = (tiene_tipo(aux.sublista, 'fuego') and
#                           tiene_tipo(aux.sublista, 'planta'))
#         agua_volador = tiene_tipo_subtipo(aux.sublista, 'agua', 'volador')
#         if fuego_y_planta or agua_volador:
#             print(aux.info.nombre)
#         aux = aux.sig


# # g. promedio de nivel de los Pokémons de un entrenador
# def promedio_nivel(lista, nombre_entrenador):
#     nodo = buscar(lista, nombre_entrenador, 'nombre')
#     if nodo is None or tamanio(nodo.sublista) == 0:
#         return None
#     suma = 0
#     poke = nodo.sublista.inicio
#     while(poke is not None):
#         suma += poke.info.nivel
#         poke = poke.sig
#     return suma / tamanio(nodo.sublista)


# # h. cuántos entrenadores tienen un determinado Pokémon
# def cuantos_tienen_pokemon(lista, nombre_pokemon):
#     cantidad = 0
#     aux = lista.inicio
#     while(aux is not None):
#         if buscar(aux.sublista, nombre_pokemon, 'nombre') is not None:
#             cantidad += 1
#         aux = aux.sig
#     return cantidad


# # i. entrenadores con Pokémons repetidos
# def con_pokemons_repetidos(lista):
#     aux = lista.inicio
#     while(aux is not None):
#         poke = aux.sublista.inicio
#         repetidos = []
#         while(poke is not None and poke.sig is not None):
#             if (poke.info.nombre == poke.sig.info.nombre and
#                     poke.info.nombre not in repetidos):
#                 repetidos.append(poke.info.nombre)
#             poke = poke.sig
#         if repetidos:
#             print(aux.info.nombre, '- repetidos:', ', '.join(repetidos))
#         aux = aux.sig


# # j. entrenadores que tengan alguno de los Pokémons indicados
# def con_alguno_de(lista, nombres_pokemon):
#     aux = lista.inicio
#     while(aux is not None):
#         encontrados = []
#         for nombre in nombres_pokemon:
#             if buscar(aux.sublista, nombre, 'nombre') is not None:
#                 encontrados.append(nombre)
#         if encontrados:
#             print(aux.info.nombre, '-', ', '.join(encontrados))
#         aux = aux.sig


# # k. determinar si el entrenador X tiene al Pokémon Y y mostrar los datos de ambos
# def tiene_pokemon(lista, nombre_entrenador, nombre_pokemon):
#     nodo = buscar(lista, nombre_entrenador, 'nombre')
#     if nodo is None:
#         print('No se encontró al entrenador', nombre_entrenador)
#         return
#     poke = buscar(nodo.sublista, nombre_pokemon, 'nombre')
#     if poke is None:
#         print('{} no tiene a {}'.format(nombre_entrenador, nombre_pokemon))
#     else:
#         print('{} tiene a {}'.format(nombre_entrenador, nombre_pokemon))
#         print('   Entrenador:', nodo.info)
#         print('   Pokémon:   ', poke.info)


# def cargar_datos(lista):
#     entrenadores = [
#         Entrenador('Ash', 4, 20, 80),
#         Entrenador('Misty', 1, 10, 30),
#         Entrenador('Brock', 2, 5, 20),
#         Entrenador('Cynthia', 7, 3, 97),
#         Entrenador('Lance', 5, 12, 38),
#         Entrenador('Red', 9, 1, 99),
#     ]
#     for entrenador in entrenadores:
#         cargar_entrenador(lista, entrenador)

#     pokemons = [
#         ('Ash', Pokemon('Pikachu', 35, 'electrico')),
#         ('Ash', Pokemon('Charizard', 50, 'fuego', 'volador')),
#         ('Ash', Pokemon('Bulbasaur', 30, 'planta', 'veneno')),
#         ('Misty', Pokemon('Staryu', 30, 'agua')),
#         ('Misty', Pokemon('Starmie', 41, 'agua', 'psiquico')),
#         ('Misty', Pokemon('Wingull', 20, 'agua', 'volador')),
#         ('Brock', Pokemon('Onix', 28, 'roca', 'tierra')),
#         ('Brock', Pokemon('Tyrantrum', 44, 'roca', 'dragon')),
#         ('Brock', Pokemon('Vulpix', 22, 'fuego')),
#         ('Cynthia', Pokemon('Garchomp', 78, 'dragon', 'tierra')),
#         ('Cynthia', Pokemon('Lucario', 70, 'acero', 'lucha')),
#         ('Cynthia', Pokemon('Terrakion', 66, 'roca', 'lucha')),
#         ('Cynthia', Pokemon('Togekiss', 72, 'hada', 'volador')),
#         ('Lance', Pokemon('Dragonite', 62, 'dragon', 'volador')),
#         ('Lance', Pokemon('Gyarados', 58, 'agua', 'volador')),
#         ('Lance', Pokemon('Gyarados', 55, 'agua', 'volador')),
#         ('Lance', Pokemon('Aerodactyl', 60, 'roca', 'volador')),
#         ('Red', Pokemon('Pikachu', 81, 'electrico')),
#         ('Red', Pokemon('Charizard', 84, 'fuego', 'volador')),
#         ('Red', Pokemon('Venusaur', 82, 'planta', 'veneno')),
#         ('Red', Pokemon('Blastoise', 80, 'agua')),
#         ('Red', Pokemon('Snorlax', 79, 'normal')),
#     ]
#     for nombre_entrenador, pokemon in pokemons:
#         cargar_pokemon(lista, nombre_entrenador, pokemon)


# if __name__ == '__main__':
#     entrenadores = Lista()
#     cargar_datos(entrenadores)

#     print('a. Cantidad de Pokémons de Cynthia')
#     print('  ', cantidad_pokemons(entrenadores, 'Cynthia'))

#     print('\nb. Entrenadores con más de tres torneos ganados')
#     mas_de_tres_torneos(entrenadores)

#     print('\nc. Pokémon de mayor nivel del entrenador con más torneos')
#     pokemon_mayor_nivel_del_campeon(entrenadores)

#     print('\nd. Datos de Lance y sus Pokémons')
#     mostrar_entrenador(entrenadores, 'Lance')

#     print('\ne. Entrenadores con más de 79% de batallas ganadas')
#     mayor_porcentaje_batallas(entrenadores, 79)

#     print('\nf. Entrenadores con Pokémons fuego y planta, o agua/volador')
#     entrenadores_por_tipos(entrenadores)

#     print('\ng. Promedio de nivel de los Pokémons de Red')
#     print('  ', promedio_nivel(entrenadores, 'Red'))

#     print('\nh. Cantidad de entrenadores con Charizard')
#     print('  ', cuantos_tienen_pokemon(entrenadores, 'Charizard'))

#     print('\ni. Entrenadores con Pokémons repetidos')
#     con_pokemons_repetidos(entrenadores)

#     print('\nj. Entrenadores con Tyrantrum, Terrakion o Wingull')
#     con_alguno_de(entrenadores, ['Tyrantrum', 'Terrakion', 'Wingull'])

#     print('\nk. ¿Ash tiene a Pikachu? ¿Misty tiene a Pikachu?')
#     tiene_pokemon(entrenadores, 'Ash', 'Pikachu')
#     tiene_pokemon(entrenadores, 'Misty', 'Pikachu')

