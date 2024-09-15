def menuMain():
    print("""\nMenú de opciones:
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
    print("""\nElija una opción:
          1 - Ver categorias.
          2 - Agregar una categoría nueva.
          3 - Eliminar una categoria
          4 - Editar descripción de una categoría.
          5 - Volver al menú.
Eliminar una categoría no elimina el gasto ya cargado en la misma.\nPara eso debe ir a editar el gasto.""")

def listaDeCategorias(categorias, descripcionCategorias):
    print('Categorias: \n')
    i=0
    for categoria in categorias:
        i+=1
        print(f'{i} - {categoria} : {descripcionCategorias[categoria]}')


# Edita la lista de categorías
def editarListaDeCategorias(categorias,descripcionCategorias):
    menuCategorias()
    opcionCat=int(input('Ingrese la opción deseada: '))
    while opcionCat!=5:
        if opcionCat==1:
            listaDeCategorias(categorias, descripcionCategorias)
            menuCategorias()
            opcionCat=int(input('Ingrese la opción deseada: '))
        elif opcionCat==2:
            nuevaCategoria=input('Ingrese el nombre de la nueva Categoría: ')
            categorias.append(nuevaCategoria)
            descripcionCategorias[nuevaCategoria]=input(f'Agregar nueva descripción para la categoría {nuevaCategoria}: ')
            menuCategorias()
            opcionCat=int(input('Ingrese la opción deseada: '))
        elif opcionCat==3:
            listaDeCategorias(categorias, descripcionCategorias)
            eliminarCategoria=int(input('Ingrese el número de la categoría que desea eliminar de la lista: '))
            print(f'La categoría a eliminar es: {categorias[eliminarCategoria-1]}')
            categorias.pop(eliminarCategoria-1)
            menuCategorias()  
            opcionCat=int(input('Ingrese la opción deseada: '))    
        elif opcionCat==4:
            listaDeCategorias(categorias, descripcionCategorias)
            editarDescripcion=int(input('Ingrese el número de la categoría de la lista que desea editar su descripcion: ')) 
            descripcionCategorias[categorias[editarDescripcion]]=input(f'Ingrese la descripción nueva para la categoria {categorias[editarDescripcion]}: ')
            menuCategorias()  
            opcionCat=int(input('Ingrese la opción deseada: '))              
        elif opcionCat==5:
            return 0
        else:
            print('La opción ingresada no es válida.\nIngrese nuevamente.') 
            opcionCat=int(input('Ingrese la opción deseada: '))

# Carga nuevo gasto y asigna un ID único 
def cargarNuevoGasto(categorias, listaGastos, mastrizGastos):
    print('\nPara cargar un gasto debe completar Fecha (YYYY-MM-DD), Monto del gasto y Categoría.\nLas categorías posibles son:\n')
    id=listaGastos[-1][0]+1
    fechaGasto=input('Fecha en formato YYYY-MM-DD: ')
    importeGasto=float(input('Importe del gasto: '))
    listaDeCategorias(categorias)
    categoriaGasto=int(input('De la lista de categorias indique el número de la misma para seleccionarla: '))
    gastoNuevo=[id,fechaGasto,importeGasto,categorias[categoriaGasto-1]]
    listaGastos.append(gastoNuevo)
    print(listaGastos)
    # llamar a la función que re sumariza en la matriz

# Elimina Gasto por FECHA 
def eliminarGasto(listaGastos, matrizGastos): 
    gastosPorFecha=[]
    fechaEliminar=input('\nIngrese la fecha del gasto a eliminar: ')
    for gasto in listaGastos:
        if gasto[1]==fechaEliminar:
            gastosPorFecha.append(gasto)
    if not gastosPorFecha:
        print('\nNo hay gastos para la fecha ',fechaEliminar)
    else:
        print('Los gastos que coinciden con esa fecha son:\n', gastosPorFecha)
        numEliminar=int(input('Ingrese el ID del gasto a eliminar: \n'))
        listaGastos.pop(numEliminar-1)
    print(listaGastos)
    # llamar a la función que re sumariza en la matriz

# Edita Gasto por FECHA 
def editarGasto(listaGastos, matrizGastos):
    gastosPorFecha=[]
    fechaModificar=input('\nIngrese la fecha del gasto a editar: ')
    for gasto in listaGastos:
        if gasto[1]==fechaModificar:
            gastosPorFecha.append(gasto)
    if not gastosPorFecha:
        print('\nNo hay gastos para la fecha ',fechaModificar)
    else:
        print('Los gastos que coinciden con esa fecha son:\n', gastosPorFecha)
        numEditar=int(input('Ingrese el ID del gasto a editar: \n'))
        queEdita=int(input('\n ¿Qué desea editar?\n1 - Fecha\n2 - Monto\n3 - Categoría\nIngrese la opcion: '))
        if queEdita==1:
            for gasto in listaGastos:
                if gasto[0]==numEditar:
                    gasto[1]=input('Ingrese Nueva fecha: ')
        elif queEdita==2:
            for gasto in listaGastos:
                if gasto[0]==numEditar:
                    gasto[2]=input('Ingrese Nuevo monto: ')
        elif queEdita==3:
            for gasto in listaGastos:
                if gasto[0]==numEditar:
                    listaDeCategorias(categorias)
                    nuevaCategoria=int(input('Ingrese el número de categoría: '))
                    gasto[3]=categorias[nuevaCategoria-1]
        else:
            queEdita=int(input('Opción ingresada es inválida. Ingrese nuevamente: '))
    print(listaGastos)


# Cuerpo principal:

mesAno=('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
#Las categorías deberían ser guardadas en un archivo para no perder las nuevas o las modificaciones que se hacen
categorias=['Aliminetación', 'Alquiler', 'Entretenimiento', 'Transporte', 'Estudios', 'Salud','Servicios']
#Pre cargo una lista de gastos para las prueabas
listaGastos=[[1, '2024-03-23', 200.45, 'Salud'], [2, '2024-03-23', 120.00, 'Alquiler'], [3, '2024-03-23', 100.5, 'Salud'], [4, '2024-03-23', 715.55, 'Servicios']]
# Matriz donde sumarizamos los gastos por mes
matrizGastos={}
#Debemos guardar las descripciones del diccionario en un archivo descripcionesCategorias. Mientras la precargo para probar.
descripcionCategorias={
    'Aliminetación':'Gastos relacionados a la alimentación como supermercado, almacen, verdulería.', 
    'Alquiler':'Gastos de alquiler o renta del lugar de vivir o para automotores, depósitos, etc...', 
    'Entretenimiento':'Gastos de diversión como por ejemplo cine, teatro, vacaciones.', 
    'Transporte':'Viaticos relacionados a la movilidad regular del mes como son la Sube, larga distancia, tren, etc...', 
    'Estudios':'Los gastos de estudios como son la universidad, cursos, talleres.', 
    'Salud':'Gastos de la medicina o relacionados como son los medicamentos.',
    'Servicios':'Los gastos fijos inherentes a la vivienda, cochera, depósito.'
    }


menuMain()
opcion=int(input('Ingrese la opción deseada: '))
while opcion!=9:
    if opcion==1:
        cargarNuevoGasto(categorias, listaGastos, matrizGastos)
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))        
    elif opcion==2: 
        gastosPorMes()
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==3:
        gastosPorMesCategoria()
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==4:
        gastosPorCategoria()
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==5:
        listaDeCategorias(categorias, descripcionCategorias)
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==6:
        editarListaDeCategorias(categorias, descripcionCategorias)
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==7:
        editarGasto(listaGastos, matrizGastos)
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==8:
        eliminarGasto(listaGastos, matrizGastos)
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==9:
        print(f'¡Gracias por elejirnos!\n')
    else:
        print('El valor ingresado no es un menú válido. Por favor ingrese nuevamente.')




