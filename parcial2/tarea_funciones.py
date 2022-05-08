import nltk
import random
from datetime import datetime

carpeta_nombre = "archivostxt"
archivo_nombre = "computo.txt"

with open(carpeta_nombre+"/"+archivo_nombre,'r', encoding="utf-8") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto,"spanish")
texto_nltk = nltk.Text(tokens)
palabra = input("ingrese una palabra: ")

# funcion 1 -> index(word)
print("----------Funcion 1----------")
if palabra in texto_nltk:
    posicion_palabra = texto_nltk.index(palabra)
    print(f"La primera aparición de la palabra \"{palabra}\" es en el posición {posicion_palabra}")
else:
    print(f"La palabra \"{palabra}\" no se encuentra en el documento")

# funcion 2 -> freq(sample)
print("\n----------Funcion 2----------")
fdist = nltk.probability.FreqDist(tokens)
frecuencia = fdist.freq(palabra)
print(f"La palabra \"{palabra}\" tiene una frecuencia de {frecuencia:.3f}")

# funcion 3 -> generate(length=100, text_seed=None, random_seed=42)
print("\n----------Funcion 3----------")
random.seed(datetime.now())
semilla = random.randint(0,1000)
texto_nltk.generate(length=50, random_seed=semilla)