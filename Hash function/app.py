from os import path
import Hash

if __name__ == "__main__":
    print('XOR Hash Function')
    menu = '\n1.Choose a file document to be hashed'
    menu += '\n' + '2.Enter a message to be hashed'
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
            text = ''
            key = 0

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
            
            if proceed:
                try:
                    key = int(input('Enter the hash key length in number of bytes '
                    + '(e.g. enter 4 to get a 4-byte i.e. 32-bit hash): '))
                except ValueError:
                    proceed = False
                    print('Type only a number to indicate the key length!')
            
            if proceed:
                h = Hash.hash(text, key)
                output = ''
                for i in h:
                    output += str(i)
                print('Hashed text:', output)
        
        elif ch == 2:
            proceed = True
            key = 0

            text = input('Enter your text: ')

            try:
                key = int(input('Enter the hash key length in number of bytes '
                    + '(e.g. enter 4 to get a 4-byte i.e. 32-bit hash): '))
            except ValueError:
                proceed = False
                print('Type only a number to indicate the key length!')
            
            if proceed:
                h = Hash.hash(text, key)
                output = ''
                for i in h:
                    output += str(i)
                print('Hashed text:', output)
            
        elif ch == 0:
            print('Exit....')
            break

        else:
            print('Wrong input!')



