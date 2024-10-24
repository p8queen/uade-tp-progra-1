import menudicc as md

# MAIN
menu = md.cargarMenuJson()
opcion = 0
md.menuDicc(menu)
print('   -----------------------   ')

while opcion!=9:
    opcion= int(input('Ingrese la opción deseada: '))
    if opcion < 10:
        md.subMenuDicc(menu, opcion)
    else:
        md.runFuncion(menu, opcion)
    print()

