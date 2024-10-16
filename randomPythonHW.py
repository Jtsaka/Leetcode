def palindrome(userInput):
    '''returns true/false -- a word or sentence that reads the same backwards, takes in string input'''
    value = userInput.lower()
    palindromeState = False
    halfLen = len(value) // 2
    counter = 0

    for i in range(0, halfLen):
        if value[i] == value[len(value) - i - 1]:
            counter += 1
    if counter == halfLen:
            palindromeState = True
            #print("This is a Palindrome!")
            return palindromeState

    #print("This is not a Palindrome!")
    return palindromeState


def pangram(userInput): 
    '''returns true/false -- a phrase or sentence containing all 26 letters of the alphabet, takes string input'''
    value = userInput.lower()
    count = 0

    for character in range(26): # go through each letter, access corresponding lowercase letter by using unicode (utilizing ord)
        letter_check = chr(character + ord("a")) 
        if letter_check in value:
            count += 1
    if count == 26:
        #print("This is a Pangram!")
        return True

    #print("This is not a Pangram!") 
    return False

def tautogram(userInput): 
    '''returns true/false -- phrase or sentence in which all words start with the same letter, takes string input'''
    tautogramState = False
    counter = 0
    value = userInput.lower()
    first_letter = value[0]

    if "," in value: # check to see if it's a list of objects
        arr = value.split(", ") 
    else: # check to see if its a sentence
        arr = value.split(" ") 
        for num in arr:
            if num[0] == first_letter:
                counter += 1
        if counter == len(arr):
            tautogramState = True
            #print("This is a tautogram!")
            return tautogramState 
        else:
            #print("This is not a tautogram!")
            return tautogramState


def isogram(userInput): 
    '''returns true/false -- a word in which no letter of the alphabet occurs more than once, takes string input'''
    value = userInput.lower()
    isogramState = True

    for character in value:
        count = value.count(character)
        if count > 1:
            isogramState = False
            #print("This is not an Isogram!")
            return isogramState

    #print("This is an Isogram!") 
    return isogramState

def abecedarian(userInput):
    '''returns true/false -- a word in which the letters appear in alphabetical order, takes string input'''
    abecedarianState = False
    counter = 0
    value = userInput.lower() 

    for increment in range(len(value) - 1):
        if(ord(value[increment]) > ord(value[increment + 1])): # check using unicode
            #print("This is not an abedecerian!")
            return abecedarianState

    abecedarianState = True
    #print("This is an abedecerian!")
    return abecedarianState

def dobloon(userInput): 
    '''returns true/false -- a word in which every letter that appears in the word appears exactly twice, takes string input'''
    dobloonState = False                  
    value = userInput.lower()
    count = 0
    
    for character in value:
        count += value.count(character)
        if count == len(value) * 2:
            dobloonState = True
            #print("This word is a dobloon!")
            return dobloonState

    #print("This word is not a dobloon!")
    return dobloonState
        
