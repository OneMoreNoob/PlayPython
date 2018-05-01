import nltk
from nltk.probability import *

#Ejercicio 1

#1 Acceder al corpus en castellano cess_esp
from nltk.corpus import cess_esp as corpus

#2 Mostrar el número de palabras que contiene este corpus
print(len(corpus.words()))

#3 Mostrar el número de frases que contiene
print(len(corpus.sents()))

#4 Obtener las frecuencias de aparición de los ítems que componen el primer fichero del corpus
#anterior. Un ítem es un par (key, value) donde key es la palabra y value es la frecuencia de
#aparición de la palabra. Visualizar los 20 más frecuentes.
text1 = corpus.words(corpus.fileids()[0])
fdist = FreqDist(text1)
print(fdist.most_common(20))

#5 Obtener el vocabulario del primer fichero del corpus (ordenado por frecuencia)
#vocxfrec= sorted([(b,a) for a,b in sorted([(y,x) for x,y in fdist.keys()])])
vocxfrec = sorted([key for key in sorted([(value, key) for key,value in fdist.most_common()])])
print(vocxfrec)

#6 Obtener de forma ordenada las palabras del vocabulario de longitud mayor que 7 y que aparezcan más de 2 veces en el primer fichero del corpus.
print([key for key,value in fdist.most_common() if (len(key) > 7) and (value > 2)])

#7 Obtener la frecuencia de aparición de las palabras en el primer fichero del corpus. Además, y para el mismo fichero obtener la frecuencia de la palabra 'a'.
print(sorted(fdist.values(), reverse = True))
print("Freq aparición de la preposición a:", fdist['a'])

#8 Obtener el número de palabras que sólo aparecen una vez en el primer fichero del corpus.
print("Número de palabras que aparecen una sóla vez:" ,len(fdist.hapaxes()))

#9 Obtener la palabra más frecuente del primer fichero del corpus.
print("La palabra más frecuente es:", fdist.max())

#10 Cargar los ficheros de PoliformaT ("spam.txt","quijote.txt" y "tirantloblanc.txt") como un corpus propio.
from nltk.corpus import PlaintextCorpusReader
corpus_root=r"./"
wordslist = PlaintextCorpusReader(corpus_root, ['spam.txt','quijote.txt', 'tirantloblanc.txt'])
4
#11 Calcular el número de palabras, el número de palabras distintas y el número de frases de los tres documentos
for doc in wordslist.fileids():
    print(doc,len(wordslist.words(doc)),len(set(wordslist.words(doc))), len(wordslist.sents(doc)))
    
#12 ¿Coinciden estos resultados con los de la práctica de "Cuenta palabras"? Justifica la respuesta.

#Ejercicio 2

#1 Escribe un programa en Python para calcular cuántas veces aparecen las palabras what, when, where, who y why en cada una de las categorías del corpus Brown como un diccionario donde para cada palabra tengamos la lista de categorías y la frecuencia de aparición
from nltk.corpus import brown
words = ['what','when','where','who','why']
lista = {'what':[], 'when':[], 'where':[], 'who':[], 'why':[]}
for cat in brown.categories():
    palabras = brown.words(categories = cat)
    for word in words:
        lista[word].extend([cat, palabras.count(word)])
print(lista)

#Ejercicio 33

#1 Carga el documento "quijote.txt" en una única cadena
quijote = wordslist.words('quijote.txt')
