# Q: Given a sequence of words, print all anagrams together

# input: plea, dog, pale, evil, peal, live, veil, leap, god, vile

# output: dog, god, evil, live, veil, vile, leap, pale, peal, plea

def groupAnagrams(words):        
    d = {}
    
    for word in words:
        sortedWord =  sorted(word)     # in alphabetical order
        print(sortedWord)

        if sortedWord not in dict:
            d[sortedWord] = [word]
        else:
            d[sortedWord].append(word)
            
    anagrams = []
    for key, value in d:
        anagrams.append(value)
        
    print(anagrams)

groupAnagrams(["plea"])