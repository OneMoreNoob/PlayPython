import re
import sys
import pickle
import random

def main(filename):
    diccionario = load_object(filename)
    count = 0
    while count < 10:
        frase = ""
        lastelement = "$"
        for i in range(1,25):
            elegirpalabra = []
            lista = diccionario[lastelement][1]
            randomvalue = random.randint(0, diccionario[lastelement][0] - 1)
            for element in lista:
                elegirpalabra+= [element[1]] * element[0]
            
            lastelement = elegirpalabra[randomvalue]
            if lastelement == "$":
                break
            frase += lastelement + " "
        if frase.strip():
            count+=1
        print(frase)
        
        
    
def load_object(file_name):
    with open(file_name, 'rb')as fh:
        obj = pickle.load(fh)
    return obj

def syntax():
    print ("\n%s filename\n" % sys.argv[0])
    sys.exit()
    
if __name__ == '__main__':
    if len(sys.argv) < 1:
        syntax()
    main(filename=sys.argv[1])