import json 

def cargarCategorias(archivo):
    try:
        f = open(archivo, 'r', encoding='utf-8')
        descripcionCategorias = json.load(f)
        f.close()
        return descripcionCategorias
    except FileNotFoundError:
        print('No se encontró el archivo de categorías.')
        return {}
    
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

def listaDeCategorias(descripcionCategorias):
    print('\nCategorias: \n')
    i=0
    for categoria in descripcionCategorias:
        i+=1
        print(f'{i} - {categoria} : {descripcionCategorias[categoria]}')
    
def cargarNuevoGasto(categorias, matrizGastos,descripcionCategorias, tuplaMeses, diccionarioGastos):
    print('\nPara cargar un gasto debe completar Fecha (YYYY-MM-DD), Monto del gasto y Categoría.\nLas categorías posibles son:\n')
    listaDeCategorias(descripcionCategorias)
    id=matrizGastos[-1][0]+1
    fechaGasto=input('Fecha en formato YYYY-MM-DD: ')
    # fecha a tupla
    fechaGasto = fechaGasto.split('-')
    fechaGasto = tuple(map(int, fechaGasto))
    importeGasto=float(input('Importe del gasto: '))
    categoriaGasto=int(input('De la lista de categorias indique el número de la misma para seleccionarla: '))
    gastoNuevo=[id,fechaGasto,importeGasto,categorias[categoriaGasto-1], True]
    matrizGastos.append(gastoNuevo)
    crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)

# Menu opciones de consulta de gastos 20 al 29
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
    for gasto in matrizGastos:
        if gasto[0] == id: 
            print(f'ID: {gasto[0]} - Fecha: {gasto[1]} - Importe: ${gasto[2]} - Categoria: {gasto[3]}')  

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

def buscarGastosPorRangoImporte(matrizGasto, minimo, maximo):
    gastos = []
    for gasto in matrizGasto:
        if gasto[2] >= minimo and gasto[2] <= maximo:
            gastos.append(gasto)
    for gasto in gastos:
        print(f'ID: {gasto[0]} - Fecha: {gasto[1]} - Importe: ${gasto[2]} - Categoria: {gasto[3]}') 

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

# FIN - Menu opciones de consulta de gastos 20 al 29

# Menu opciones de consulta de categorías 30 al 39

def guardarCategorias(archivo, descripcionCategorias):
    try:
        f = open(archivo, 'w', encoding='utf-8')
        # escribir en formato json 
        json.dump(descripcionCategorias, f, indent=4)
        f.close()
        print('Categorías actualizadas en el archivo.')
    except FileNotFoundError:
        print('No se encontró el archivo de categorías.')
    

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
    for gasto in matrizGastos:
        if gasto[4]:
            categoriasEnUso.append(gasto[3])
    return set(categoriasEnUso)

# escribir en el archivo de categorias


# FIN - Menu opciones de consulta de categorías 30 al 39

# Menu opciones  gastos 40 al 49
def buscarGastoPorId(matrizGastos, id): 
    for gasto in matrizGastos:
        if gasto[0] == id: 
            print(f'ID: {gasto[0]} - Fecha: {gasto[1]} - Importe: ${gasto[2]} - Categoria: {gasto[3]} - activo: {gasto[4]}')  

def eliminarGastoId(matrizGastos, id, tuplaMeses, diccionarioGastos):
    buscarGastoPorId(matrizGastos, id)
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
    buscarGastoPorId(matrizGastos, id)

def editarGastoId(matrizGastos, id, descripcionCategorias, tuplaMeses, diccionarioGastos):
    print('Gasto a editar:')
    buscarGastoPorId(matrizGastos, id)
    queEdita=int(input('\n ¿Qué desea editar?\n1 - Fecha\n2 - Monto\n3 - Categoría\n4 - Deshacer Gasto Borrado \n0 - Cancelar. Volver al menu\n Ingrese la opcion: '))
    if queEdita==0:
        print('Operación cancelada.')
        return
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
    crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)

# FIN - Menu opciones  gastos 40 al 49