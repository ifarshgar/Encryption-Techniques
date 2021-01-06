import Vigenere

if __name__=='__main__':
    Vigenere.initializeDictionaries()

    # Test
    key = 'EncryptionKey'
    print('Key:', key)
    message = 'Some random text with UPPER and lower alphabets...!'
    print('Plain Text:', message)
    cipher = Vigenere.encryption(key, message)
    print('Ciphertext:', cipher)

    plain = Vigenere.decryption(key, cipher)
    print('Plain Text:', plain)