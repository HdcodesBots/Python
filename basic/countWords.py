string = input("Introduce Yourself:")
print(string)
wordCount = 1
characterCount = 0

for character in string :
        characterCount=characterCount+1
print("Number of characters in the string :")
print(characterCount) 

if (character == " ") :
        wordCount = wordCount + 1
print("Number of words in the string :")
print(wordCount+2)      
         