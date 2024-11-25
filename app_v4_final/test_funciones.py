from funciones import totalGastosPorMes, totalGastosPorCategoria, mostrarGastosPorMes

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
                    [16, (2024, 10, 24), 9.20, 'Alimentación', True]]
    resultado = totalGastosPorCategoria(matrizGastos)
    # Assert
    assert resultado == 2010.0

def test_mostrarGastosPorMes():
    diccionarioGastos = {'Enero': {'Alquiler': [1000], 'Comida': [500], 'Ropa': [200]},
                         'Febrero': {'Alquiler': [1000], 'Comida': [500], 'Ropa': [500]},
                         'Marzo': {'Alquiler': [1000], 'Comida': [100], 'Ropa': [200]} }
    
    assert mostrarGastosPorMes(diccionarioGastos, 'Enero') == 1700.0
    assert mostrarGastosPorMes(diccionarioGastos, 'Febrero') == 2000.0
    assert mostrarGastosPorMes(diccionarioGastos, 'Marzo') == 1300.0
    
