import nltk

carpeta_nombre = "archivostxt"
archivo_nombre = "computo.txt"

with open(carpeta_nombre+"/"+archivo_nombre,'r', encoding="utf-8") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto,"spanish")

tokens_conjunto = set(tokens)
palabras_totales = len(tokens)
palabras_diferentes = len(tokens_conjunto)

texto_nltk = nltk.Text(tokens)
distribucion = nltk.FreqDist(texto_nltk)
hapaxes = distribucion.hapaxes()

for hapax in hapaxes:
    print(hapax)

print(f"Palabras totales: {palabras_totales}")
print(f"Palabras diferentes: {palabras_diferentes}")

distribucion.plot(cumulative=True)
distribucion.plot(40,cumulative=True)

