'''
 XOR Hash Algorithm
--------------------------
-- Abdolrahman Farshgar --
    January 7, 2021
--------------------------
'''
import math
import random
import Hash

# Great Common Divisor
def gcd(m, n):
    temp = 0
    
    while n != 0:
        temp = n
        n = m % n
        m = temp
    
    return m


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(3, math.floor(math.sqrt(n))+1, 2):
        if n%i==0:
            return False
    
    return True


# Actual converter
def decimalToBinary(decimal):
    binary = []
    if decimal == 0:
        binary.append(0)
    while(decimal > 0):
        binary.append(decimal%2)
        decimal = decimal // 2
    binary.reverse()
    return binary


def find_large_prime(nBytes):
    n = nBytes+2
    num = random.randint((10**n+10**n//2), 10**(n+1))
    q = num // 6

    # in case we only needed a small prime number
    if nBytes == 0:
        num = random.randint(2, 10**n+1)
        q = num // 6 + 1
        while not is_prime(num):
            num = q * 6
            q += 1

            if is_prime(num+1):
                return num+1
            if is_prime(num-1):
                return num-1
    
    # otherwise if really a large prime is needed
    length = len(decimalToBinary(num))
    while length < nBytes*8:
        num = q * 6
        q += random.randint(10**n//2, 10**n)
        length = len(decimalToBinary(num))

    q = num // 6 + 1
    while not is_prime(num):
        num = q * 6
        q += 1

        if is_prime(num+1):
            return num+1
        if is_prime(num-1):
            return num-1

    return -1


def generate_e(Phi):
    e = random.randint(2, Phi-1)
    # e, Phi should be relatively prime with each other
    while gcd(e, Phi) != 1:
        e = random.randint(2, Phi-1)

    return e


def generate_d(e, Phi):
    for i in range(2, Phi-1):
        if i == e:
            continue

        if e*i%Phi == 1:
            return i
    
    return -1
    

# the length of the RSA keys can be given by number of bytes. 
def generate_key_pairs(i=0):
    p = find_large_prime(i//2)
    while p == -1:
        p = find_large_prime(i//2)

    q = find_large_prime(i//2)
    while q == -1:
        q = find_large_prime(i//2)
    
    n = p * q
    Phi = (p-1) * (q-1)

    e = generate_e(Phi)
    d = generate_d(e, Phi)
    while d == -1:
        e = generate_e(Phi)
        d = generate_d(e, Phi)

    return e,d,n


def encryption(message, e, n):
    cipher = []

    for m in message:
        M = ord(m)    
        C = (M ** e) % n
        cipher.append(C)
    
    return cipher

def decryption(cipher, d, n):
    message = []
    
    for C in cipher:
        M = (C**d) % n
        m = chr(M)
        message.append(m)
        # print(m, end='')
    # print()

    return message

def E_Signature(hashedValue, d, n):
    h = Hash.binaryToDecimal(hashedValue)
    h = str(h)
    # encryption with private key for creating e-signature
    c = encryption(h, d, n)

    return c

def confirm_signature(hashedValue, e, n, e_signature):
    h = Hash.binaryToDecimal(hashedValue)
    h = str(h)
    m = decryption(e_signature, e, n)
    m = ''.join(m)

    if h == m:
        print('E-Signature is confirmed!')
    else:
        print('The E-Signature is not authentic!')
    

