def creardiccionarioGastos(tuplaMeses, matrizGastos, diccionarioGastos):
    # Recorrer la matriz y agrupar los datos en el diccionario
    for fila in matrizGastos:
        fecha_str, importe, categoria = fila
        
        # Extraer el mes (caracteres 5 y 6 de la fecha)
        mes_num = fecha_str[5:7]
        
        # Convertir el número de mes a índice de la tupla
        mes = tuplaMeses[int(mes_num) - 1]

        # Si el mes no está en el diccionario, agregarlo
        if mes not in diccionarioGastos:
            diccionarioGastos[mes] = {}

        # Si la categoría no está en el diccionario de ese mes, agregarla
        if categoria not in diccionarioGastos[mes]:
            diccionarioGastos[mes][categoria] = []

        # Agregar el importe a la lista de la categoría correspondiente
        diccionarioGastos[mes][categoria].append(importe)


def imprimirOrdenado(diccionarioGastos): #Ordena alfabeticamente el contenido interno del diccionario
    for mes, categorias in diccionarioGastos.items():
        print(f"{mes.capitalize()}:")
        for categoria, importes in categorias.items():
            print(f"  {categoria}: {importes}")

diccionarioGastos = crearDiccionario()

def buscarGastoPorId(matrizGastos, id):
    # Recorrer la matriz para buscar el gasto con el ID proporcionado
    for gasto in matrizGastos:
        if gasto[0] == id:  # El primer elemento de cada fila es el ID
            return gasto  # Devolver la fila completa si el ID coincide

def listaDeCategorias(matrizGastos, mes):
    categorias = set()  # Usamos un conjunto (set) para eliminar duplicados automáticamente

    # Recorrer la matriz de gastos
    for fila in matrizGastos:
        fecha_str, importe, categoria = fila

        # Extraer el número del mes (caracteres del 5 al 6 de la fecha)
        mes_num = fecha_str[5:7]
        
        # Si el mes coincide con el mes especificado
        if tupla[int(mes_num) - 1] == mes.lower():
            categorias.add(categoria)  # Añadir la categoría al conjunto

    # Convertimos el conjunto a una lista y la devolvemos
    return list(categorias)

def listaDeCategorias(categorias, descripcionCategorias):
    # Recorrer cada categoría de la lista
    for categoria in categorias:
        # Verificar si la categoría tiene una descripción en el diccionario
        if categoria in descripcionCategorias:
            descripcion = descripcionCategorias[categoria]
        else:
            descripcion = "Descripción no disponible"
        
        # Imprimir la categoría y su descripción
        print(f"Categoría: {categoria}")
        print(f"Descripción: {descripcion}")
        print()  # Línea en blanco para separar cada categoría
