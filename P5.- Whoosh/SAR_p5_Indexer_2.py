#!/usr/bin/env python

import os
import re
from whoosh.index import create_in
from whoosh.fields import Schema, ID, TEXT

#from whoosh.analysis import LowercaseFilter, RegexTokenizer
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), globalID=TEXT(stored=True), inDoc=TEXT(stored=True), content=TEXT)
idir = "index_dir"
pathenero = "./enero"
if not os.path.exists(idir):
    os.mkdir(idir)
ix = create_in(idir, schema)

directory = os.fsencode(pathenero)
writer = ix.writer()
for f in os.listdir(directory):
    with open(pathenero + "/" + os.fsdecode(f) , 'r' ) as origin:
        counter = 0
        texto = origin.read()
        noticias = re.compile('<text>(.*?)</text>', re.DOTALL |  re.IGNORECASE).findall(texto)
        titulos = re.compile('<title>(.*?)</title>', re.DOTALL |  re.IGNORECASE).findall(texto)
        notit = zip(titulos, noticias)
        for par in notit:
            counter += 1
            writer.add_document(title = par[0],path=pathenero, globalID= os.fsdecode(f)+ "/" + str(counter),inDoc= str(counter),content= par[1])
writer.commit()        
