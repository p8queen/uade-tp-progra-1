opcion=0

print("""
    Menú de opciones:
    1. Cargar nuevo gasto
    2. Ver gastos por mes
    3. Ver gastos por mes y categoría
    4. Ver gastos por categoría
    5. Ver lista de categorías
    6. Editar lista de categorías
    7. Editar gasto
    8. Eliminar gasto
    9. Salir""")

opcion=int(input('Ingrese la opción deseada: '))

while opcion!=9:
    if opcion==1:
        cargarNuevoGasto()
    elif opcion==2: 
        gastosPorMes()
    elif opcion==3:
        gastosPorMesCategoria()
    elif opcion==4:
        gastosPorCategoria()
    elif opcion==5:
        listaDeCategorias()
    elif opcion==6:
        editarListaDeCategorias()
    elif opcion==7:
        editarGasto()
    elif opcion==8:
        eliminarGasto()
    elif opcion==9:
        print(f'¡Gracias por elejirnos!\n')
    else:
        print('El valor ingresado no es un menú válido. Por favor ingrese nuevamente.')
