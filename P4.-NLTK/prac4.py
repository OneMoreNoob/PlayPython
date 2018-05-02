import nltk
from nltk.probability import *

def remove_stopwords(text, language = 'english'):
    stopwords = nltk.corpus.stopwords.words(language)
    result = [w for w in text if w.lower() not in stopwords]
    return result

def formattedprint(listaimp):
    stringl = " ".join(map(str,listaimp))
    print(stringl)

def printfreq(listaimp):
    freqtoprint = FreqDist(listaimp)
    print(freqtoprint.most_common(20))
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
#vocxfrec = sorted([key for key in sorted([(value, key) for key,value in fdist.most_common()])])
vocxfrec = [key for (key,value) in fdist.most_common()]
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
for doc in sorted(wordslist.fileids()):
    print(doc,len(wordslist.words(doc)),len(set(wordslist.words(doc))), len(wordslist.sents(doc)))
    
#12 ¿Coinciden estos resultados con los de la práctica de "Cuenta palabras"? Justifica la respuesta.
# No coinciden, en esta practica son mayores. Seguramente por la limpieza del texto que hacemos en la otra practica
# con la funcion clean_text que se hacia antes de trabajar con el texto.

#Ejercicio 2

#1 Escribe un programa en Python para calcular cuántas veces aparecen las palabras what, when, where, who y why en cada una de las categorías del corpus Brown como un diccionario donde para cada palabra tengamos la lista de categorías y la frecuencia de aparición
from nltk.corpus import brown
lista = {'what':[], 'when':[], 'where':[], 'who':[], 'why':[]}
for cat in brown.categories():
    palabras = brown.words(categories = cat)
    for word in lista.keys():
        lista[word].extend([cat, palabras.count(word)])
print(lista)

#Ejercicio 3

#1 Carga el documento "quijote.txt" en una única cadena
quijoteraw = open('quijote.txt').read()

#2 Mostrar todos los símbolos del documento filtrado ordenados por orden alfabético
from nltk.tokenize.simple import CharTokenizer
tokenizer = CharTokenizer()
tokensraw = set(tokenizer.tokenize(quijoteraw))
tokensraw.remove('\n')
tokensraw.remove(' ')
formattedprint(sorted(tokensraw))

#3 Eliminar del texto los símbolos siguientes
failedtokens = set(['¡','!', '"', "'", '(', ')', ',','-','.',':',';','¿','?',']','«','»'])
tokensfiltered = tokensraw - failedtokens

#4 Mostrar todos los símbolos del documento filtrado ordenados por orden alfabético
formattedprint(sorted(tokensfiltered))

#5 Obtener el número de palabras y el número de palabras distintas del texto filtrado. Mostrar las 10 primeras y las 10 últimas en orden alfabético 
from nltk.tokenize import word_tokenize
predata = quijoteraw
for simbolo in failedtokens:
    predata = predata.replace(simbolo, "")
postdata = word_tokenize(predata)
postdataf = set(postdata)
print(len(postdata), len(postdataf))
formattedprint(sorted(postdataf)[:10])
formattedprint(sorted(postdataf)[-10:])

#6 Obtener las frecuencias de aparición de los ítems que componen el documento filtrado. Un ítem es un par (key, value) donde key es la palabra y value es la frecuencia de aparición de la palabra.Visualizar los primeros 20 ítems.

printfreq(postdata)

#7 Crear un nuevo documento eliminando las stopwords del texto filtrado.
nonstopwords = remove_stopwords(postdata, 'spanish')
with open("quijotefiltered.txt", "w") as wr:
    wr.write(" ".join(map(str,nonstopwords)))

#8 Obtener el número de palabras y el número de palabras distintas del texto sin stopwords. Mostrar la 10 primeras y las 10 últimas en orden alfabético
print(len(nonstopwords), len(set(nonstopwords)))
formattedprint(sorted(set(nonstopwords))[:10])
formattedprint(sorted(set(nonstopwords))[-10:])

#9 Obtener las frecuencias de aparición de los ítems que componen el documento sin stopwords. Visualizar los primeros 20 ítems.
printfreq(nonstopwords)

#10 Crear un nuevo documento sustituyendo cada palabra del texto sin stopwords por su raíz. Para ello se utilizará el stemmer snowball.
from nltk.stem import SnowballStemmer as snow
stem = snow('spanish')
stemmedtext = []
for stemo in nonstopwords:
    stemmedtext.append(stem.stem(stemo))
with open("quijotestemmed.txt", "w") as wr:
    wr.write(" ".join(map(str,stemmedtext)))

#11 Obtener el número de palabras y el número de palabras distintas del nuevo documento. Mostrar la 10 primeras y las 10 últimas en orden alfabético
print(len(stemmedtext), len(set(stemmedtext)))
formattedprint(sorted(set(stemmedtext))[:10])
formattedprint(sorted(set(stemmedtext))[-10:])

#12 Obtener las frecuencias de aparición de los ítems que componen el nuevo documento. Visualizar los primeros 20 ítems.
printfreq(stemmedtext)

#13. Justifica los resultados obtenidos en los pasos 5, 8 y 11
    # 5. Es el que mas palabras tiene porque no eliminamos los stopwords ni utilizamos otras tecnicas como lematizacion. Solo eliminamos ciertos simbolos.
    # 8. Aqui el numero de palabras disminuye porque esta vez si eliminamos los stopwords. 
    # En estos dos pasos, 5 y 8, observamos que las 10 primeras palabras empiezan en mayusculas y las 10 últimas con tilde ya que en nuestro vocabulario
    # existen palabras con mayusculas y tildes, y las mayusculas van primero en orden alfabético y las tildes las ultimas.
    
    # 11. En este caso es el que menos tiene porque quitamos las stopwords y hacemos lematizacion (stemming) con el stemmer snowball que hace que
    # disminuya el numero de palabras porque eliminamos palabras que difieren solo en sus derivaciones. Tambien cambian las primeras y ultimas 
    # palabras porque ya no trabajamos con las palabras originales sino con su version lematizada que hace desaparecer las letras con tildes 
    # y las mayusculas siendo los nuevos mas apropiados exepto por la ultima palabra que al comenzar con ñ en el orden ascii va despues de la z.
    
