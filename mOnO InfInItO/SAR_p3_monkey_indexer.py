import re

def main(filename, resultname):
   with open(filename , 'r') as origin:
    phrase = re.compile((?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\:|\!)\s)
    

def syntax():
    print ("\n%s filename.txt resultfile.txt\n" % sys.argv[0])
    sys.exit()
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        syntax()
    main(filename=sys.argv[1], resultname=sys.argv[2])
