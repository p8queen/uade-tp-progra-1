def crearDiccionario():
    diccionario = {}
    # Recorrer la matriz y agrupar los datos en el diccionario
    for fila in matriz:
        fecha_str, importe, categoria = fila
        
        # Extraer el mes (caracteres 5 y 6 de la fecha)
        mes_num = fecha_str[5:7]
        
        # Convertir el número de mes a índice de la tupla
        mes = tupla[int(mes_num) - 1]

        # Si el mes no está en el diccionario, agregarlo
        if mes not in diccionario:
            diccionario[mes] = {}

        # Si la categoría no está en el diccionario de ese mes, agregarla
        if categoria not in diccionario[mes]:
            diccionario[mes][categoria] = []

        # Agregar el importe a la lista de la categoría correspondiente
        diccionario[mes][categoria].append(importe)

    return diccionario

def imprimirOrdenado(diccionario): #Ordena alfabeticamente el contenido interno del diccionario
    for mes, categorias in diccionario.items():
        print(f"{mes.capitalize()}:")
        for categoria, importes in categorias.items():
            print(f"  {categoria}: {importes}")

diccionario = crearDiccionario()
