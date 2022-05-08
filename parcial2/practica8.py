import nltk

carpeta_nombre = "archivostxt"
archivo_nombre = "computo.txt"

with open(carpeta_nombre+"/"+archivo_nombre,'r', encoding="utf-8") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto,"spanish")

for token in tokens:
    print(token)

palabras_totales = len(tokens)
print(f"Número de palabras: {palabras_totales}")

tokens_conjunto = set(tokens)
palabras_diferentes = len(tokens_conjunto)

riqueza_lexica = palabras_diferentes/palabras_totales
print("Riqueza lexica: {:.3f}".format(riqueza_lexica))

riqueza_lexica = 100*(palabras_diferentes/palabras_totales)
print("Porcentaje de riqueza lexica: {:.3f}%".format(riqueza_lexica))

palabra = input("Ingrese una palabra: ")

texto_nltk = nltk.Text(tokens)
texto_nltk.concordance(palabra)
texto_nltk.similar(palabra)

conteo_individual = tokens.count(palabra)
print(f"La palabra \"{palabra}\" se ecuentró {conteo_individual} veces en el texto")