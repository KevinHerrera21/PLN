from operator import index
import os

nombre_carpeta = "archivostxt"
archivo_salida = "union.txt"
carpeta_salida = "archivostxt/union"
union = ""

lista_archivos = os.listdir(nombre_carpeta)

for archivo_nombre in lista_archivos:
    if os.path.isfile(nombre_carpeta+"/"+archivo_nombre):
        archivo = open(nombre_carpeta+"/"+archivo_nombre,'r')
        texto = archivo.read()
        union += f"---------------- archivo: {archivo_nombre} ----------------\n"
        union += texto
        union += "\n\n"
        archivo.close()

with open(carpeta_salida+"/"+archivo_salida,'w') as salida:
    salida.write(union)
    salida.close()