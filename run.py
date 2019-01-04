from modelado.archivo import*
from paquete_archivos.miarchivo import *

m = MiArchivo();
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
lista_obj=[]


for d in lista:
    p=Equipo(d[0],d[1],d[2],d[3])
    lista_obj.append(p)
    print(p)


operacion = Operaciones(lista_obj)

opc = input("Ordenar por nombre(1)\nOrdenar por Camperonatos(2)")

if opc == 1:
    operacion.ordenarnombre()
    if opc==2:
        operacion.ordenarCamperonatos()


