'''
 Vigenere Cipher Algorithm
--------------------------
-- Abdolrahman Farshgar --
    January 5, 2021
--------------------------
'''

# Uppercase alphabets of English language
UPPERCASE_ALPHABETS = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

# Lowercase alphabets of English language
LOWERCASE_ALPHABETS = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m', 
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

# A set of dictionaries will be defined once 
# in the program to increase the access speed for later usage.
charToNumUpper = {}
numTocharUpper = {}

charToNumLower = {}
numTocharLower = {}


def initializeDictionaries():
    for i in range(26):
        charToNumUpper[UPPERCASE_ALPHABETS[i]] = i
        numTocharUpper[i] = UPPERCASE_ALPHABETS[i]
        charToNumLower[LOWERCASE_ALPHABETS[i]] = i
        numTocharLower[i] = LOWERCASE_ALPHABETS[i]


def encryption(key, message):
    cipher = ''

    # changing the key to be all lowercase. Otherwise we would run into problems later.
    lowerKey = []
    for k in range(len(key)):
        lowerKey.append(key[k].lower())

    # to keep track of the current key to be used as the alphabet shift
    index = 0

    for m in message: 
        if m in UPPERCASE_ALPHABETS:
            n = charToNumUpper[m]
            k = charToNumLower[lowerKey[index]]
            index = (index + 1) % len(key)
            n = (n+k) % 26
            t = numTocharUpper[n]
            cipher += t
        elif m in LOWERCASE_ALPHABETS:
            n = charToNumLower[m]
            k = charToNumLower[lowerKey[index]]
            index = (index + 1) % len(key)
            n = (n+k) % 26
            t = numTocharLower[n]
            cipher += t
        else:
            cipher += m
    
    return cipher


def decryption(key, cipher):
    message = ''

    # changing the key to be all lowercase. Otherwise we would run into problems later.
    lowerKey = []
    for k in range(len(key)):
        lowerKey.append(key[k].lower())

    # to keep track of the current key to be used as the alphabet shift
    index = 0

    for c in cipher: 
        if c in UPPERCASE_ALPHABETS:
            n = charToNumUpper[c]
            k = charToNumLower[lowerKey[index]]
            index = (index + 1) % len(key)
            n = (n-k) % 26
            t = numTocharUpper[n]
            message += t
        elif c in LOWERCASE_ALPHABETS:
            n = charToNumLower[c]
            k = charToNumLower[lowerKey[index]]
            index = (index + 1) % len(key)
            n = (n-k) % 26
            t = numTocharLower[n]
            message += t
        else:
            message += c
    
    return message