def creardiccionarioGastos(tuplaMeses, matrizGastos, diccionarioGastos):
   def crearDiccionario():
    diccionarioGastos = {}
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
