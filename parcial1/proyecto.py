# Herrera Escareño Kevin Alejandro 6°B
import os

nombre_carpeta = "documentos"
carpeta_salida = "documentos/union"
archivo_salida = "union.txt"
nombre_documento1 = "computo.txt"
nombre_documento2 = "npl.txt"

numLinea_doc1 = 0
numTexto_doc1 = 0
numVacio_doc1 = 0

numLinea_doc2 = 0
numTexto_doc2 = 0
numVacio_doc2 = 0

simbolos = ["(",")",",",".",";",":","\"", "“", "”", "-"]

union = ""

# Documento 1
with open(nombre_carpeta+"/"+nombre_documento1,'r') as doc:
    lineas_doc1 = doc.readlines()
    doc.close()

with open(nombre_carpeta+"/"+nombre_documento1,'r') as doc:
    texto_doc1 = doc.read()
    union += f"---------------- archivo: {nombre_documento1} ----------------\n"
    union += texto_doc1
    union += "\n\n"
    doc.close()

for linea in lineas_doc1:
    numLinea_doc1+=1
    if linea.strip() == "":
        numVacio_doc1+=1
    else:
        numTexto_doc1+=1

for simbolo in simbolos:
    texto_doc1 = texto_doc1.replace(simbolo,"")

lista_palabras_doc1 = texto_doc1.split()
lista_palabras_doc1.sort()

print(f"----------{nombre_documento1}----------")
print(f"Total de lineas: {len(lineas_doc1)}")
print(f"Número de lineas con texto: {numTexto_doc1}")
print(f"Número de líneas vácias: {numVacio_doc1}")

for palabra in lista_palabras_doc1:
    print(palabra)

print(f"Número de palabras {len(lista_palabras_doc1)}")

# Documento 2
with open(nombre_carpeta+"/"+nombre_documento2,'r') as doc:
    lineas_doc2 = doc.readlines()
    doc.close()

with open(nombre_carpeta+"/"+nombre_documento2,'r') as doc:
    texto_doc2 = doc.read()
    union += f"---------------- archivo: {nombre_documento2} ----------------\n"
    union += texto_doc2
    union += "\n\n"
    doc.close()

for linea in lineas_doc2:
    numLinea_doc2+=1
    if linea.strip() == "":
        numVacio_doc2+=1
    else:
        numTexto_doc2+=1

for simbolo in simbolos:
    texto_doc2 = texto_doc2.replace(simbolo,"")

lista_palabras_doc2 = texto_doc2.split()
lista_palabras_doc2.sort()

print(f"----------{nombre_documento2}----------")
print(f"Total de lineas: {len(lineas_doc2)}")
print(f"Número de lineas con texto: {numTexto_doc2}")
print(f"Número de líneas vácias: {numVacio_doc2}")

for palabra in lista_palabras_doc2:
    print(palabra)

print(f"Número de palabras: {len(lista_palabras_doc2)}")

# union de los dos documentos
with open(carpeta_salida+"/"+archivo_salida,'w') as salida:
    salida.write(union)
    salida.close()

with open(carpeta_salida+"/"+archivo_salida,'r') as doc_union:
    texto_doc_union = doc_union.read()
    doc_union.close()

for simbolo in simbolos:
    texto_doc_union = texto_doc_union.replace(simbolo,"")

lista_palabras_doc_union = texto_doc_union.split()
lista_palabras_doc_union.sort()


print(f"----------{archivo_salida}----------")

for palabra in lista_palabras_doc_union:
    print(palabra)

print(f"Número de palabras {len(lista_palabras_doc_union)}")

palabra = input("ingresar palbra a buscar: ")

if palabra in texto_doc_union:
    print(f"La palabra: \"{palabra}\", fue encontrada en el texto")
else:
    print(f"La palabra \"{palabra}\" no existe en el documento")