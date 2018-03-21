import re
import sys
import pickle

def main(filename, resultname):
    with open(filename , 'r') as origin:
        textrg = "$ " + origin.read() + " $"
        texto = textrg.lower()
        textdollar = re.sub(r'\n', " ", re.sub(r'\n\n', " $ ", re.sub(r'[;.?!]', " $ ", texto)))
        finaltext = re.sub("[^\w$]"," ", textdollar).split()
        hashtable = {}
#      This subset implementation was made using dictionaries        
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
            hashtable[finaltext[i]][1] = listatemp
            
            #hashtable[finaltext[i]][1] = sorted(listatemp, reverse = True)            
        
        for key in hashtable.keys():
            hashtable[key][1] = sorted(hashtable[key][1], reverse = True)
        save_object(hashtable, resultname)
                
    
    
def save_object(object, file_name):
    with open(file_name, 'wb') as fh:
        pickle.dump(object, fh)

def syntax():
    print ("\n%s filename.txt resultfile\n" % sys.argv[0])
    sys.exit()
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        syntax()
    main(filename=sys.argv[1], resultname=sys.argv[2])
