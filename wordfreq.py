def tokenize(lines):
    words = []

    for line in lines:
        start = 0

        while start < len(line):

            if line[start].isspace(): 
                start=start+1

            elif line[start].isalpha():
                end=start 
                try:
                    while line[end].isalpha():
                        end=end+1
                    words.append(line[start:end].lower())
                    start=end
                except IndexError:
                    words.append(line[start:end].lower())
                    break

            elif line[start].isdigit():
                end=start
                try:
                    while line[end].isdigit():
                        end=end+1
                    words.append(line[start:end])
                    start=end
                except IndexError:
                    words.append(line[start:end].lower())
                    break
                

            else:
                words.append(line[start])
                start=start+1
 
    return words


def countWords(words, stopWords):
    frequencies={}

    for word in words:
        if word not in stopWords and word not in frequencies:
            frequencies[word]=1
            
        elif word not in stopWords and word in frequencies:
            frequencies[word]+=1
        
    return frequencies


def printTopMost(frequencies,n): 
    myDict = 0
    
    for word, freq in sorted(frequencies.items(), key=lambda x: -x[1]): 
        if myDict == n:
            break   
        
        print(str(word).ljust(20)+str(freq).rjust(5))
        myDict = myDict +1