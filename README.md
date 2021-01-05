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



## RSA (Rivest-Shamir-Adleman)
RSA is an asymmetric cryptographic algorithm. Assymetric means that there are two differetn keys. A public key and a private key. 

Public key encryption
- if m < n, c = m**e mod n
- m = c**d mod n

Both sender and reciever know the value of n.
The sender knows the value of e, and only the receiver knows the value of d. 

PU = {e, n}
PR = {d, n}


RSA Key Generation
1. choose p and q privately such that p and q are two prime numbers and p!=q
2. Calcualte n, n = p * q
3. Calculate Phi(n) privately, Phi(n) = (p-1)(q-1)
4. choose e publicly such that 1<e<Phi(n) and gcd(Phi(n), e) = 1 and d*e mod(Phi(n))=1
5. privately calcualte d such that d = e**-1 mod(Phi(n)) and d<Phi(n)


Relatively Prime Numbers
Two integers are relatively prime if there is no integer greater than one that divides them both. In other words, they don't have any greater common divisor (GCD) other than 1. 

A typical size for n is 1024-bits or 309 decimal digits less than 2**1024. 