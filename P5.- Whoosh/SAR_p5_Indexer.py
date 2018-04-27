#!/usr/bin/env python

import os
from whoosh.index import create_in
from whoosh.fields import Schema, ID, TEXT

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
idir = "index_dir"
pathenero = "./enero"
if not os.path.exists(idir):
    os.mkdir(idir)
ix = create_in(idir, schema)


directory = os.fsencode(pathenero)
writer = ix.writer()
print(os.listdir(directory))
for f in os.listdir(directory):
    print(os.fsdecode(f))
    with open(pathenero + "/" + os.fsdecode(f) , 'r' ) as origin:
        writer.add_document(title=os.fsdecode(f), path=pathenero,
                    content=origin.read())        
writer.commit()
