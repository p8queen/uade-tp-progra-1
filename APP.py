tupla = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
matriz = [] # como en gastos.csv
diccionario = {} # como en modelo-diccionario.json

def cargarDatos(archivo):
    with open(archivo) as data:
        primeraLinea = True
        for line in data:
            gastos = line.strip('\n').split(',')
            if not primeraLinea:
                gastos[1] = round(float(gastos[1]), 2) # redondea el importe
            else:
                primeraLinea = False
            gastos[2] = gastos[2].strip() # elimina espacios en blanco
            matriz.append(gastos)
        matriz.pop(0) # elimina cabecera


def generarMenu():
    # desarrolla joaquin
    print("1. ...")
    print("2. ...")

def crearDiccionario():
    diccionario = {}
    # desarrolla pablo 
    # leer gastos.csv y crear como en modelo-diccionario.json
    return diccionario

def mostrarGastos(mes):
    # desarrolla gustavo
    pass

def gastosPorMes(mes):
    # desarrolla gustavo
    pass

def gastosPorCategoria(mes):
    # desarrolla gustavo
    pass

def gastosPorCategoria(categoria):
    # desarrolla gustavo
    # return lista de gastos
    pass

def gastosPorMesCategoria(mes, categoria):
    # desarrolla gustavo
    # return lista de gastos
    pass

def totalMes(mes):
    # desarrolla gustavo
    # return total de gastos
    pass

def totalMesCategoria(mes, categoria):
    # desarrolla gustavo
    # return total de gastos mes y categoria
    pass

def listaDeCategorias():
    # desarrolla gustavo
    categorias = [x[2] for x in matriz]
    return list(set(categorias)) # elimina duplicados
    
# CRUD Gastos
# crear, recuperar, actualizar, borrar


#MAIN

cargarDatos('gastos.csv')
for linea in matriz:
    print(linea)

