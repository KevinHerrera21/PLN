# Leer documento de texto
archivoComputo = open("archivostxt/computo.txt",'r')
print(archivoComputo.read())
archivoComputo.close()

# Escribir en documento de texto
cadena = "Hola mundo"
archivoPrueba = open("archivostxt/prueba.txt",'w')
archivoPrueba.write(cadena)
archivoPrueba.close()

## Leer la el documento con la nueva linea
archivoPrueba = open("archivostxt/prueba.txt",'r')
print(archivoPrueba.read())
archivoPrueba.close()