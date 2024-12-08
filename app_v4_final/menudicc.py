import json
import funciones as f

# Declaramos listas, tuplas, matrices y diccionarios que se usan en el programa.
# Tupla de los meses del año.
tuplaMeses=('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
#Las categorías deberían ser guardadas en un archivo para no perder las nuevas o las modificaciones que se hacen
#categorias=['Alimentación', 'Alquiler', 'Entretenimiento', 'Transporte', 'Estudios', 'Salud','Servicios']
#Pre cargo una lista de gastos para las prueabas
matrizGastos=f.cargarMatriz('matrizGastos.csv')
diccionarioGastos = {}
'''descripcionCategorias={
    'Alimentación':'Gastos relacionados a la alimentación como supermercado, almacen, verdulería.', 
    'Alquiler':'Gastos de alquiler o renta del lugar de vivir o para automotores, depósitos, etc...', 
    'Entretenimiento':'Gastos de diversión como por ejemplo cine, teatro, vacaciones.', 
    'Transporte':'Viaticos relacionados a la movilidad regular del mes como son la Sube, larga distancia, tren, etc...', 
    'Estudios':'Los gastos de estudios como son la universidad, cursos, talleres.', 
    'Salud':'Gastos de la medicina o relacionados como son los medicamentos.',
    'Servicios':'Los gastos fijos inherentes a la vivienda, cochera, depósito.'
    }'''
descripcionCategorias = f.cargarCategorias('categorias.json')

def cargarMenuJson():
    try:
        fo = open('menu.json', 'r', encoding='utf-8')
        submenu = json.load(fo)
        fo.close()
        menu = {
        0: 'Mostrar Menú Completo', 
        1: 'Cargar nuevo gasto',
        2: {'Ver gastos': submenu['gastosOpciones']},
        3: {'Ver/Editar lista de categorías': submenu['categoriasOpciones']},
        4: {'Editar gasto': submenu['editarGastoOpciones']},
        9: 'Salir'
        }
        return menu
    except FileNotFoundError as e:
        cadena = f'No se pudo encontrar el archivo para la carga del Menú. Error: {e}'
        print(cadena)
        f.escribirErrores('error.log', cadena)
        print('No se puede continuar. Se apaga el programa. Disculpe las molestias.')
        return -1


def imprimirMenu(menu, nivel=0):
    for opcion, detalles in menu.items():
        if type(detalles) == dict:
            # Si es un submenú, se imprime el nombre de la opción y se llama a la función recursivamente
            if nivel == 0:
                print(str(opcion) + " - " + list(detalles.keys())[0])
            imprimirMenu(detalles, nivel + 1)
        else:
            print("\t" * nivel + str(opcion) + " - " + detalles)

def menuDicc(menu):
    for k,v in menu.items():
        #print(type(menu[k]), menu[k] )
        if type(menu[k]) == dict:
            for k1,v1 in menu[k].items():
                print(f'{k}: {k1}')
        else:
            print(f'{k}: {v}')

def subMenuDicc(menu, opcion):
    try: 
        if type(menu[opcion]) == dict:
            key = list(menu[opcion])[0]
            for k,v in menu[opcion][key].items():
                print(f'{opcion}{k}: {v}')   
        else:
            print(f'{opcion}: {menu[opcion]}')
    except KeyError as e:
        print(f'Error en la opción: {e}')
        print('Volver al menú anterior')
        menuDicc(menu)
        print('   -----------------------   ')
        f.escribirErrores('error.log', f'subMenuDicc funcion: Error en la opción: {e}')

def runFuncion(menu, opcion):
    if opcion % 10 == 9:
        print('Volver al menú anterior')
        menuDicc(menu)
        print('   -----------------------   ')
    elif opcion == 0:
        print('Menu Completo')
        imprimirMenu(menu)
        print()
    elif opcion == 1:
        print('Cargar nuevo gasto')
        op=False
        while not op:
            op=f.cargarNuevoGasto(matrizGastos,descripcionCategorias, tuplaMeses, diccionarioGastos)
        menuDicc(menu) # Vuelve a menú completo
        print()
    elif opcion == 3:
        print('Ver lista de categorías')
        menuDicc(menu)
    elif opcion == 4:
        print('Editar lista de categorías')
    elif opcion == 5:
        print('Editar gasto')
    elif opcion == 21:
        print('Total gastos por categorias')
        f.totalGastosPorCategoria(matrizGastos)
        print('2 - Ver gastos')
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 22:
        print('Gastos por mes')
        f.totalGastosPorMes(diccionarioGastos)
        print('2 - Ver gastos')        
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 23:
        print('Gastos por mes por categoría')
        mes=input('Ingrese el mes en LETRAS a consultar: ').lower()
        f.mostrarGastosPorMes(diccionarioGastos, mes)
        print('2 - Ver gastos')
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 24:
        print('Gastos por ID\n')
        id=int(input('Ingrese el ID que quiere buscar:'))
        f.buscarGastoPorId(matrizGastos, id)
        print('2 - Ver gastos')
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 25:
        print('Gastos por fecha')
        print()
        fecha=input('Ingrese la fecha a buscar con el formato: YYYY-MM-DD')
        # fecha a tupla
        fecha = fecha.split('-')
        fecha = tuple(map(int, fecha))
        f.buscarGastoPorFecha(matrizGastos, fecha)
        print('2 - Ver gastos')
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 26:
        print('Gastos por rango de importe')
        print()
        minimo=int(input('Ingrese el mínimo importe del rango:'))
        maximo=int(input('Ingrese el máximo importe del rango:'))
        f.buscarGastosPorRangoImporte(matrizGastos, minimo, maximo)
        print('2 - Ver gastos')
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 27:
        print('Gastos por Categoria')
        print()
        f.buscarGastoPorCategoria(matrizGastos, descripcionCategorias)
        print('2 - Ver gastos')
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 28:
        print('Gastos eliminados')
        print()
        f.gastosEliminados(matrizGastos)
        print('2 - Ver gastos')
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 31:
        print(f'Ver Lista categorías')
        print()
        f.listaDeCategorias(descripcionCategorias)
        print('\n3 - Ver/Editar lista de categorías')
        subMenuDicc(menu, 3) # Menu gastos
        print()
    elif opcion == 32:
        print('Crear nueva categoría')
        f.nuevaCategoria(descripcionCategorias)
        print()
        f.listaDeCategorias(descripcionCategorias)
        print('\n3 - Ver/Editar lista de categorías')
        subMenuDicc(menu, 3) # Menu gastos
        print()
    elif opcion == 33:
        print('Eliminar una categoría')
        print('Nombre de categoria en letras, respetar mayusculas. ')
        categoria = input('Ingrese la categoría a eliminar: ')
        f.eliminarCategoria(descripcionCategorias, categoria)
        print()
        f.listaDeCategorias(descripcionCategorias)
        print('\n3 - Ver/Editar lista de categorías')
        subMenuDicc(menu, 3)
        print()
    elif opcion == 34:    
        print('Editar una categoría')
        print('Nombre de categoria en letras, respetar mayusculas. ')
        categoria = input('Ingrese la categoría a editar: ')
        while categoria not in f.obtenerCategorias():
            print('Categoria a Editar no encontrada')
            categoria = input('Ingrese la categoría a editar de nuevo: ')
        f.editarCategoria(descripcionCategorias, categoria)
        print()
        f.listaDeCategorias(descripcionCategorias)
        print('\n3 - Ver/Editar lista de categorías')
        subMenuDicc(menu, 3)
        print()
    elif opcion == 35:
        print('Ver lista de categorías con gastos')
        print()
        lista = f.obtenerCategoriasEnUso(matrizGastos)
        for e in lista:
            print(f'{e}', end=' ')
        print('\n3 - Ver/Editar lista de categorías')
        subMenuDicc(menu, 3)
        print ()

    elif opcion == 41:
        print('Elimiar gasto por ID')
        id = int(input('Ingrese el ID del gasto a eliminar: '))
        f.eliminarGastoId(matrizGastos, id, tuplaMeses, diccionarioGastos)
        print('\n4 - Editar gasto')
        subMenuDicc(menu, 4)
        print()
    elif opcion == 42:
        print('Editar gasto por ID')
        id = int(input('Ingrese el ID del gasto a editar: '))
        f.editarGastoId(matrizGastos, id, descripcionCategorias, tuplaMeses, diccionarioGastos)
        print('\n4 - Editar gasto')
        subMenuDicc(menu, 4)
        print()
    elif opcion == 43:
        print('eliminar gasto por fecha')
        f.eliminarGastoPorFecha(matrizGastos, tuplaMeses, diccionarioGastos)
        print('\n4 - Editar gasto')
        subMenuDicc(menu, 4)
        print()
    elif opcion == 44:
        print('Editar gasto por fecha')
        f.editarGastoPorFecha(matrizGastos, descripcionCategorias, tuplaMeses, diccionarioGastos)
        print('\n4 - Editar gasto')
        subMenuDicc(menu, 4)
        print()
    else:
        print('Opcion No encontrada')
        menuDicc(menu)
        print('   -----------------------   ')

