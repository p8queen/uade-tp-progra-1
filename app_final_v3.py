import menudicc as md
import funciones as f

# MAIN
f.crearDiccionarioId(md.tuplaMeses, md.matrizGastos, md.diccionarioGastos)
menu = md.cargarMenuJson()
opcion = 0
md.menuDicc(menu)
print('   -----------------------   ')

while opcion!=9:
    opcion= int(input('Ingrese la opción deseada: '))
    if opcion > 1 and opcion < 10:
        md.subMenuDicc(menu, opcion)
    else:
        md.runFuncion(menu, opcion)
    print()

