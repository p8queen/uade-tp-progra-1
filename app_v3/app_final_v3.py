import menudicc as md
import funciones as f

# MAIN
f.crearDiccionarioId(md.tuplaMeses, md.matrizGastos, md.diccionarioGastos)

menu = md.cargarMenuJson()
opcion = 0
md.menuDicc(menu)
print('   -----------------------   ')

while opcion!=9:
    try:
        opcion= int(input('Ingrese la opción deseada:'))
        if opcion > 1 and opcion < 10:
            md.subMenuDicc(menu, opcion)
        else:
            md.runFuncion(menu, opcion)
        print()
    except ValueError as e:
        cadena = f'Ingresada opción inválida no INT. Error: {e}'
        print(cadena)
        f.escribirErrores('error.log', cadena)

