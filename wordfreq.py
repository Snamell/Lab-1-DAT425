def tokenize(lines):
    words=[]
    for line in lines:
        start = 0
        while start < len(line):
            print(line[start].lower(), end="")
            start = start+1
    return words

def countWords(a,b):
    pass
    
def printTopMost(x,y):
    pass
    
fil=open("articles/article1.txt")
tokenize(fil)
fil.close()
