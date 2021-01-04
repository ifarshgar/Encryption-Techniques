# Encryption-Techniques


## Data Encryption Standard - DES

### Usage:

#### Encryption
 1. ```import DES```
 2. Use ```DES.check_msg()``` function on your plain text to prepare it for encryption.
 3. Use ```DES.check_key()``` function on your encryption key to prepare it for further operations. 
 4. ```DES.encryption(<Key>, <Plain Text>)```
  
  ```python
  msg = DES.check_msg('Your Plain Text Message')
  K = DES.check_key('Your Encryption Key')

  print('Encrypted Text:', end=' ')
  cipher = DES.encryption(K, msg)
  print(cipher)

  print('Decrypted Text:', end=' ')
  Message = DES.decryption(K, cipher)
  print(Message)
  ```

#### Decryption
 1. ```import DES```
 2. Use ```DES.check_key()``` function on your encryption/decryption key.
 3. ```DES.decryption(<Key>, <Cipher Text>)```
  
  ```python
  K = DES.check_key('Your Encryption Key')
  print('Decrypted Text:', end=' ')
  Message = DES.decryption(K, cipher)
  print(Message)
  ```


![DES Encryption-Decryption Scheme](https://github.com/ifarshgar/Encryption-Techniques/blob/main/DES_Encryption_Decryption.jpg)
