'''
 DES Encryption Algorithm
--------------------------
-- Abdolrahman Farshgar --
    December 31, 2020
--------------------------
'''

# Initial permutation. 64-bit
IP  = [
    58, 50, 42, 34, 26, 18, 10, 2, 
    60, 52, 44, 36, 28, 20, 12, 4, 
    62, 54, 46, 38, 30, 22, 14, 6, 
    64, 56, 48, 40, 32, 24, 16, 8, 
    57, 49, 41, 33, 25, 17, 9, 1, 
    59, 51, 43, 35, 27, 19, 11, 3, 
    61, 53, 45, 37, 29, 21, 13, 5, 
    63, 55, 47, 39, 31, 23, 15, 7
]

# Inverse of the initial permutation. 64-bit
IPInv = [
    40, 8, 48, 16, 56, 24, 64, 32, 
    39, 7, 47, 15, 55, 23, 63, 31, 
    38, 6, 46, 14, 54, 22, 62, 30, 
    37, 5, 45, 13, 53, 21, 61, 29, 
    36, 4, 44, 12, 52, 20, 60, 28, 
    35, 3, 43, 11, 51, 19, 59, 27, 
    34, 2, 42, 10, 50, 18, 58, 26, 
    33, 1, 41, 9, 49, 17, 57, 25
]

# PC1. 56-bit
PC1 = [
    57, 49, 41, 33, 25, 17, 9, 
    1, 58, 50, 42, 34, 26, 18, 
    10, 2, 59, 51, 43, 35, 27, 
    19, 11, 3, 60, 52, 44, 36, 
    63, 55, 47, 39, 31, 23, 15, 
    7, 62, 54, 46, 38, 30, 22, 
    14, 6, 61, 53, 45, 37, 29, 
    21, 13, 5, 28, 20, 12, 4
]

# PC2. 48-bit
PC2 = [
    14, 17, 11, 24, 1, 5, 
    3, 28, 15, 6, 21, 10, 
    23, 19, 12, 4, 26, 8, 
    16, 7, 27, 20, 13, 2, 
    41, 52, 31, 37, 47, 55, 
    30, 40, 51, 45, 33, 48, 
    44, 49, 39, 56, 34, 53, 
    46, 42, 50, 36, 29, 32
]

# number of left shifts per round. 16 rounds.
nLeftShifts  = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Expansion table. 48bit. For increasing the difusion effect. 
# Also called E-bit Selection Table
ExpansionTable = [
    32,  1,  2,  3,  4, 5, 
    4 ,  5,  6,  7,  8, 9, 
    8,   9, 10, 11, 12, 13, 
    12, 13, 14, 15, 16, 17, 
    16, 17, 18, 19, 20, 21, 
    20, 21, 22, 23, 24, 25, 
    24, 25, 26, 27, 28, 29, 
    28, 29, 30, 31, 32, 1
]

# Permutation function used on the output of the SBoxes. 32-bit.
P = [
    16, 7, 20, 21, 
    29, 12, 28, 17, 
    1, 15, 23, 26, 
    5, 18, 31, 10, 
    2, 8, 24, 14, 
    32, 27, 3, 9, 
    19, 13, 30, 6, 
    22, 11, 4, 25
]

# S-Boxes - 8 x 4x16-bit
sbox = [
    # S1
    [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],

    # S2
    [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],

    # S3
    [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],

    # S4
    [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],

    # S5
    [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],

    # S6
    [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],

    # S7
    [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],

    # S8
    [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ],
]

def binaryToDecimal(binary):
    d = 0
    j = 0
    for i in range(len(binary)-1, -1, -1):
        d += binary[i] * 2**j
        j += 1
    return d

# 4-bit based converter
def decimalToBinary(decimal):
    binary = []
    while(decimal > 0):
        binary.append(decimal%2)
        decimal = decimal // 2
    while(len(binary) < 4):
        binary.append(0)
    binary.reverse()
    return binary

def hexToBinary(hex):
    hexList = list(hex)
    binary = []
    for h in hexList:
        if h == 'A':
            binary.extend([1,0,1,0])
        elif h == 'B':
            binary.extend([1,0,1,1])
        elif h == 'C':
            binary.extend([1,1,0,0])
        elif h == 'D':
            binary.extend([1,1,0,1])
        elif h == 'E':
            binary.extend([1,1,1,0])
        elif h == 'F':
            binary.extend([1,1,1,1])
        else:
            d = int(h)
            tmp = []
            while(d > 0):
                tmp.append(d%2)
                d = d // 2            
            while len(tmp) < 4:
                tmp.append(0)
            tmp.reverse()
            binary.extend(tmp)

    return binary

def binaryToHex(binary):
    res = ''
    # first we gotta convert the binary to decimal 
    decimal = binaryToDecimal(binary)
    # Then convert the decimal back to Hex    
    h = []
    while(decimal > 0):
        h.append(decimal%16)
        decimal = decimal // 16
    
    h.reverse()
    for i in range(len(h)):
        if h[i] == 10: h[i] = 'A'
        elif h[i] == 11: h[i] = 'B'
        elif h[i] == 12: h[i] = 'C'
        elif h[i] == 13: h[i] = 'D'
        elif h[i] == 14: h[i] = 'E'
        elif h[i] == 15: h[i] = 'F'

    for i in h:
        res += str(i)
    
    return res


'''# ----------- Testing -----------'''
# plain text message. 64-bit. 
Msg = '0123456789ABCDEF'
M = hexToBinary(Msg)
L = M[0:32]
R = M[32:]

# Key. 64-bit.
Key = '133457799BBCDFF1'
K = hexToBinary(Key)

# The result cipher text will be: 85E813540F0AB405
'''# --------------------------------'''

# Step 1. Transforming the 64-bit original key to a 56-bit key using PC-1.
KK = [0] * 56
for i in range(0, len(PC1)):
    KK[i] = K[PC1[i]-1]

# Step 2
# Creating two dimensional lists with the capacity of holding 16 different rounds. Each round has 28-bits.
Ci = [ [0]*28 ] * 17
Di = [ [0]*28 ] * 17
# Dividing KK which is a 56-bit key into two equal halves. Each will have 28-bits.
Ci[0] = KK[0:28]
Di[0] = KK[28:]

# step 3. Performing lefts shifts on C and D acquired from KK. We are dealing with 28-bit of data.
# Notice that Ci[0] and Di[0] are the initial states without shifts. 
for i in range(1, 17):
    tmpCi = Ci[i-1][:]
    tmpDi = Di[i-1][:]

    for n in range(nLeftShifts[i-1]):
        
        first = tmpCi[0]
        for j in range(28-1):
            tmpCi[j] = tmpCi[j+1] 
        tmpCi[-1] = first

        first = tmpDi[0]
        for j in range(28-1):
            tmpDi[j] = tmpDi[j+1]
        tmpDi[-1] = first
    
    Ci[i] = tmpCi[:]
    Di[i] = tmpDi[:]

# putting all Cs and Ds from the previous step into one variable as a whole. 
# CiDi[0] is the initial state of the key without shifts!
CiDi = [0] * 17
for i in range(17):
    CiDi[i] = []
    CiDi[i].extend(Ci[i])
    CiDi[i].extend(Di[i])

# Step 4. Applying the 48-bit PC-2 on the CiDi that we calculated in the last step.
# Notice that Ki[0] is the initial sequence and should not be used for further calculations. 
Ki = [0] * 17 # This is going to store [17][48] bit of data
for i in range(17):
    tmp = [0] * 48
    for j in range(len(PC2)):
        tmp[j] = CiDi[i][PC2[j]-1]
    Ki[i] = []
    Ki[i].extend(tmp)

# Step 5. Using IP to Alter M
# Now that the keys are shifted 16 times and are ready it is time to work on the plain text message.
AM = [0] * 64
for i in range(len(IP)):
    AM[i] = M[IP[i]-1]

# Step 6. Using the below formula to create L and R sequences
# L(n) = R(n-1) 
# R(n) = L(n-1) + f(R(n-1), K(n))
Li = [0] * 17
Ri = [0] * 17
# Setting L0 and R0 accroding to the previous step
Li[0] = AM[:32]
Ri[0] = AM[32:]

# A variable to hold E(Ri) of size [16][48]. E function is the expansion table.  
ERi = [0] * 16

# A variable to hold Ki + E(Ri) of size [16][48]
KiERi = [0] * 16

# A variable to hold seperated 8-bit chunks of data from Ki + E(Ri) of size [16][8][6]
Bii = [0] * 16

# A variable to hold the output of S-boxes on B(i) particles. 
SiBi = [0] * 16

# Holds the value of f = P(S(i)B(i))
f = [0] * 16

# This for contains so much code and is repeated for 16 times. 
for r in range(16):

    # Step 6.1 Using the expansion table on Ri to calcualte E(Ri)
    tmp = [0] * 48
    for i in range(len(ExpansionTable)):
        tmp[i] = Ri[r][ExpansionTable[i]-1]
    ERi[r] = []
    ERi[r].extend(tmp)

    if r == 0:
        for i in range(len(ERi[0])):
            if i%6==0 and i != 0:
                print(end=' ')
            print(ERi[r][i], end='')
        print(f' ER{r}')

    # Step 6.2 Calculate K(n) + E(R(n-1))
    # Remember that Ki[0] should be counted as it is the initial state. 
    tmp = [0] * 48
    for i in range(len(Ki[r])):
        tmp[i] = Ki[r+1][i] ^ ERi[r][i]
    KiERi[r] = []
    KiERi[r].extend(tmp)

    if r == 0:
        for i in range(len(KiERi[0])):
            if i%6==0 and i != 0:
                print(end=' ')
            print(KiERi[r][i], end='')
        print(f' KiERi{r}')

    # Dividing the previous result into 8 parts. 
    # K(n) + E(R(n-1)) = B1 B2 B3 B4 B5 B6 B7 B8
    # Bii will be a list of size [16][8][6]
    i = 0
    Bii[r] = [0] * 8
    for k in range(8):
        Bii[r][k] = []
        Bii[r][k].extend(KiERi[r][i:i+6])
        i += 6

    # Time to use the sBoxes. 
    # f = P(S1(B1) S2(B2) S3(B3) S4(B4) S5(B5) S6(B6) S7(B7) S8(B8))
    SiBi[r] = []
    for j in range(8):
        rowList = []
        rowList.append(Bii[r][j][0])
        rowList.append(Bii[r][j][-1])
        row = binaryToDecimal(rowList)
        colList = []
        for a in range(1,5):
            colList.append(Bii[r][j][a])
        col = binaryToDecimal(colList)
        num = sbox[j][row][col]
        SiBi[r].extend(decimalToBinary(num))

    if r == 0:
        for i in range(len(SiBi[0])):
            if i%4==0 and i != 0:
                print(end=' ')
            print(SiBi[r][i], end='')
        print(f' SiBi{r}')

    # Now by using the P table the SiBi calculated before 
    # should be reduced to 32-bit to get our f
    tmp = [0] * 32
    for j in range(len(P)):
        tmp[j] = SiBi[r][P[j]-1]
    f[r] = []
    f[r].extend(tmp)

    if r == 0:
        for i in range(len(f[0])):
            if i%4==0 and i != 0:
                print(end=' ')
            print(f[r][i], end='')
        print(f' f{r}')

    # Now we did all of the above steps to replicate a sequence 
    # accroding to the formula: 
    # L(n) = R(n-1) 
    # R(n) = L(n-1) + f(R(n-1), K(n))
    tmp = [0] * 32 
    for j in range(32):
        tmp[j] = Li[r][j] ^ f[r][j]
    Li[r+1] = Ri[r]
    Ri[r+1] = []
    Ri[r+1].extend(tmp)

    if r == 0:
        for i in range(len(Li[0])):
            if i%4==0 and i != 0:
                print(end=' ')
            print(Li[r][i], end='')
        print(f' Li{r}')

    if r == 0:
        for i in range(len(Ri[0])):
            if i%4==0 and i != 0:
                print(end=' ')
            print(Ri[r+1][i], end='')
        print(f' R{r+1}')

    if r == 15:
        for i in range(len(Li[0])):
            if i%4==0 and i != 0:
                print(end=' ')
            print(Li[r+1][i], end='')
        print(f' Li{r+1}')

    if r == 15:
        for i in range(len(Ri[0])):
            if i%4==0 and i != 0:
                print(end=' ')
            print(Ri[r+1][i], end='')
        print(f' R{r+1}')


R16L16 = []

for i in range(len(Ri[0])):
    if i%4==0 and i != 0:
        print(end=' ')
    R16L16.append(Ri[16][i])
    print(Ri[16][i], end='')

for i in range(len(Ri[0])):
    if i%4==0 and i != 0:
        print(end=' ')
    R16L16.append(Li[16][i])
    print(Li[16][i], end='')

print(f' R16L16')

C = [0] * 64
for i in range(len(IPInv)):
    C[i] = R16L16[IPInv[i]-1]

for i in range(len(C)):
    if i%8==0 and i!=0:
        print(end=' ')
    print(C[i], end='')
print(' IP-1')

print(binaryToHex(C), 'cipher')