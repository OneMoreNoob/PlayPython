#!/usr/bin/env python

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh.query import *

ix = open_dir("index_dir")
with ix.searcher() as searcher:
    valencia = QueryParser("content", ix.schema).parse("valencia")
    resvalencia = searcher.search(valencia)
    print(len(resvalencia))
    notSalenko = QueryParser("content", ix.schema).parse("valencia NOT Salenko")
    resnotSalenko = searcher.search(notSalenko)
    print(len(resnotSalenko))
    futbol = QueryParser("content", ix.schema).parse("futbol")
    resFutbol = searcher.search(futbol)
    print(len(resFutbol))
    aero = QueryParser("content", ix.schema).parse("Los Angeles AND Aeroflot")
    resAero = searcher.search(aero)
    print(len(resAero))