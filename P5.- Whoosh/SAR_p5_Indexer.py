#!/usr/bin/env python

import os
from whoosh.index import create_in
from whoosh.fields import Schema, ID, TEXT
#from whoosh.analysis import LowercaseFilter, RegexTokenizer
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
idir = "index_dir"
pathenero = "./enero"
if not os.path.exists(idir):
    os.mkdir(idir)
ix = create_in(idir, schema)


directory = os.fsencode(pathenero)
writer = ix.writer()
for f in os.listdir(directory):
    with open(pathenero + "/" + os.fsdecode(f) , 'r' ) as origin:
        writer.add_document(title=os.fsdecode(f), path=pathenero,
                    content=origin.read())        
writer.commit()
