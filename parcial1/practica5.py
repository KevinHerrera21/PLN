ruta_arhivo = "archivostxt"
nombre_archivo = "computo.txt"
simbolos = ["(",")",",",".",";",":","\""]
palabras_unicas = []

with open(ruta_arhivo+"/"+nombre_archivo) as archivo:
    texto = archivo.read()
    archivo.close()

for s in simbolos:
    texto = texto.replace(s,""+s+"")

lista_palabras = texto.split()

for palabra in lista_palabras:
    if palabra in palabras_unicas:
        continue
    palabras_unicas.append(palabra)

print(palabras_unicas)
num_punicas = len(palabras_unicas)
print("El número de palabras unicas es: ",num_punicas)
num_palabras = len(lista_palabras)
print("Número de palabras en todo el documento: ",num_palabras)