
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

def listaDeCategorias(categorias, descripcionCategorias):
    print('\nCategorias: \n')
    i=0
    for categoria in categorias:
        i+=1
        print(f'{i} - {categoria} : {descripcionCategorias[categoria]}')

def cargarNuevoGasto(categorias, matrizGastos,descripcionCategorias, tuplaMeses, diccionarioGastos):
    print('\nPara cargar un gasto debe completar Fecha (YYYY-MM-DD), Monto del gasto y Categoría.\nLas categorías posibles son:\n')
    listaDeCategorias(categorias,descripcionCategorias)
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

''' 
def consultarGastos(matrizGastos, categorias, tuplaMeses,descripcionCategorias,diccionarioGastos):
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

'''        