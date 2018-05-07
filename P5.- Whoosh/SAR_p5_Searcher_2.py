#!/usr/bin/env python

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh.query import *

def printer(lista):
    print("Número de elementos encontrados en la consulta: ", len(lista), "\n")
    if(len(lista) <4):
        cuatro(lista)
    else:
        for item in lista:
            formattedPrint(item)
                
def formattedPrint(diccionario):
    for keys  in sorted(diccionario.keys()):
                print(keys, ": " , diccionario[keys].strip())
    print("")

def cuatro(lista):
    for item in lista: 
        with open(item["path"] + "/" + item["globalID"].split("/")[0] , 'r' ) as origin:
            noticias = re.compile('<text>(.*?)</text>', re.DOTALL |  re.IGNORECASE).findall(origin.read())
            formattedPrint(item)
            print("Contenido:\n", noticias[int(item["inDoc"])-1])                
       
        
ix = open_dir("index_dir")
with ix.searcher() as searcher:
    valencia = QueryParser("content", ix.schema).parse("valencia")
    resvalencia = searcher.search(valencia)
    printer(resvalencia)
    notSalenko = QueryParser("content", ix.schema).parse("valencia NOT Salenko")
    resnotSalenko = searcher.search(notSalenko)
    printer(resnotSalenko)
    futbol = QueryParser("content", ix.schema).parse("futbol")
    resFutbol = searcher.search(futbol)
    printer(resFutbol)
    aero = QueryParser("content", ix.schema).parse("Los Angeles AND Aeroflot")
    resAero = searcher.search(aero)
    printer(resAero)