import json
import os
import funciones as f

# Declaramos listas, tuplas, matrices y diccionarios que se usan en el programa.
# Tupla de los meses del año.
tuplaMeses=('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
#Las categorías deberían ser guardadas en un archivo para no perder las nuevas o las modificaciones que se hacen
categorias=['Alimentación', 'Alquiler', 'Entretenimiento', 'Transporte', 'Estudios', 'Salud','Servicios']
#Pre cargo una lista de gastos para las prueabas
matrizGastos=[[1, (2024, 3, 23), 200.45, 'Salud',True], [2, (2024, 3, 23), 120.0, 'Alquiler',True], [3, (2024, 3, 23), 100.5, 'Salud',True], [4, (2024, 3, 23), 715.55, 'Servicios',True], [5, (2024, 4, 23), 715.55, 'Servicios',True], [6, (2024, 9, 23), 715.55, 'Estudios',True]]
diccionarioGastos = {}
descripcionCategorias={
    'Alimentación':'Gastos relacionados a la alimentación como supermercado, almacen, verdulería.', 
    'Alquiler':'Gastos de alquiler o renta del lugar de vivir o para automotores, depósitos, etc...', 
    'Entretenimiento':'Gastos de diversión como por ejemplo cine, teatro, vacaciones.', 
    'Transporte':'Viaticos relacionados a la movilidad regular del mes como son la Sube, larga distancia, tren, etc...', 
    'Estudios':'Los gastos de estudios como son la universidad, cursos, talleres.', 
    'Salud':'Gastos de la medicina o relacionados como son los medicamentos.',
    'Servicios':'Los gastos fijos inherentes a la vivienda, cochera, depósito.'
    }

def cargarMenuJson():
    f = open('menu.json', 'r', encoding='utf-8')
    submenu = json.load(f)
    f.close()
    
    menu = {
    1: 'Cargar nuevo gasto',
    2: {'Ver gastos': submenu['gastosOpciones']},
    3: {'Ver lista de categorías': submenu['descripcionCategorias']},
    4: {'Editar lista de categorías': submenu['categoriasOpciones']},
    5: {'Editar gasto': submenu['editarGastoOpciones']},
    9: 'Salir'
    }
    
    return menu



def menuDicc(menu):
    #os.system('clear')
    for k,v in menu.items():
        #print(type(menu[k]), menu[k] )
        if type(menu[k]) == dict:
            for k1,v1 in menu[k].items():
                print(f'{k}: {k1}')
        else:
            print(f'{k}: {v}')

def subMenuDicc(menu, opcion): 
    if type(menu[opcion]) == dict:
        key = list(menu[opcion])[0]
        for k,v in menu[opcion][key].items():
            print(f'{opcion}{k}: {v}')   
    else:
        print(f'{opcion}: {menu[opcion]}')

def runFuncion(menu, opcion):
    if opcion % 10 == 9:
        print('Volver al menú anterior')
        menuDicc(menu)
        print('   -----------------------   ')
    elif opcion == 1:
        print('Cargar nuevo gasto')
        f.cargarNuevoGasto(categorias, matrizGastos,descripcionCategorias, tuplaMeses, diccionarioGastos)
        menuDicc(menu)
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
    elif opcion == 22:
        print('Gastos por mes')
        f.totalGastosPorMes(diccionarioGastos, tuplaMeses)
    elif opcion == 23:
        print('Gastos por mes por categoría')
        mes=input('Ingrese el mes en LETRAS a consultar: ')
        f.mostrarGastosPorMes(diccionarioGastos, mes)
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 24:
        print('Gastos por ID')
        print()
        id=int(input('Ingrese el ID que quiere buscar:'))
        f.buscarGastoPorId(matrizGastos, id)
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
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 26:
        print('Gastos por rango de importe')
        print()
        minimo=int(input('Ingrese el mínimo importe del rango:'))
        maximo=int(input('Ingrese el máximo importe del rango:'))
        f.buscarGastosPorRangoImporte(matrizGastos, minimo, maximo)
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 27:
        print('Gastos por Categoria')
        print()
        f.buscarGastoPorCategoria(matrizGastos, categorias, descripcionCategorias)
        subMenuDicc(menu, 2) # Menu gastos
        print()
    elif opcion == 31:
        clave = list(menu[3].keys())[0]
        valor = str(opcion%10)
        # Ver lista de categorías
        print(f'Lista categoría, ', menu[3][clave][valor])
    elif opcion == 32:
        print('Eliminar categoría')
    elif opcion == 51:
        print('Editar gasto')

    else:
        print('Opcion No encontrada')
        menuDicc(menu)
        print('   -----------------------   ')

