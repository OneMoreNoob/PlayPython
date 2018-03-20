import re
import sys

def main(filename, resultname):
    with open(filename , 'r') as origin:
    #phrase = re.compile((?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\:|\!)\s))
        #jumpreg = re.compile
        textrg = "$ " + origin.read() + " $"
        texto = textrg.lower()
        textdollar = re.sub(r'\n', " ", re.sub(r'\n\n', " $ ", re.sub(r'[;.?!]', " $ ", texto)))
        finaltext = re.sub("[^\w$]"," ", textdollar).split()
        hashtable = {}
#        for i in range(len(finaltext)-1):
#            hashtable[finaltext[i]] = hashtable.get(finaltext[i], [0, {finaltext[i+1]:0}])
#            hashtable[finaltext[i]][0] += 1
#            aux = hashtable[finaltext[i]][1]
#            aux[finaltext[i+1]] = aux.get(finaltext[i+1], 0) + 1
#            hashtable[finaltext[i]][1] = aux
            
            
        for i in range(len(finaltext)-1):
            hashtable[finaltext[i]] = hashtable.get(finaltext[i], [0, [(0,finaltext[i+1])]])
            hashtable[finaltext[i]][0] += 1
            aux = hashtable[finaltext[i]][1]
            te = True
            listatemp = []
            for elemento in aux:
                if(elemento[1] == finaltext[i+1]):
                    listatemp.append(tuple((elemento[0]+1, elemento[1])))
                    te = False
                else:
                    listatemp.append(elemento)
            if(te):
                listatemp.append(tuple((1,finaltext[i+1])))
            hashtable[finaltext[i]][1] = sorted(listatemp, key=lambda x: x[0], reverse = True)
            
        
        for key in sorted(hashtable.keys()):
            print(hashtable[key])
                
    
    

def syntax():
    print ("\n%s filename.txt resultfile.txt\n" % sys.argv[0])
    sys.exit()
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        syntax()
    main(filename=sys.argv[1], resultname=sys.argv[2])
