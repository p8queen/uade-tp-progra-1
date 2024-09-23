# funciones Gustavo 

def mostrarGastos (diccionarioGastos, mes):
    print(f'Gastos de {mes}:')
    # calcular sub totales por categorias 
    for categoria in diccionarioGastos[mes]:
        total = sum(diccionarioGastos[mes][categoria])
        print(f'\t{categoria}: {total}')

# obtener de diccionario el total de gastos de un mes
def totalGastosMes(diccionarioGastos, mes):
    total = 0
    for categoria in diccionarioGastos[mes]:
        total += sum(diccionarioGastos[mes][categoria]) # suma los importes de cada categoria
    print(f'Total de gastos de {mes}: ${total}')

def totalGastosPorMes(diccionarioGastos):
    for mes in tuplaMeses:
        print(f'{mes}: ${totalGastosMes(diccionarioGastos, mes)}')

def eliminarGasto(matrizGastos, id):
    encontrado = False
    i=0
    while i < len(matrizGastos) and not encontrado:
        if matrizGastos[i][0] == id:
            del matrizGastos[i]
            encontrado = True
        i += 1
    return encontrado

def buscarGastosPorRangoImporte(matrizGasto, minimo, maximo):
    gastos = []
    for gasto in matrizGasto:
        if gasto[2] >= minimo and gasto[2] <= maximo:
            gastos.append(gasto)
    for gasto in gastos:
        print(gasto)

# fin funciones Gustavo

# Funciones Pablo:

def imprimirOrdenado(diccionarioGastos): #Ordena alfabeticamente el contenido interno del diccionario
    for mes, categorias in diccionarioGastos.items():
        print(f"{mes.capitalize()}:")
        for categoria, importes in categorias.items():
            print(f"  {categoria}: {importes}")

def crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos):
    for linea in matrizGastos:
        # linea[0] es de la forma YYYY-MM-DD 
        mes = tuplaMeses[int(linea[1].split('-')[1]) - 1]
        concepto = linea[3]
        importe = linea[2]
        if mes not in diccionarioGastos:
            diccionarioGastos[mes] = {}
        if concepto not in diccionarioGastos[mes]:
            diccionarioGastos[mes][concepto] = []
        diccionarioGastos[mes][concepto].append(importe)
        
def buscarGastoPorId(matrizGastos, id): #Buscar el gasto por el registro id
    # Recorrer la matriz para buscar el gasto con el ID proporcionado
    for gasto in matrizGastos:
        if gasto[0] == id:  # El primer elemento de cada fila es el ID
            return gasto  # Devolver la fila completa si el ID coincide

def listaDeCategoriasUnicas(matrizGastos): 
    categoria = [x[3] for x in matriz]
    print(set(categoria))

# Fin funciones Pablo

# Menús que se imprimen generales:
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
        
# Carga nuevo gasto y asigna un ID único 
def cargarNuevoGasto(categorias, matrizGastos,descripcionCategorias):
    print('\nPara cargar un gasto debe completar Fecha (YYYY-MM-DD), Monto del gasto y Categoría.\nLas categorías posibles son:\n')
    id=matrizGastos[-1][0]+1
    fechaGasto=input('Fecha en formato YYYY-MM-DD: ')
    importeGasto=float(input('Importe del gasto: '))
    listaDeCategorias(categorias,descripcionCategorias)
    categoriaGasto=int(input('De la lista de categorias indique el número de la misma para seleccionarla: '))
    gastoNuevo=[id,fechaGasto,importeGasto,categorias[categoriaGasto-1]]
    matrizGastos.append(gastoNuevo)
    print(matrizGastos)

def buscarGastoPorFecha(matrizGastos, fecha):
    gastosPorFecha=[]
    i=0
    for gasto in matrizGastos:
        if gasto[i][1]==fecha:
            gastosPorFecha.append(gasto)
        i+=1
    if gastosPorFecha==[]:
        print(f'\nNo hay gastos para la fecha {fecha}')
    else:
        print(f'Los gastos que coinciden con {fecha} son:\n')
        i=0
        for gasto in gastosPorFecha:
            print(f'ID: {gastosPorFecha[i][0]} - Fecha: {gastosPorFecha[i][1]} - Importe:: {gastosPorFecha[i][2]} - Categoria:: {gastosPorFecha[i][3]}')
            i+=1

# Función menú para consultar gastos:
def consultarGastos(matrizGastos, categorias, tuplaMeses, descripcionCategorias):
    menuConsultarGastos ()
    opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
    while opcion!=9:
        if opcion==1:
            totalGastosPorCategoria(matrizGastos)
            menuConsultarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==2:
            totalGastosPorMes(matrizGastos)
            menuConsultarGastos ()
            opcion=int(input('Ingrese la opción de consulta de gastos que quiera usar:'))
        elif opcion==3:
            i=1
            for mes in tuplaMeses:
                print(f'{i} - {mes}')
                i+=1
            mes=int(input('Ingrese el número del mes a consultar: '))
            mostrarGastosPorMes (matrizGastos, mes)
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

# Edita la lista de categorías
def editarListaDeCategorias(categorias,descripcionCategorias):
    menuCategorias()
    opcionCat=int(input('\nIngrese la opción deseada: '))
    while opcionCat!=5:
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

# Función menú que edita/elimina gastos:
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
            editarGasto(matrizGastos,id)
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

# Edita Gasto pasando un ID
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

# Funcion para buscar por una categoria determinada los gastos
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
            print(f'ID: {gastosPorCategoria[j][0]} - Fecha: {gastosPorCategoria[j][1]} - Importe:: {gastosPorCategoria[j][2]} - Categoria:: {gastosPorCategoria[j][3]}')
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
# Declaramos listas, tuplas, matrices y diccionarios que se usan en el programa.
# Tupla de los meses del año.
tuplaMeses=('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
#Las categorías deberían ser guardadas en un archivo para no perder las nuevas o las modificaciones que se hacen
categorias=['Alimentación', 'Alquiler', 'Entretenimiento', 'Transporte', 'Estudios', 'Salud','Servicios']
#Pre cargo una lista de gastos para las prueabas
matrizGastos=[[1, '2024-03-23', 200.45, 'Salud'], [2, '2024-03-23', 120.00, 'Alquiler'], [3, '2024-03-23', 100.5, 'Salud'], [4, '2024-03-23', 715.55, 'Servicios']]
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

# Menú que selecciona la acción principal y llama a los demás sub menús del programa:
menuMain()
opcion=int(input('Ingrese la opción deseada: '))
while opcion!=9:
    if opcion==1:
        cargarNuevoGasto(categorias, matrizGastos)
        menuMain()
        opcion=int(input('Ingrese la opción deseada: '))        
    elif opcion==2: 
        consultarGastos(matrizGastos, categorias, tuplaMeses)
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



