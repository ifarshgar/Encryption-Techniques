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


def extended_gcd(m,n):
    if m == 0:
        return n, 0, 1
    else:
        g, y, x = extended_gcd(n % m, m)
        return g, x - (n // m) * y, y


def modinv(m, n):
    g, x, y = extended_gcd(m, n)
    if g != 1:
        # modulus inverse does not exist.
        return -1
    else:
        return x % n


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
            break
        if is_prime(num-1):
            break

    return num


def generate_e(start, Phi):
    # e and Phi should be relatively prime with each other
    e = start
    for i in range(start, Phi):
        e += 1
        if gcd(Phi, e) == 1:
            return e        

    return -1


def generate_d(e, Phi):
    i = 1

    d = modinv(e, Phi)
    while d == e:
        d = modinv(e, Phi)
        i += 1
        if i == 10:
            e = generate_e(e, Phi)
            i = 1
    
    return d
    

# This RSA has the length of 32-bits i.e. 4-bytes  
def generate_key_pairs(i=0):
    p = find_large_prime(i//2)
    q = find_large_prime(i//2)

    # Calculating n and Phi according to our chosen prime numbers p and q.
    n = p * q 
    Phi = (p-1) * (q-1)

    e = generate_e(10**(i+1), Phi)

    d = generate_d(e, Phi)

    # print(p,q)
    return e,d,n

# e, d, n = generate_key_pairs(i)

# i: 1-byte , 8-bit
# p: 678
# q: 757
# e: 101
# d: 466205
# n: 513246

# p: 61 
# q: 47
# e: 7
# d: 1183 
# n: 2867

def simple_init():
    e = 7
    d = 1183 
    n = 2867
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
    

