def fileWordCount():
    fileName = input("Enter the file name : ")
    numberOfWords = 0
    
    file = open(fileName , "r")
    for line in file :
        words = line.split()
        numberOfWords = numberOfWords + len(words)
        print("number of Words : ")
        print(numberOfWords)


fileWordCount()