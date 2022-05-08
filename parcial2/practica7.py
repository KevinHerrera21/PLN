import re

carpeta_nombre = "archivostxt"
archivo_nombre = "computo.txt"

with open(carpeta_nombre+"/"+archivo_nombre) as archivo:
    texto = archivo.read()
    archivo.close()

expresion_regular1 = re.compile(r"computación")
resultados_busqueda1 = expresion_regular1.finditer(texto)

expresion_regular2 = re.compile(r"nu")
resultados_busqueda2 = expresion_regular2.finditer(texto)

print(f"------------{expresion_regular1}------------")
for resultado in resultados_busqueda1:
    print(resultado.group(0))

print(f"------------{expresion_regular2}------------")
for resultado in resultados_busqueda2:
    print(resultado.group(0))