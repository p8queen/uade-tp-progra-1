import json 
import re
import datetime

def cargarMatriz(archivo):
    matriz = []
    try:
        f = open(archivo, 'r', encoding='utf-8')
        for line in f:
            fila = line.strip().split(';')
            id = int(fila[0])
            # fila[1] es de la forma '(YYYY, MM, DD)'
            listaFecha = fila[1].strip('() ').split(',')
            fecha = tuple(map(int, listaFecha))
            importe = float(fila[2])
            activo = eval(fila[4]) #bool siempre devuelve True si el valor es distinto de ""
            matriz.append([id, fecha, importe, fila[3], activo])
        f.close()        
        return matriz
    except FileNotFoundError as e:
        cadena = f'No se encontró el archivo para cargar la matriz. Error: {e}'
        print(cadena)
        print('Se cargará una matriz de ejemplo.')
        escribirErrores('error.log', cadena)
        matrizGastos=[[1, (2024, 3, 23), 200.45, 'Salud',True], [2, (2024, 3, 23), 120.0, 'Alquiler',True], [3, (2024, 3, 23), 100.5, 'Salud',True], [4, (2024, 3, 23), 715.55, 'Servicios',True], [5, (2024, 4, 23), 715.55, 'Servicios',True], [6, (2024, 9, 23), 715.55, 'Estudios',True]]
        return matrizGastos
    except IndexError as e2:
        cadena = f'Archivo contiene fechas fuera de la Tupla Meses y no se puede cargar la matriz. Error: {e2}'
        print(cadena)
        escribirErrores('error.log', cadena)
        exit(1)

def escribirMatriz(archivo, matriz):
    try:
        f = open(archivo, 'w', encoding='utf-8')
        for fila in matriz:
            f.write(f'{fila[0]};{fila[1]};{fila[2]};{fila[3]};{fila[4]}\n')
        f.close()
        print('Matriz Gastos guardada en el archivo.\n')
    except FileNotFoundError as e:
        cadena = f'No se encontró el archivo para guardar la matriz. Error: {e}'
        print(cadena)
        escribirErrores('error.log', cadena)

def escribirErrores(archivo, errorMensaje):
    try:
        f = open(archivo, 'a', encoding='utf-8')
        fechaLog=datetime.datetime.now()
        f.write(f'{fechaLog} - {errorMensaje}\n')
        f.close()
        print('Errores guardados en el archivo.')
    except FileNotFoundError:
        print('No se encontró el archivo de errores.')

def cargarCategorias(archivo):
    try:
        f = open(archivo, 'r', encoding='utf-8')
        descripcionCategorias = json.load(f)
        f.close()
        return descripcionCategorias
    except FileNotFoundError as e:
        cadena = f'No se encontró el archivo cargarCategorias. Error: {e}'
        print(cadena)
        escribirErrores('error.log', cadena)
        return {}
    
def crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos):
    try:
        gastosActivos = filter(lambda gasto: gasto[4], matrizGastos)
        for gasto in gastosActivos:
            mes = tuplaMeses[gasto[1][1] - 1]
            categoria = gasto[3]
            importe = gasto[2]
            if mes not in diccionarioGastos:
                diccionarioGastos[mes] = {}
            if categoria not in diccionarioGastos[mes]:
                diccionarioGastos[mes][categoria] = []
                diccionarioGastos[mes][categoria].append(importe)
    except IndexError as e:
        cadena = f'Archivo contiene fechas fuera de la Tupla Meses y no se puede cargar la matriz. Error: {e}'
        print(cadena)
        escribirErrores('error.log', cadena)
        print ('Archivo origen de datos corrupto, no se puede continuar.\nContactar al administrador del sistema.')
        exit(1)
    except TypeError as e2:
        cadena = f'Fecha ingresada no es válida. Error: {e2}'
        print(cadena)
        escribirErrores('error.log', cadena)
        return False



def listaDeCategorias(descripcionCategorias):
    print('\nCategorias: \n')
    i=0
    for categoria in descripcionCategorias:
        i+=1
        print(f'{i} - {categoria} : {descripcionCategorias[categoria]}')

# Menu opciones  1    

def cargarFechaGasto():
    fechaGasto=input('Fecha en formato YYYY-MM-DD: ')
    patron = r'^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
    while not re.match(patron, fechaGasto):
        print('Formato de fecha incorrecto. Intente nuevamente.')
        fechaGasto=input('Fecha en formato YYYY-MM-DD: ')
    # fecha a tupla
    fechaGasto = fechaGasto.split('-')
    fechaGasto = tuple(map(int, fechaGasto))
    return fechaGasto

def cargarNuevoGasto(categorias, matrizGastos,descripcionCategorias, tuplaMeses, diccionarioGastos):
    print('\nPara cargar un gasto debe completar Fecha (YYYY-MM-DD), Monto del gasto y Categoría.\nLas categorías posibles son:\n')
    listaDeCategorias(descripcionCategorias)
    id=matrizGastos[-1][0]+1
    fechaGasto=cargarFechaGasto()
    importeGasto=float(input('Importe del gasto: '))
    categoriaGasto=int(input('De la lista de categorias indique el número de la misma para seleccionarla: '))
    try:
        gastoNuevo=[id,fechaGasto,importeGasto,categorias[categoriaGasto-1], True]
    except IndexError as e:
        cadena=f'Categoría ingresada fuera de la lista de opciones {e}'
        print(cadena)
        escribirErrores('error.log',cadena)
        print('Intente nuevamente.\n')
        return False
    matrizGastos.append(gastoNuevo)
    print(f'\nGasto {id} cargado.\n')
    buscarGastoPorId(matrizGastos, id)
    escribirMatriz('matrizGastos.csv', matrizGastos)
    crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)
    return True    

# Menu opciones de consulta de gastos 20 al 29
def totalGastosPorCategoria(matrizGastos):
    totalPorCategoria={}
    redondeo2 = lambda importe: round(importe, 2)
    # gasto[4] es el campo activo. False indica eliminado
    gastosActivos = filter(lambda gasto: gasto[4], matrizGastos)
    for gasto in gastosActivos:
        importe=gasto[2]
        categoria=gasto[3]
        if categoria in totalPorCategoria:
            totalPorCategoria[categoria]=redondeo2(totalPorCategoria[categoria] + importe)
        else:
            totalPorCategoria[categoria]=redondeo2(importe)
    print(f'Los gastos por categoría son: \n')
    for categoria, impTotal in totalPorCategoria.items():
        print(f'{categoria}: $ {impTotal}')
    print()
        
def totalGastosPorMes(diccionarioGastos, tuplaMeses):
    for mes in diccionarioGastos:
        total = 0
        for categoria in diccionarioGastos[mes]:
            total += sum(diccionarioGastos[mes][categoria])
        print(f'{mes}: ${total}')

def mostrarGastosPorMes(diccionarioGastos, mes):
    print(f'Gastos de {mes}:')
    try:
        for categoria in diccionarioGastos[mes]:
            total = sum(diccionarioGastos[mes][categoria])
            print(f'\t{categoria}: ${total}')
    except KeyError:
        print(f'\tNo hay gastos de {mes}.')

def buscarGastoPorId(matrizGastos, id):
    cadena = 'Id Gastado no encontrado'
    for gasto in matrizGastos:
        if gasto[0] == id: 
            cadena = f'ID: {gasto[0]} - Fecha: {gasto[1]} - Importe: ${gasto[2]} - Categoria: {gasto[3]} - activo: {gasto[4]}' 
            print (f'{cadena}\n')
            break
    return cadena

            
def buscarGastoPorFecha(matrizGastos, fecha):
    gastosPorFecha=[]
    gastosPorFecha = [gasto for gasto in matrizGastos if gasto[1] == fecha]
    if gastosPorFecha==[]:
        print(f'\nNo hay gastos para la fecha {fecha}')
    else:
        print(f'Los gastos que coinciden con {fecha} son:\n')
        i=0
        for gasto in gastosPorFecha:
            print(f'ID: {gastosPorFecha[i][0]} - Fecha: {gastosPorFecha[i][1]} - Importe: ${gastosPorFecha[i][2]} - Categoria:: {gastosPorFecha[i][3]}')
            i+=1

def buscarGastosPorRangoImporte(matrizGasto, minimo, maximo):
    gastos = []
    for gasto in matrizGasto:
        if gasto[2] >= minimo and gasto[2] <= maximo:
            gastos.append(gasto)
    for gasto in gastos:
        print(f'ID: {gasto[0]} - Fecha: {gasto[1]} - Importe: ${gasto[2]} - Categoria: {gasto[3]}') 

def buscarGastoPorCategoria(matrizGastos, categorias,descripcionCategorias):
    gastosPorCategoria=[]
    listaDeCategorias(descripcionCategorias)
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

# FIN - Menu opciones de consulta de gastos 20 al 29

# Menu opciones de consulta de categorías 30 al 39

def guardarCategorias(archivo, descripcionCategorias):
    try:
        f = open(archivo, 'w', encoding='utf-8')
        # escribir en formato json 
        json.dump(descripcionCategorias, f, indent=4)
        f.close()
        print('Categorías actualizadas en el archivo.')
    except FileNotFoundError as e:
        cadena = f'No se encontró el archivo guardarCategorias. Error: {e}'
        print(cadena)
        escribirErrores('error.log', cadena)
    

def nuevaCategoria(descripcionCategorias):
    nuevaCategoria=input('\nIngrese el nombre de la nueva Categoría: ')
    if nuevaCategoria in descripcionCategorias:
        print(f'La categoría {nuevaCategoria} ya existe.')
    else:
        descripcionCategorias[nuevaCategoria]=input(f'\nAgregar nueva descripción para la categoría {nuevaCategoria}: ')
        print(f'La nueva categoría {nuevaCategoria} ha sido agregada .')
        guardarCategorias('categorias.json', descripcionCategorias)

def eliminarCategoria(descripcionCategorias, categoria):
    try:
        del descripcionCategorias[categoria]
        print(f'La categoría {categoria} ha sido eliminada.')
        guardarCategorias('categorias.json', descripcionCategorias)
    except KeyError:
        print(f'La categoría {categoria} no existe.')

def obtenerCategorias():
    try:
        f = open('categorias.json', 'r', encoding='utf-8') 
        descripcionCategorias=json.load(f)
        f.close()
        return list(descripcionCategorias.keys())
    except FileNotFoundError as e:
        cadena = f'No se encontró el archivo guardarCategorias. Error: {e}'
        print(cadena)
        escribirErrores('error.log', cadena)
        return []

def editarCategoria(descripcionCategorias, categoria):
    try:
        nuevaDescripcion=input(f'Ingrese la nueva descripción para la categoría {categoria}: ')
        descripcionCategorias[categoria]=nuevaDescripcion
        print(f'La categoría {categoria} ha sido actualizada.')

        guardarCategorias('categorias.json', descripcionCategorias)
    except KeyError:
        print(f'La categoría {categoria} no existe.')

def obtenerCategoriasEnUso(matrizGastos):
    categoriasEnUso = []
    gastosActivos = filter(lambda gasto: gasto[4], matrizGastos)
    for gasto in gastosActivos:
        categoriasEnUso.append(gasto[3])
    return set(categoriasEnUso)

# escribir en el archivo de categorias


# FIN - Menu opciones de consulta de categorías 30 al 39

def eliminarGastoId(matrizGastos, id, tuplaMeses, diccionarioGastos):
    print('Gasto a eliminar:', buscarGastoPorId(matrizGastos, id))
    respuesta = input('¿Desea eliminar el gasto? (s/n): ')
    if respuesta.lower() == 'n':
        print('Operación cancelada.')
        return
    
    encontrado = False
    i=0
    while i < len(matrizGastos) and not encontrado:
        if matrizGastos[i][0] == id:
            matrizGastos[i][4] = False
            encontrado = True
        i += 1
    crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)
    print('Gasto eliminado.')
    escribirMatriz('matrizGastos.csv', matrizGastos)
    buscarGastoPorId(matrizGastos, id)

def editarGastoId(matrizGastos, id, descripcionCategorias, tuplaMeses, diccionarioGastos):
    print('Gasto a editar:')
    print(buscarGastoPorId(matrizGastos, id))
    queEdita=int(input('\n ¿Qué desea editar?\n1 - Fecha\n2 - Monto\n3 - Categoría\n4 - Deshacer Gasto Borrado \n0 - Cancelar. Volver al menu\n Ingrese la opcion: '))
    if queEdita==0:
        print('Operación cancelada.')
        return
    if queEdita==1:
        for gasto in matrizGastos:
            if gasto[0]==id:
               fechaEdit=cargarFechaGasto()
               gasto[1]=fechaEdit

    elif queEdita==2:
        for gasto in matrizGastos:
            if gasto[0]==id:
               gasto[2]=input('Ingrese Nuevo monto: ')
    elif queEdita==3:
        for gasto in matrizGastos:
            if gasto[0]==id:
                listaDeCategorias(descripcionCategorias)
                nuevaCategoria=input('Ingrese en letras, respetando mayusculas algunas de las categoría : ')
                noEncontrado=True
                while noEncontrado:
                    if nuevaCategoria in descripcionCategorias:
                        gasto[3]=nuevaCategoria
                        noEncontrado=False
                    if noEncontrado:
                        nuevaCategoria=input('Categoría no encontrada. Ingrese nuevamente: ')
    elif queEdita==4:
        for gasto in matrizGastos:
            if gasto[0]==id:
                gasto[4]=True
                break          
    else:
        queEdita=int(input('Opción ingresada es inválida. Ingrese nuevamente: (0 para salir)'))
    buscarGastoPorId(matrizGastos, id)
    crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)

def obtenerGastosPorFecha(matrizGastos):
    gastosPorFecha=[]
    fechaEliminar=input('\nIngrese la fecha del gasto a eliminar: Formato YYYY-MM-DD')
    # fecha a tupla
    fecha = fechaEliminar.split('-')
    fecha = tuple(map(int, fecha))
    gastosPorFecha = [gasto for gasto in matrizGastos if gasto[1] == fecha]
    return gastosPorFecha

def gastosEliminados(matrizGasto):
    gastosEliminados = []
    for gasto in matrizGasto:
        if not gasto[4]:
            gastosEliminados.append(gasto)
    for gasto in gastosEliminados:
        print(f'ID: {gasto[0]} - Fecha: {gasto[1]} - Importe: ${gasto[2]} - Categoria: {gasto[3]}')

def eliminarGastoPorFecha(matrizGastos, tuplaMeses, diccionarioGastos):
    gastosPorFecha=obtenerGastosPorFecha(matrizGastos)
    
    if not gastosPorFecha:
        print('\nNo hay gastos para la fecha seleccionada.')
    else:
        print('Los gastos que coinciden con la fecha son:')
        for gasto in gastosPorFecha:
            print(f'ID: {gasto[0]} - Fecha: {gasto[1]} - Importe: ${gasto[2]} - Categoria: {gasto[3]} - activo: {gasto[4]}')
        
        print('se solicitará confirmar la eliminación del gasto con el ID correspondiente.')
        numEliminar=int(input('Ingrese el ID del gasto a eliminar: \n'))
        while numEliminar not in [gasto[0] for gasto in gastosPorFecha]:
            print('El ID ingresado no corresponde a un gasto de la fecha indicada.')
            numEliminar=int(input('Ingrese el ID del gasto a eliminar: \n'))
    
        eliminarGastoId(matrizGastos, numEliminar, tuplaMeses, diccionarioGastos)

def editarGastoPorFecha(matrizGastos, descripcionCategorias, tuplaMeses, diccionarioGastos):
    gastosPorFecha=obtenerGastosPorFecha(matrizGastos)
    if not gastosPorFecha:
        print('\nNo hay gastos para la fecha seleccionada.')
    else:
        print('Los gastos que coinciden con la fecha son:')
        for gasto in gastosPorFecha:
            print(f'ID: {gasto[0]} - Fecha: {gasto[1]} - Importe: ${gasto[2]} - Categoria: {gasto[3]} - activo: {gasto[4]}')
        
        numEditar=int(input('Ingrese el ID del gasto a editar: \n'))
        while numEditar not in [gasto[0] for gasto in gastosPorFecha]:
            print('El ID ingresado no corresponde a un gasto de la fecha indicada.')
            numEditar=int(input('Ingrese el ID del gasto a editar: \n'))
        editarGastoId(matrizGastos, numEditar, descripcionCategorias, tuplaMeses, diccionarioGastos)       



# FIN - Menu opciones  gastos 40 al 49