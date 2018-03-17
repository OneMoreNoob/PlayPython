#! -*- encoding: utf8 -*-
# Akshay Punjabi
# Pablo Izquierdo Ayala
from operator import itemgetter
import re
import sys

clean_re = re.compile('\W+')
def clean_text(text):
    return clean_re.sub(' ', text)

def sort_dic(d):
    for key, value in sorted(sorted(d.items()), key=itemgetter(1), reverse=True):
        yield key, value

def text_statistics(filename, to_lower=True, remove_stopwords=True):
    # COMPLETAR
    with open(filename, 'r') as datos:
        lineas = datos.readlines()
        print("Lines:" , len(lineas))      
        listmasteraux=clean_text(" ".join(lineas)).split()
        listmaster = []
        if(to_lower):
            for word in listmasteraux:
                listmaster.append(word.lower())
        wordsaux = []
        if(to_lower == False):
            listmaster = listmasteraux
        print("Number words (with stopwords):" , len(listmaster))
        if(remove_stopwords):
            with open("stopwords_en.txt",'r') as stop:
                words = clean_text(" ".join(stop.readlines())).split()
                for palabras in listmaster:
                    if(palabras not in words):
                        wordsaux.append(palabras)
                print("Number words (without stopwords):", len(wordsaux))
                listmaster = wordsaux
        vocabulario = set().union(listmaster,listmaster)
        print("Vocabulary size:" , len(vocabulario))
        print("Number of symbols:" , len("".join(listmaster)))
        diccionario = {}
        letras = {}
        for palabra in listmaster:
            diccionario[palabra] = diccionario.get(palabra, 0) + 1
            for letra in palabra:
                letras[letra] = letras.get(letra, 0) + 1
        sort_dic(diccionario)
        sort_dic(letras)
        print("Number of different symbols:", len(letras))      
        print("Words (alphabetical order):")
        for key in sorted(diccionario.keys()):
            print("\t%s\t%d" % (key,diccionario[key]))
        print("Words (by frequency):")
        for key, value in sort_dic(diccionario):
            print("\t%s\t%d" % (key,value))
        print("Symbols (alphabetical order):")
        for key in sorted(letras.keys()):
            print("\t%s\t%d"%(key,letras[key]))
        print("Symbols (by frequency):")
        for key, value in sort_dic(letras):
            print("\t%s\t%d"%(key,value))

def syntax():
    print ("\n%s filename.txt [to_lower?[remove_stopwords?]\n" % sys.argv[0])
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        syntax()
    name = sys.argv[1]
    lower = False
    stop = False
    if len(sys.argv) > 2:
        lower = (sys.argv[2] in ('1', 'True', 'yes'))
        if len(sys.argv) > 3:
            stop = (sys.argv[3] in ('1', 'True', 'yes'))
    text_statistics(name, to_lower=lower, remove_stopwords=stop)
