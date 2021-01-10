from os import path
import Hash
import RSA

if __name__ == "__main__":
    print('RSA Algorithm')

    public_key, private_key, n = RSA.simple_init()

    menu = '\n' + '1.Choose a file document to be encrypted'
    menu += '\n' + '2.Choose a file document to be decrypted'
    menu += '\n' + '3.Enter a message to be encrypted'
    menu += '\n' + '4.Enter a cipher to be decrypted'
    menu += '\n' + '5.Choose a file document to be E-Signed'
    menu += '\n' + '6.Enter a message to be E-Signed'
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
            proceed = True

            try:
                file = input('Enter the address of the file document: ')
                if not path.exists(file) or not path.isfile(file):
                    print('File is not found!')
                    proceed = False
                else:
                    f = open(file, 'r')
                    if f.mode == 'r':
                        text = f.read()
                        f.close()
            except:
                proceed = False
            
            # The length of the RSA in bytes e.g. for a 32-bit RSA, length is 4.
            length = 4
            
            if proceed:
                # Performing public-key encryption
                cipher = RSA.encryption(text, public_key, n)
                try:
                    f = open('Encrypted_'+file, 'w')
                    for c in cipher:
                        f.write(str(c) + ' ')
                    f.close()
                    print('\nEncrypted document created successfully!')
                except:
                    print('Document encryption failed!')
        
        if ch == 2:
            proceed = True

            try:
                file = input('Enter the address of the file document: ')
                if not path.exists(file) or not path.isfile(file):
                    print('File is not found!')
                    proceed = False
                else:
                    f = open(file, 'r')
                    if f.mode == 'r':
                        text = f.read()
                        f.close()
            except:
                proceed = False
            
            # The length of the RSA in bytes e.g. for a 32-bit RSA, length is 4.
            length = 4
            
            if proceed:
                cipher = text.split(' ')
                c = []
                for ch in cipher:
                    if ch == ' ' or ch == '':
                        continue
                    c.append(int(ch))
                
                try:
                    m = RSA.decryption(c, private_key, n)
                    file = file.replace('Encrypted_', '')
                    f = open('Decrypted_'+file, 'w')
                    f.write(''.join(m))
                    f.close()
                    print('Decrypted document created successfully!')
                except:
                    print('Document decryption failed!')
        
        elif ch == 3:
            text = input('Enter your message: ')
            
            # The length of the RSA in bytes e.g. for a 32-bit RSA, length is 4.
            length = 4
            
            # Performing public-key encryption
            cipher = RSA.encryption(text, public_key, n)
            print('--Encryption by public key--')
            print('Encrypted text:', cipher)

        elif ch == 4:
            cipher = input('Enter your cipher: ')
            cipher = cipher.replace('[', '')
            cipher = cipher.replace(']', '')
            cipher = cipher.replace(',', '')
            cipher = cipher.replace('-', '')
            c = cipher.split(' ')
            for i in range(len(c)):
                c[i] = c[i].replace(' ', '')
                c[i] = int(c[i])
            
            # The length of the RSA in bytes e.g. for a 32-bit RSA, length is 4.
            length = 4
            
            # Performing public-key encryption
            text = RSA.decryption(c, private_key, n)
            print('--Decryption by private key--')
            print('Decrypted text:', ''.join(text))
        
        elif ch == 5:
            proceed = True

            try:
                file = input('Enter the address of the file document: ')
                if not path.exists(file) or not path.isfile(file):
                    print('File is not found!')
                    proceed = False
                else:
                    f = open(file, 'r')
                    if f.mode == 'r':
                        text = f.read()
                        f.close()
            except:
                proceed = False
            
            # The length of the RSA in bytes e.g. for a 32-bit RSA, length is 4.
            length = 4
            
            if proceed:
                # Getting the hash value of the document 
                hash = Hash.hash(text, length)
                # Performing private_key encryption or e-signature creation
                signature = RSA.E_Signature(hash, private_key, n)
                print('E-Signature:', signature)
                RSA.confirm_signature(hash, public_key, n, signature)



        elif ch == 6:
            text = input('Enter your message: ')
            
            # The length of the RSA in bytes e.g. for a 32-bit RSA, length is 4.
            length = 4
            
            # Getting the hash value of the document 
            hash = Hash.hash(text, length)
            # Performing private_key encryption or e-signature creation
            signature = RSA.E_Signature(hash, private_key, n)
            print('E-Signature:', signature)
            RSA.confirm_signature(hash, public_key, n, signature)
            
        elif ch == 0:
            print('Exit....')
            break


