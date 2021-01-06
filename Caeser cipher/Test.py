import Caeser

if __name__=='__main__':
    Caeser.initializeDictionaries()

    # Test
    message = 'Some random text with UPPER and lower alphabets...!'
    print('Plain Text:', message)
    cipher = Caeser.encryption(message)
    print('Ciphertext:', cipher)

    plain = Caeser.decryption(cipher)
    print('Plain Text:', plain)