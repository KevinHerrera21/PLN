from pydoc import doc


archivo = "archivostxt/computo.txt"

palabra = input("Ingresar la palabra a buscar: ")

with open(archivo,'r') as documento:
    texto = documento.read()
    documento.close()

if palabra in texto:
    print(f"La palabra: \"{palabra}\", fue encontrada en el texto")
else:
    print(f"La palabra \"{palabra}\" no existe en el documento")