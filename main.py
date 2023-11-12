import re # may use in future to find most common words
import json

file = "lettersRanked.json"
with open(file) as xyz:
    letterRanking = json.load(xyz)


sampleText = input("Please copy and paste sample text in the cipher: ")

letterCount = {}

for letter in sampleText.lower():
    try:
        letterCount[letter]
    except:
        letterCount[letter] = 0

for letter in sampleText:
    letterCount[letter] = letterCount[letter] + 1


print("Number of recurrences: ")
print(letterCount)

# find number of recurrences of each unknown glyph, then map to english by most recurrent
# english characters

mostCommon = None
letterMap = {}


for rankedLetter in letterRanking:
    if letterCount:
        for letter in letterCount: # find most common remaining unknown letter
            try:
                if letterCount[letter] >= letterCount[mostCommon]: # finds most common letter left
                    mostCommon = letter
            except:
                mostCommon = letter
                print(f"Letter hit is {letter}")
        letterMap[rankedLetter] = mostCommon
        del letterCount[mostCommon]
        print(letterCount)
        mostCommon = None
    else:
        break



print("Here is the resulting mapping: \n----------")
print(letterMap)
print("----------")
    












    




