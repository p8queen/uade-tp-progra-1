
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