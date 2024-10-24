import json
import os

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
    os.system('clear')
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
    if opcion % 9 == 0:
        print('Volver al menú anterior')
        menuDicc()
        print('   -----------------------   ')
    elif opcion == 1:
        print('Cargar nuevo gasto')
    elif opcion == 2:
        print('Ver gastos')
    elif opcion == 3:
        print('Ver lista de categorías')
    elif opcion == 4:
        print('Editar lista de categorías')
    elif opcion == 5:
        print('Editar gasto')
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

# MAIN
menu = cargarMenuJson()
opcion = 0
menuDicc(menu)
print('   -----------------------   ')

while opcion!=9:
    opcion= int(input('Ingrese la opción deseada: '))
    if opcion < 10:
        subMenuDicc(menu, opcion)
    else:
        runFuncion(menu, opcion)
    print()
