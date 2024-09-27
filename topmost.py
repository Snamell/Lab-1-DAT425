from wordfreq import *
from sys import *
import urllib.request

def main():

    stopWordFileName = argv[1]
    
    linesFileName = argv[2]
    
    n = int(argv[3])

    inp_file=open(stopWordFileName)
    stopWords = inp_file.read().splitlines()
    inp_file.close()

    if linesFileName.startswith("http://") or linesFileName.startswith("https://"):
        response = urllib.request.urlopen(linesFileName)
        lines = response.read().decode("utf8").splitlines()
    
    else:
        inp_file=open(linesFileName)
        lines = inp_file.read().splitlines()
        inp_file.close()

    tokens = tokenize(lines)
    wordcount = countWords(tokens,stopWords)
    printTopMost(wordcount, n)
    

main()