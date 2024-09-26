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
        if word not in stopWords:
            if word in these_words:
                these_words[word] += 1
            else:
                these_words[word] = 1
        
    return these_words


print(countWords(["hej","hej","hej", "hallå","a"],["a"]))


def printTopMost(frequencies,n):
    
    top_most_words = []
    top_word_count = []
    
    with open("articles/article1.txt") as files:
        files = {}
        for word,freq in files.items(): 
            top_most_words.append([files])

    return top_most_words


print(printTopMost)