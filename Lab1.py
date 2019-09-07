import time

def readFile(wordSet, prefixList):    #This reads the file containing all the words to reference against
    f = open("words_alpha.txt","r")
    for line in f:
        wordSet.add(line[:-1])
        for i in range(len(line)-1):
            prefixList.add(line[:i])
    f.close()


def findAnagrams(notUsed, used, anagram, prefixList):    # This finds all possible anagrams  
    if len(notUsed) == 0:
        anagram.add(used)
    else:
        for i in range(len(notUsed)):
            usedLetters = notUsed[i]
            notUsedLetters = notUsed[:i] + notUsed[i+1:]
            findAnagrams(notUsedLetters, used + usedLetters, anagram, prefixList)


def findAnagramsPart2(notUsed, used, anagram, prefixList):    # Same as findAnagrams but witch a check for duplicates
    if len(notUsed) == 0:
        anagram.add(used)
    else:
        for i in range(len(notUsed)):
            if notUsed[i] not in notUsed[i+1:]:              
                usedLetters = notUsed[i] 
                notUsedLetters = notUsed[:i] + notUsed[i+1:]
                findAnagramsPart2(notUsedLetters, used + usedLetters, anagram, prefixList)

def findAnagramsPart3(notUsed, used, anagram, prefixList):    # This finds all possible anagrams  
    if len(notUsed) == 0:
        anagram.add(used)
    elif used not in prefixList:
        return
    else:
        for i in range(len(notUsed)):
            usedLetters = notUsed[i]
            notUsedLetters = notUsed[:i] + notUsed[i+1:]
            findAnagramsPart3(notUsedLetters, used + usedLetters, anagram, prefixList)
  

########################    MAIN START    ############################################  

newRun = True
wordSet = set()
prefixList = set()
readFile(wordSet, prefixList)
while(newRun):  
    anagram = set()
    print("Enter a word or empty string to finish: ")
    userWord = input()
    startTime = time.time()
    if userWord == "" :
        break 
    findAnagramsPart3(userWord, '', anagram, prefixList) # calls methods,,, change part number to change callmethods
    common = wordSet.intersection(anagram)
    endTime = time.time()
    ogWordBypass = []          # lines 60-65 remove any duplicate words
    for i in common:           # and sorts the set alpebetically
        if i == userWord:
            continue
        ogWordBypass.append(i)
    ogWordBypass.sort()
    print("The word", userWord, " has the following", len(ogWordBypass), " anagrams: ")
    for i in ogWordBypass:
        print(i)
    print("It took ", endTime - startTime, "seconds to find the anagrams")
print("Bye, thanks for useing this program")    