tuplaMeses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

def cargarDatosConId(matrizGastos, archivo):
    with open(archivo) as data:
        primeraLinea = True
        for line in data:
            gastos = line.strip('\n').split(',')
            if not primeraLinea:
                gastos[0] = int(gastos[0]) # convierte el id a entero
                gastos[2] = round(float(gastos[2]), 2) # redondea el importe
            else:
                primeraLinea = False
            gastos[3] = gastos[3].strip() # elimina espacios en blanco
            matrizGastos.append(gastos)
        matrizGastos.pop(0) # elimina cabecera

matrizGastos = []
cargarDatosConId(matrizGastos, 'gastos-id.csv')

#for line in matrizGastos[:10]:
#    print(line)

def crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos):
    for linea in matrizGastos:
        # linea[0] es de la forma YYYY-MM-DD 
        mes = tuplaMeses[int(linea[1].split('-')[1]) - 1]
        categoria = linea[3]
        importe = linea[2]
        if mes not in diccionarioGastos:
            diccionarioGastos[mes] = {}
        if categoria not in diccionarioGastos[mes]:
            diccionarioGastos[mes][categoria] = []
        diccionarioGastos[mes][categoria].append(importe)

diccionarioGastos = {}
crearDiccionarioId(tuplaMeses, matrizGastos, diccionarioGastos)

for mes in diccionarioGastos:
    print(mes)
    for categoria in diccionarioGastos[mes]:
        print(f'\t{categoria}: {diccionarioGastos[mes][categoria]}')

def mostrarGastos(diccionario, mes):
    print(f'Gastos de {mes}:')
    # calcular sub totales por categorias 
    for categoria in diccionario[mes]:
        total = sum(diccionario[mes][categoria])
        print(f'\t{categoria}: {total}')

print('Gastos por mes:')
mostrarGastos(diccionarioGastos, 'enero')

# obtener subtotales por mes 
def totalGastosPorMes(diccionarioGastos, tuplaMeses):
    for mes in tuplaMeses:
        print(f'{mes}: ${totalGastosMes(diccionarioGastos, mes)}')

totalGastosPorMes(diccionarioGastos)
