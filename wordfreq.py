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
                except IndexError:
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