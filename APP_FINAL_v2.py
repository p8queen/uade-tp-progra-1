# Declaramos listas, tuplas, matrices y diccionarios que se usan en el programa.
# Tupla de los meses del año.
tuplaMeses=('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
#Las categorías deberían ser guardadas en un archivo para no perder las nuevas o las modificaciones que se hacen
categorias=['Alimentación', 'Alquiler', 'Entretenimiento', 'Transporte', 'Estudios', 'Salud','Servicios']
#Pre cargo una lista de gastos para las prueabas
matrizGastos=[[1, (2024, 3, 23), 200.45, 'Salud',True], [2, (2024, 3, 23), 120.0, 'Alquiler',True], [3, (2024, 3, 23), 100.5, 'Salud',True], [4, (2024, 3, 23), 715.55, 'Servicios',True], [5, (2024, 4, 23), 715.55, 'Servicios',True], [6, (2024, 9, 23), 715.55, 'Estudios',True]]
diccionarioGastos = {}
#Debemos guardar las descripciones del diccionario en un archivo descripcionesCategorias. Mientras la precargo para probar.
descripcionCategorias={
    'Alimentación':'Gastos relacionados a la alimentación como supermercado, almacen, verdulería.', 
    'Alquiler':'Gastos de alquiler o renta del lugar de vivir o para automotores, depósitos, etc...', 
    'Entretenimiento':'Gastos de diversión como por ejemplo cine, teatro, vacaciones.', 
    'Transporte':'Viaticos relacionados a la movilidad regular del mes como son la Sube, larga distancia, tren, etc...', 
    'Estudios':'Los gastos de estudios como son la universidad, cursos, talleres.', 
    'Salud':'Gastos de la medicina o relacionados como son los medicamentos.',
    'Servicios':'Los gastos fijos inherentes a la vivienda, cochera, depósito.'
    }

def stringFechaAtupla(fecha):
    return tuple(map(int, fecha.split('-')))

def mostrarGastosPorMes(diccionarioGastos, mes):
    print(f'Gastos de {mes}:')
    for categoria in diccionarioGastos[mes]:
        total = sum(diccionarioGastos[mes][categoria])
        print(f'\t{categoria}: ${total}')

def totalGastosPorMes(diccionarioGastos, tuplaMeses):
    for mes in diccionarioGastos:
        total = 0
        for categoria in diccionarioGastos[mes]:
            total += sum(diccionarioGastos[mes][categoria])
        print(f'{mes}: ${total}')


def eliminarGastoId(matrizGastos, id):
    encontrado = False
    i=0
    while i < len(matrizGastos) and not encontrado:
        if matrizGastos[i][0] == id:
            matrizGastos[i][0] = 0
            encontrado = True
        i += 1
    crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)

def buscarGastosPorRangoImporte(matrizGasto, minimo, maximo):
    gastos = []
    for gasto in matrizGasto:
        if gasto[2] >= minimo and gasto[2] <= maximo:
            gastos.append(gasto)
    for gasto in gastos:
        print(f'ID: {gasto[0]} - Fecha: {gasto[1]} - Importe: ${gasto[2]} - Categoria: {gasto[3]}') 

def crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos):
    for gasto in matrizGastos:
        mes = tuplaMeses[gasto[1][1] - 1]
        categoria = gasto[3]
        importe = gasto[2]
        if mes not in diccionarioGastos:
            diccionarioGastos[mes] = {}
        if categoria not in diccionarioGastos[mes]:
            diccionarioGastos[mes][categoria] = []
        diccionarioGastos[mes][categoria].append(importe)

def buscarGastoPorId(matrizGastos, id): 
    for gasto in matrizGastos:
        if gasto[0] == id: 
            print(f'ID: {gasto[0]} - Fecha: {gasto[1]} - Importe: ${gasto[2]} - Categoria: {gasto[3]}')  

def listaDeCategoriasUnicas(matrizGastos): 
    categoria = [gasto[3] for gasto in matrizGastos]
    print(set(categoria))


def menuMain():
    print("""\nMenú de opciones:
        1. Cargar nuevo gasto.
        2. Ver gastos.
        3. Ver lista de categorías.
        4. Editar lista de categorías.
        5. Editar gasto.
        9. Salir""")

def menuCategorias():
    print("""\nElija una opción:
        1 - Ver categorias.
        2 - Agregar una categoría nueva.
        3 - Eliminar una categoria
        4 - Editar descripción de una categoría.
        5 - Obtener categorias en uso, es decir, que tengan gastos ingresados.
        9 - Volver al menú anterior.
Eliminar una categoría no elimina el gasto ya cargado en la misma.\nPara eso debe ir a editar el gasto.""")
    
def menuConsultarGastos():
        print("""\nElija como ver los gastos:
        1 - Total gastos por categorias.
        2 - Gastos por mes.
        3 - Gastos por mes por categoría.
        4 - Gastos por ID.
        5 - Gastos por fecha.
        6 - Gastos por rango de importe.
        7 - Gastos por Categoria.
        9 - Volver al menú anterior.\n""")
        
def menuEditarGastos():
    print("""\nIngrese la opción que quiere usar:
        1 - Eliminar gasto por ID.
        2 - Editar gasto por ID.
        3 - Eliminar gasto por Fecha.
        4 - Editar gasto por Fecha.
        9 - Volver al menú anterior.\n""")

def listaDeCategorias(categorias, descripcionCategorias):
    print('\nCategorias: \n')
    i=0
    for categoria in categorias:
        i+=1
        print(f'{i} - {categoria} : {descripcionCategorias[categoria]}')
        
def cargarNuevoGasto(categorias, matrizGastos,descripcionCategorias):
    print('\nPara cargar un gasto debe completar Fecha (YYYY-MM-DD), Monto del gasto y Categoría.\nLas categorías posibles son:\n')
    id=matrizGastos[-1][0]+1
    fechaGasto=input('Fecha en formato YYYY-MM-DD: ')
    importeGasto=float(input('Importe del gasto: '))
    listaDeCategorias(categorias,descripcionCategorias)
    categoriaGasto=int(input('De la lista de categorias indique el número de la misma para seleccionarla: '))
    gastoNuevo=[id,fechaGasto,importeGasto,categorias[categoriaGasto-1]]
    matrizGastos.append(gastoNuevo)
    crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)

def buscarGastoPorFecha(matrizGastos, fecha):
    gastosPorFecha=[]
    for gasto in matrizGastos:
        if gasto[1]==fecha:
            gastosPorFecha.append(gasto)
    if gastosPorFecha==[]:
        print(f'\nNo hay gastos para la fecha {fecha}')
    else:
        print(f'Los gastos que coinciden con {fecha} son:\n')
        i=0
        for gasto in gastosPorFecha:
            print(f'ID: {gastosPorFecha[i][0]} - Fecha: {gastosPorFecha[i][1]} - Importe: ${gastosPorFecha[i][2]} - Categoria:: {gastosPorFecha[i][3]}')
            i+=1

def eliminarGastoPorFecha(matrizGastos):
    gastosPorFecha=[]
    fechaEliminar=input('\nIngrese la fecha del gasto a eliminar: Formato YYYY-MM-DD')
    for gasto in matrizGastos:
        if gasto[1]==fechaEliminar:
            gastosPorFecha.append(gasto)
    if not gastosPorFecha:
        print('\nNo hay gastos para la fecha ',fechaEliminar)
    else:
        print('Los gastos que coinciden con esa fecha son:\n', gastosPorFecha)
        numEliminar=int(input('Ingrese el ID del gasto a eliminar: \n'))
        siNo = input(f'¿Está seguro que desea eliminar el gasto con ID {numEliminar}? (s/n): ')
        if siNo == 's':
            eliminarGastoId(matrizGastos, numEliminar)
        else:
            print('El gasto no fue eliminado.')
    crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)

def editarGastoPorFecha(matrizGastos, descripcionCategorias):
    gastosPorFecha=[]
    fechaModificar=input('\nIngrese la fecha del gasto a editar: Formato YYYY-MM-DD')
    for gasto in matrizGastos:
        if gasto[1]==fechaModificar:
            gastosPorFecha.append(gasto)
    if not gastosPorFecha:
        print('\nNo hay gastos para la fecha ',fechaModificar)
    else:
        print('Los gastos que coinciden con esa fecha son:\n', gastosPorFecha)
        numEditar=int(input('Ingrese el ID del gasto a editar: \n'))
        queEdita=int(input('\n ¿Qué desea editar?\n1 - Fecha\n2 - Monto\n3 - Categoría\nIngrese la opcion: '))
        if queEdita==1:
            for gasto in matrizGastos:
                if gasto[0]==numEditar:
                    gasto[1]=input('Ingrese Nueva fecha: ')
        elif queEdita==2:
            for gasto in matrizGastos:
                if gasto[0]==numEditar:
                    gasto[2]=input('Ingrese Nuevo monto: ')
        elif queEdita==3:
            for gasto in matrizGastos:
                if gasto[0]==numEditar:
                    listaDeCategorias(categorias,descripcionCategorias)
                    nuevaCategoria=int(input('Ingrese el número de categoría: '))
                    gasto[3]=categorias[nuevaCategoria-1]
        else:
            queEdita=int(input('Opción ingresada es inválida. Ingrese nuevamente: '))
    crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)

def consultarGastos(matrizGastos, categorias, tuplaMeses, descripcionCategorias, diccionarioGastos):
    menuConsultarGastos ()
    opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
    while opcion!=9:
        if opcion==1:
            totalGastosPorCategoria(matrizGastos)
            menuConsultarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==2:
            totalGastosPorMes(diccionarioGastos,tuplaMeses)
            menuConsultarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==3:
            mes=input('Ingrese el mes en LETRAS a consultar: ')
            mostrarGastosPorMes(diccionarioGastos, mes)
            menuConsultarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==4:
            id=int(input('Ingrese el ID que quiere buscar:'))
            buscarGastoPorId(matrizGastos, id)
            menuConsultarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==5:
            fecha=input('Ingrese la fecha a buscar con el formato: YYYY-MM-DD')
            buscarGastoPorFecha(matrizGastos, fecha)
            menuConsultarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==6:
            minimo=int(input('Ingrese el mínimo importe del rango:'))
            maximo=int(input('Ingrese el máximo importe del rango:'))
            buscarGastosPorRangoImporte(matrizGastos, minimo, maximo)
            menuConsultarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==7:
            buscarGastoPorCategoria(matrizGastos, categorias, descripcionCategorias)
            menuConsultarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==9:
            return 0
        else:
            print('La opción ingresada no es válida.\nIngrese nuevamente.') 
            opcion=int(input('Ingrese la opción deseada: '))

def editarListaDeCategorias(categorias,descripcionCategorias):
    menuCategorias()
    opcionCat=int(input('\nIngrese la opción deseada: '))
    while opcionCat!=9:
        if opcionCat==1:
            listaDeCategorias(categorias, descripcionCategorias)
            menuCategorias()
            opcionCat=int(input('\nIngrese la opción deseada: '))
        elif opcionCat==2:
            nuevaCategoria=input('\nIngrese el nombre de la nueva Categoría: ')
            categorias.append(nuevaCategoria)
            descripcionCategorias[nuevaCategoria]=input(f'\nAgregar nueva descripción para la categoría {nuevaCategoria}: ')
            menuCategorias()
            opcionCat=int(input('\nIngrese la opción deseada: '))
        elif opcionCat==3:
            listaDeCategorias(categorias, descripcionCategorias)
            eliminarCategoria=int(input('\nIngrese el número de la categoría que desea eliminar de la lista: '))
            print(f'\nLa categoría a eliminar es: {categorias[eliminarCategoria-1]}')
            categorias.pop(eliminarCategoria-1)
            menuCategorias()  
            opcionCat=int(input('\nIngrese la opción deseada: '))    
        elif opcionCat==4:
            listaDeCategorias(categorias, descripcionCategorias)
            editarDescripcion=int(input('\nIngrese el número de la categoría de la lista que desea editar su descripcion: ')) 
            descripcionCategorias[categorias[editarDescripcion-1]]=input(f'\nIngrese la descripción nueva para la categoria {categorias[editarDescripcion-1]}: ')
            menuCategorias()  
            opcionCat=int(input('\nIngrese la opción deseada: '))    
        elif opcionCat==5:
            listaDeCategoriasUnicas(matrizGastos)
            menuCategorias()  
            opcionCat=int(input('\nIngrese la opción deseada: '))    
        elif opcionCat==9:
            return 0
        else:
            print('\nLa opción ingresada no es válida.\nIngrese nuevamente.') 
            opcionCat=int(input('Ingrese la opción deseada: '))

def editarGastos(matrizGastos):
    menuEditarGastos ()
    opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
    while opcion!=9:
        if opcion==1:
            id=int(input('Ingrese el ID que quiere buscar:'))
            eliminarGastoId(matrizGastos, id)
            menuEditarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==2:
            id=int(input('Ingrese el ID que quiere buscar:'))
            editarGastoId(matrizGastos,id,descripcionCategorias)
            menuEditarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==3:
            eliminarGastoPorFecha(matrizGastos) 
            menuEditarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==4:
            editarGastoPorFecha(matrizGastos)
            menuEditarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==9:
            return 0
        else:
            print('La opción ingresada no es válida.\nIngrese nuevamente.') 
            opcion=int(input('Ingrese la opción deseada: '))            

def editarGastoId(matrizGastos, id, descripcionCategorias):
    queEdita=int(input('\n ¿Qué desea editar?\n1 - Fecha\n2 - Monto\n3 - Categoría\nIngrese la opcion: '))
    if queEdita==1:
        for gasto in matrizGastos:
            if gasto[0]==id:
               gasto[1]=input('Ingrese Nueva fecha con formato YYYY-MM-DD: ')
    elif queEdita==2:
        for gasto in matrizGastos:
            if gasto[0]==id:
               gasto[2]=input('Ingrese Nuevo monto: ')
    elif queEdita==3:
        for gasto in matrizGastos:
            if gasto[0]==id:
                listaDeCategorias(categorias,descripcionCategorias)
                nuevaCategoria=int(input('Ingrese el número de categoría nuevo: '))
                gasto[3]=categorias[nuevaCategoria-1]
    else:
        queEdita=int(input('Opción ingresada es inválida. Ingrese nuevamente: '))
    crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)

def buscarGastoPorCategoria(matrizGastos, categorias,descripcionCategorias):
    gastosPorCategoria=[]
    listaDeCategorias(categorias,descripcionCategorias)
    buscarCategoria=int(input('Ingrese el número de la categoría a buscar: '))
    for gasto in matrizGastos:
        if gasto[3]==categorias[buscarCategoria-1]:
            gastosPorCategoria.append(gasto)
    if gastosPorCategoria==[]:
        print(f'\nNo hay gastos para la categoría {categorias[buscarCategoria-1]}')
    else:
        print(f'Los gastos que coinciden con {categorias[buscarCategoria-1]} son:\n')
        j=0
        for gasto in gastosPorCategoria:
            print(f'ID: {gastosPorCategoria[j][0]} - Fecha: {gastosPorCategoria[j][1]} - Importe: ${gastosPorCategoria[j][2]} - Categoria:: {gastosPorCategoria[j][3]}')
            j+=1

def totalGastosPorCategoria(matrizGastos):
    totalPorCategoria={}
    for gasto in matrizGastos:
        imp=gasto[2]
        cat=gasto[3]
        if cat in totalPorCategoria:
            totalPorCategoria[cat]+=imp
        else:
            totalPorCategoria[cat]=imp
    print(f'Los gastos por categoría son: \n')
    for categoria, impTotal in totalPorCategoria.items():
        print(f'{categoria}: $ {impTotal}.')

# Main. 

crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)
menuMain()
opcion=int(input('Ingrese la opción deseada: '))
while opcion!=9:
    if opcion==1:
        cargarNuevoGasto(categorias, matrizGastos,descripcionCategorias)
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))        
    elif opcion==2: 
        consultarGastos(matrizGastos, categorias, tuplaMeses,descripcionCategorias,diccionarioGastos)
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==3:
        listaDeCategorias(categorias, descripcionCategorias)
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==4:
        editarListaDeCategorias(categorias, descripcionCategorias)
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==5:
        editarGastos(matrizGastos)
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))
    elif opcion==9:
        print(f'¡Gracias por elejirnos!\n')
    else:
        print('El valor ingresado no es un menú válido. Por favor ingrese nuevamente.')

        


