def menuMain():
    print("""Menú de opciones:
    1. Cargar nuevo gasto
    2. Ver gastos por mes
    3. Ver gastos por mes y categoría
    4. Ver gastos por categoría
    5. Ver lista de categorías
    6. Editar lista de categorías
    7. Editar gasto
    8. Eliminar gasto
    9. Salir""")

def menuCategorias():
    print('\nElija una opción:\n1 - Ver categorias.\n2 - Agregar una categoría nueva.\n3 - Eliminar una categoria\n4 - Volver al menú.')
    print('Eliminar una categoría no elimina el gasto ya cargado en la misma.\nPara eso debe ir a editar el gasto.\n')

def listaDeCategorias(categorias):
    print('Categorias: \n')
    for categoria in categorias:
        print(categoria)
    menuMain()

def editarListaDeCategorias(categorias):
    menuCategorias()
    opcionCat=int(input('Ingrese la opción deseada: '))
    while opcionCat!=4:
        if opcionCat==1:
            print('Categorias: \n')
            for categoria in categorias:
                print(categoria)
            menuCategorias()
            opcionCat=int(input('Ingrese la opción deseada: '))

        elif opcionCat==2:
            nuevaCategoria=input('Ingrese el nombre de la nueva Categoría: ')
            categorias.append(nuevaCategoria)
            menuCategorias()
            opcionCat=int(input('Ingrese la opción deseada: '))

        elif opcionCat==3:
            print('Categorias: \n')
            i=0
            for categoria in categorias:
                i+=1
                print(f'{i} - ',categoria)
            eliminarCategoria=int(input('Ingrese el número de la categoría que desea eliminar de la lista: '))
            print(f'La categoría a eliminar es: {categorias[eliminarCategoria-1]}')
            categorias.pop(eliminarCategoria-1)
            menuCategorias()  
            opcionCat=int(input('Ingrese la opción deseada: '))    

        elif opcionCat==4:
            return 0
        else:
            print('La opción ingresada no es válida.\nIngrese nuevamente.') 
            opcionCat=int(input('Ingrese la opción deseada: '))
    menuMain()


# Cuerpo principal, imprimimos el menú general.

mesAno=('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
categorias=['Aliminetación', 'Alquiler', 'Entretenimiento', 'Transporte', 'Estudios', 'Salud','Servicios']


menuMain()
opcion=int(input('Ingrese la opción deseada: '))
while opcion!=9:
    if opcion==1:
        cargarNuevoGasto()
    elif opcion==2: 
        gastosPorMes()
    elif opcion==3:
        gastosPorMesCategoria()
    elif opcion==4:
        gastosPorCategoria()
    elif opcion==5:
        listaDeCategorias(categorias)
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==6:
        editarListaDeCategorias(categorias)
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==7:
        editarGasto()
    elif opcion==8:
        eliminarGasto()
    elif opcion==9:
        print(f'¡Gracias por elejirnos!\n')
    else:
        print('El valor ingresado no es un menú válido. Por favor ingrese nuevamente.')
