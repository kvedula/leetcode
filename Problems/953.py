# Kamesh Vedula
# Problem: Verifying an Alien Dictionary  


def isAlienSorted(self, words: List[str], order: str) -> bool:
    alphaMap = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    #Regular way to do this
    # for i in range(26):
    #     alphaMap[order[i]] = alphabet[i]
    
    #Smarter way to do this
    for l1, l2 in zip(order, alphabet):
        alphaMap[l1] = l2
    
    converted = []
    for word in words:
        #longer way
        # temp = ""
        # for letter in word:
        #     temp += alphaMap[letter]
        
        #string comprehension
        temp = "".join(alphaMap[letter] for letter in word)
        converted.append(temp)
        
        
    #if this needs to be done without Pythons inbuilt sort function
    for i in range(1, len(converted)):
        if converted[i] < converted[i - 1]:
            return False
    return True