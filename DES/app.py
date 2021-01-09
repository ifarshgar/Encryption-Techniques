import DES

if __name__ == "__main__":
    print('Data Encryption Standard (DES)')
    menu = '\n1.Encrypt'
    menu += '\n' + '2.Decrypt'
    menu += '\n' + '0.Exit'
    menu += '\n' + '> '
    ch = -1
    while(ch != 0):
        print(menu, end='')

        try:
            ch = int(input())
        except ValueError:
            print('Indicate your choice by typing only a number!')
            continue

        if ch == 1:
            Message = input('Enter your message to be encrypted: ')
            Key = input('Enter the encryption key: ')
            msg = DES.check_msg(Message)
            K = DES.check_key(Key)

            print('Encrypted Text:', end=' ')
            cipher = DES.encryption(K, msg)
            print(cipher)
        
        elif ch == 2:
            cipher = input('Enter your cipher text to be decrypted: ')
            Key = input('Enter the encryption key: ')
            msg = DES.check_msg(cipher)
            K = DES.check_key(Key)

            print('Decrypted Text:', end=' ')
            Message = DES.decryption(K, cipher)
            print(Message)
            
        elif ch == 0:
            print('Exit....')
            break

        else:
            print('Wrong input!')



