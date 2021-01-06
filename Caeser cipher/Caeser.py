'''
 Caeser Cipher Algorithm
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


def encryption(message):
    cipher = ''

    for m in message: 
        if m in UPPERCASE_ALPHABETS:
            n = charToNumUpper[m]
            n = (n+3) % 26
            t = numTocharUpper[n]
            cipher += t
        elif m in LOWERCASE_ALPHABETS:
            n = charToNumLower[m]
            n = (n+3) % 26
            t = numTocharLower[n]
            cipher += t
        else:
            cipher += m
    
    return cipher


def decryption(cipher):
    message = ''

    for c in cipher: 
        if c in UPPERCASE_ALPHABETS:
            n = charToNumUpper[c]
            n = (n-3) % 26
            t = numTocharUpper[n]
            message += t
        elif c in LOWERCASE_ALPHABETS:
            n = charToNumLower[c]
            n = (n-3) % 26
            t = numTocharLower[n]
            message += t
        else:
            message += c
    
    return message