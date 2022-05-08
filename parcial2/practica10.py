'''Herrera Escareño Kevin Alejandro 6°B'''
import nltk

print("Herrera Escareño Kevin Alejandro 6°B")

carpeta_nombre = "archivostxt"
archivo_nombre = "computo.txt"

with open(carpeta_nombre+"/"+archivo_nombre,"r") as archivo:
    texto = archivo.read()
    archivo.close()

print("-----------------------------------------------------")
palabras_funcionales = nltk.corpus.stopwords.words("spanish")

for palabra in palabras_funcionales:
    print(palabra)

print("-----------------------------------------------------")
tokens = nltk.word_tokenize(texto,"spanish")
tokens_limpios = []

for token in tokens:
    if token not in palabras_funcionales:
        tokens_limpios.append(token)        

print(tokens_limpios)
print("Total de tokens: ",len(tokens))
print("Total de tokens limpios: ",len(tokens_limpios))

texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)
distribucion_limpia.plot(40)