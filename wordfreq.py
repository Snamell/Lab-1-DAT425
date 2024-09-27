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
                    print(line[start:end])
                    words.append(line[start:end].lower())
                    start=end
                except IndexError: #Without IndexError, if a string ends with a letter there will be an error. 
                    print(line[start:end])
                    words.append(line[start:end].lower())
                    return words

            elif line[start].isdigit():
                end=start
                while line[end].isdigit():
                    end=end+1
                print(line[start:end])
                words.append(line[start:end])
                start=end

            else:
                print(line[start])
                words.append(line[start])
                start=start+1

    return words

def countWords(words, stopWords):
    these_words={}

    for word in words:
        if word not in stopWords and word not in these_words:
            these_words[word]=1
        elif word not in stopWords and word in these_words:
            these_words[word]+=1
        
    return these_words


print(countWords(["hej","hej","hej", "hallå","a"],["a"]))


def printTopMost(frequencies,n):
    
    top_most_words = []
    
    for word, freq in frequencies.items():
        print(word, freq)
        
    
    print(printTopMost(frequencies, n))
 
  
    # ta in frequencies (countWords dictionary) och printa de n-flesta ord ({sak: 10, vet: 4, fisk: 14, cool: 2}(frequencies), 3(n)): ger fisk 14, sak 10 , vet 4.
     
    # ljust = 20 och rjust 5 (lägger till mellanrum mellan ord, frequencies, och antal upprepningar, n.)