archivo = "archivostxt/computo.txt"

numPalabra = 0
numLinea = 0
numTexto = 0
numVacio = 0

palabra = input("Ingresar palabra a buscar: ")

with open(archivo, 'r') as documento:
    lineas = documento.readlines()
    documento.close()

for linea in lineas:
    numLinea+=1
    if linea.strip() == "":
        print(f"Linea No.{numLinea}: esta linea esta vacia\n")
        numVacio+=1
    else:
        print(f"Linea No.{numLinea}: {linea}")
        numTexto+=1
        if palabra in linea:
            numPalabra+=1

print("\nConteos:")
print("Lineas totales:", numLinea)
print("Lineas con texto:",numTexto)
print("Lineas vacias:",numVacio)

if numPalabra>0:
    print(f"La palabra \"{palabra}\" se encuentra: {numPalabra} veces en el documento")
else:
    print(f"La palabra \"{palabra}\" no existe en el documento")