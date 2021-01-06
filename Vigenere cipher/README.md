# Encryption-Techniques


## Vigenere Cipher
Vigenère cipher is a method of encrypting alphabetic substitution system that use a key and a double-entry table. It employs a form of polyalphabetic substitution. The Vigenère cipher encrypts alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. 

### Usage:

#### Encryption
 1. ```import Vigenere```
 2. ```Vigenere.encryption(<Encryption key>, <Plain Text>)```

  ```python
  print('Encrypted Text:', end=' ')
  cipher = Vigenere.encryption('<Encryption key>', '<Your Plain Text Message>')
  print(cipher)
  ```

#### Decryption
 1. ```import Vigenere```
 2. ```Vigenere.decryption(<Encryption key>, <Cipher Text>)```
  
  ```python
  print('Decrypted Text:', end=' ')
  Message = Vigenere.decryption('<Encryption key>', '<The encrypted cipher>')
  print(Message)
  ```
