import Caeser

if __name__ == "__main__":
    print('Caeser Cipher')
    
    menu = '\n1.Encrypt'
    menu += '\n' + '2.Decrypt'
    menu += '\n' + '0.Exit'
    menu += '\n' + '> '
    
    # This function has to be called once before starting.
    Caeser.initializeDictionaries()
    
    ch = -1
    while(ch != 0):
        print(menu, end='')
        
        try:
            ch = int(input())
        except ValueError:
            print('Indicate your choice by typing only a number!')

        if ch == 1:
            message = input('Enter your message to be encrypted: ')
            print('Encrypted Text:', end=' ')
            cipher = Caeser.encryption(message)
            print(cipher)
        
        elif ch == 2:
            cipher = input('Enter your cipher text to be decrypted: ')
            print('Decrypted Text:', end=' ')
            Message = Caeser.decryption(cipher)
            print(Message)
            
        elif ch == 0:
            print('Exit....')
            break

        else:
            print('Wrong input!')



