import datetime


# cargar fecha en formato yyyy/mm/dd-hh:mm:ss
def cargarFecha():
    return datetime.datetime.now()

print(cargarFecha())