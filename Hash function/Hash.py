'''
 XOR Hash Algorithm
--------------------------
-- Abdolrahman Farshgar --
    January 7, 2021
--------------------------
'''

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


def convert_msg_to_blocks_of_8bit_array(msg, nBytes):
    M = []
    
    for m in msg:
        tmp = []
        tmp.extend(decimalToBinary(ord(m)))
        while len(tmp) < 8:
            tmp.insert(0,0)
        M.extend(tmp)
    
    while len(M) < nBytes*8:
        M.insert(0,0)

    return M


def generate_key(nBytes):
    K = []
    # The repeated key is 01
    # The size of the key should be same as the requested length of the hash
    while len(K) < nBytes*8:
        K.append(0)
        K.append(1)
        
    return K


def check_text(Message, nBytes):
    msg = []
    msg.append(Message[:nBytes])
    Message = Message.replace(Message[:nBytes], '', 1)
    while len(Message) > 0:
        msg.append(Message[:nBytes])
        Message = Message.replace(Message[:nBytes], '', 1)

    return msg


def hash(text, nBytes):
    h = [0] *  nBytes*8

    key = generate_key(nBytes)
    msg = check_text(text, nBytes)

    for m in msg: 
        cm = convert_msg_to_blocks_of_8bit_array(m, nBytes)
        for i in range(nBytes*8):
            temp = cm[i] ^ key[i]
            h[i] = h[i] ^ temp

    return h