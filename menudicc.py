descripcionCategorias={
    1:{'Alimentación':'Gastos relacionados a la alimentación como supermercado, almacen, verdulería.'}, 
    2:{'Alquiler':'Gastos de alquiler o renta del lugar de vivir o para automotores, depósitos, etc...'}, 
    3:{'Entretenimiento':'Gastos de diversión como por ejemplo cine, teatro, vacaciones.'}, 
    4:{'Transporte':'Viaticos relacionados a la movilidad regular del mes como son la Sube, larga distancia, tren, etc...'}, 
    5:{'Estudios':'Los gastos de estudios como son la universidad, cursos, talleres.'}, 
    6:{'Salud':'Gastos de la medicina o relacionados como son los medicamentos.'},
    7:{'Servicios':'Los gastos fijos inherentes a la vivienda, cochera, depósito.'},
    9: 'Volver al menú anterior'
    }

categoriasOpciones = {
    1: 'Ver categorias',
    2: 'Agregar una categoría nueva',
    3: 'Eliminar una categoria',
    4: 'Editar descripción de una categoría',
    5: 'Obtener categorias en uso, es decir, que tengan gastos ingresados',
    9: 'Volver al menú anterior'
}

editarGastoOpciones = {
    1: 'Eliminar gasto por ID',
    2: 'Editar gasto por ID',
    3: 'Eliminar gasto por Fecha',
    4: 'Editar gasto por Fecha',
    9: 'Volver al menú anterior'
    }

gastosOpciones = {
    1: 'Total gastos por categorias',
    2: 'Gastos por mes',
    3: 'Gastos por mes por categoría',
    4: 'Gastos por ID',
    5: 'Gastos por fecha',
    6: 'Gastos por rango de importe',
    7: 'Gastos por Categoria',
    9: 'Volver al menú anterior'
}
# crear diccionario con menu principal
menu = {
    1: 'Cargar nuevo gasto',
    2: {'Ver gastos': gastosOpciones},
    3: {'Ver lista de categorías': descripcionCategorias},
    4: {'Editar lista de categorías': categoriasOpciones},
    5: {'Editar gasto': editarGastoOpciones},
    9: 'Salir'
}

def runFuncion(opcion):
    if opcion == 1:
        print('Cargar nuevo gasto')
    elif opcion == 2:
        print('Ver gastos')
    elif opcion == 3:
        print('Ver lista de categorías')
    elif opcion == 21:
        print('Total gastos por categorias')
    elif opcion == 22:
        print('Gastos por mes')
    elif opcion == 23:
        print('Gastos por mes por categoría')
    elif opcion == 24:
        print('Gastos por ID')
    elif opcion == 25:
        print('Gastos por fecha')
    elif opcion == 26:
        print('Gastos por rango de importe')
    elif opcion == 27:
        print('Gastos por Categoria')
    elif opcion == 29:
        print('Volver al menú anterior')
        menuDicc()
        print('   -----------------------   ')
    else:
        print('Opcion No encontrada')
        menuDicc()
        print('   -----------------------   ')

def menuDicc():
    for k,v in menu.items():
        #print(type(menu[k]), menu[k] )
        if type(menu[k]) == dict:
            for k1,v1 in menu[k].items():
                print(f'{k}: {k1}')
        else:
            print(f'{k}: {v}')

def subMenuDicc(opcion): 
    if type(menu[opcion]) == dict:
        key = list(menu[opcion])[0]
        for k,v in menu[opcion][key].items():
            print(f'{opcion}{k}: {v}')   
    else:
        print(f'{opcion}: {menu[opcion]}')
         
opcion = 0
menuDicc()
print('   -----------------------   ')

while opcion!=9:
    opcion=int(input('Ingrese la opción deseada: '))
    if opcion < 10:
        subMenuDicc(opcion)
    else:
        runFuncion(opcion)
    print()
