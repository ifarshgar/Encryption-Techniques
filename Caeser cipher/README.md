# Encryption-Techniques


## Caeser Cipher
Caesar cipher (or Caesar code) is a shift cipher, one of the most easy and most famous encryption systems. It uses the substitution of a letter by another one further in the alphabet.

### Usage:

#### Encryption
 1. ```import Caeser```
 2. ```Caeser.encryption(<Plain Text>)```

  ```python
  print('Encrypted Text:', end=' ')
  cipher = Caeser.encryption('<Your Plain Text Message>')
  print(cipher)
  ```

#### Decryption
 1. ```import Caeser```
 2. ```Caeser.decryption(<Cipher Text>)```
  
  ```python
  print('Decrypted Text:', end=' ')
  Message = Caeser.decryption('<The encrypted cipher>')
  print(Message)
  ```
