import os

nombre_carpeta = "archivostxt"

lista_archivos = os.listdir(nombre_carpeta)

for nombre_archivo in lista_archivos:
    if os.path.isfile(nombre_carpeta+"/"+nombre_archivo):
        print(nombre_archivo)
        archivo = open(nombre_carpeta+"/"+nombre_archivo,'r')
        lista_lineas = archivo.readlines()
        archivo.close()
        longitud = len(lista_lineas)
        print(f"El archivo: {nombre_archivo}, tiene {longitud} lineas")

        archivo = open(nombre_carpeta+"/"+nombre_archivo,'r')
        texto = archivo.read()
        archivo.close()
    
        simbolos = ["(",")",",",".",";",":","\""]

        for simbolo in simbolos:
            texto = texto.replace(simbolo, "")

        lista_palabras = texto.split()
        lista_palabras.sort()

        for palabra in lista_palabras:
            print(palabra)