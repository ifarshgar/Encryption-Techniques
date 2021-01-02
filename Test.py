import DES


def Test1():
    # plain text message. 64-bit. 
    Msg = '0123456789ABCDEF'
    M = DES.hexToBinary(Msg)

    # Key. 64-bit.
    Key = '133457799BBCDFF1'
    K = DES.hexToBinary(Key)

    print('Text Message:  ', Msg)
    cipher = DES.DES_Encryption_Decryption(K, M, DES.ENCRYPT)
    print('Encrypted Text:', cipher)
    
    C = DES.hexToBinary(cipher)
    plain = DES.DES_Encryption_Decryption(K, C, DES.DECRYPT)
    print('Decrypted Text:', plain)


def Test2():
    Message = 'A very very very very long text message to be encrypted!'
    print('Text Message:  ', Message)
    Key = 'Some Random Secret Key'

    msg = DES.check_msg(Message)
    K = DES.check_key(Key)

    print('Encrypted Text:', end=' ')
    cipher = DES.encryption(K, msg)
    print(cipher)

    print('Decrypted Text:', end=' ')
    Message = DES.decryption(K, cipher)
    print(Message)


if __name__ == '__main__':
    ''' ----------- Test ----------- '''
    print('\n--Test 1--')
    Test1()

    print('\n--Test 2--')
    Test2()
    ''' ------------------------------ '''