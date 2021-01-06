import Vigenere

if __name__ == "__main__":
    print('Vigenere Cipher')
    
    menu = '\n1.Encrypt'
    menu += '\n' + '2.Decrypt'
    menu += '\n' + '0.Exit'
    menu += '\n' + '> '
    
    # This function has to be called once before starting.
    Vigenere.initializeDictionaries()
    
    ch = -1
    while(ch != 0):
        print(menu, end='')
        
        try:
            ch = int(input())
        except ValueError:
            print('Indicate your choice by typing only a number!')

        if ch == 1:
            message = input('Enter your message to be encrypted: ')
            key = input('Enter your encryption key: ')
            keyStatus = True
            for k in key:
                if not k.isalpha():
                    print('Your encryption key should be consisted of alphabets only!')
                    keyStatus = False
            
            if keyStatus:
                print('Encrypted Text:', end=' ')
                cipher = Vigenere.encryption(key, message)
                print(cipher)
        
        elif ch == 2:
            cipher = input('Enter your cipher to be decrypted: ')
            key = input('Enter your encryption key: ')
            keyStatus = True
            for k in key:
                if not k.isalpha():
                    print('Your encryption key should be consisted of alphabets only!')
                    keyStatus = False
            
            if keyStatus:
                print('Decrypted Text:', end=' ')
                message = Vigenere.decryption(key, cipher)
                print(message)
            
        elif ch == 0:
            print('Exit....')
            break

        else:
            print('Wrong input!')



