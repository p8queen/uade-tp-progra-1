from funciones import totalGastosPorMes, totalGastosPorCategoria, mostrarGastosPorMes, obtenerCategoriasEnUso, escribirErrores

def test_totalGastosPorMes():
    diccionarioGastos = {'Enero': {'Alquiler': [1000], 'Comida': [500], 'Ropa': [200]},
                         'Febrero': {'Alquiler': [1000], 'Comida': [500], 'Ropa': [200]},
                         'Marzo': {'Alquiler': [1000], 'Comida': [500], 'Ropa': [200]} }
    resultado = totalGastosPorMes(diccionarioGastos)
    # Assert
    assert resultado == 5100.0



def test_totalGastosPorCategoria():
    matrizGastos = [[12, (2024, 8, 7), 123.0, 'Alimentación', False], 
                    [13, (2024, 1, 1), 1000.8, 'Salud', True],
                    [14, (2024, 12, 9), 700.0, 'Entretenimiento', True],
                    [15, (2024, 11, 11), 300.0, 'Servicios', True],
                    [16, (2024, 10, 24), 9.25, 'Alimentación', True]]
    resultado = totalGastosPorCategoria(matrizGastos)
    # Assert
    assert resultado == 2010.05

def test_mostrarGastosPorMes():
    diccionarioGastos = {'Enero': {'Alquiler': [1000], 'Comida': [300], 'Ropa': [200]},
                         'Febrero': {'Alquiler': [1000], 'Comida': [500], 'Ropa': [500]},
                         'Marzo': {'Alquiler': [1000], 'Comida': [100], 'Ropa': [200]} }
    
    assert mostrarGastosPorMes(diccionarioGastos, 'Enero') == 1500.0
    assert mostrarGastosPorMes(diccionarioGastos, 'Febrero') == 2000.0
    assert mostrarGastosPorMes(diccionarioGastos, 'Marzo') == 1300.0
    
def test_obtenerCategoriasEnUso():
    matrizGastos = [[12, (2024, 8, 7), 123.0, 'Alimentación', False], 
                    [13, (2024, 1, 1), 1000.8, 'Salud', True],
                    [14, (2024, 12, 9), 700.0, 'Entretenimiento', True],
                    [15, (2024, 11, 11), 300.0, 'Servicios', True],
                    [16, (2024, 10, 24), 9.25, 'Alimentación', True]]
    resultado = obtenerCategoriasEnUso(matrizGastos)
    # Assert
    assert resultado == set(['Servicios', 'Entretenimiento', 'Salud', 'Alimentación'])
    
def test_escribirErrores():
    cadena='Test de fun EscribirErrores'
    resultado=escribirErrores('error.log',cadena)
    # Assert
    assert resultado==True
    
