# Encryption-Techniques
## RSA (Rivest-Shamir-Adleman)
 RSA is an asymmetric cryptographic algorithm. Assymetric means that there are two different keys. Public and private keys refer to the ‘keys’ used to encrypt and decrypt information. A public key is available to many, and made available in an online directory. A private key is private, and only made available to the originator of the encrypted content, and those it is shared with.

#### Public key encryption / decryption
 m stands for the plain text message and c stands for the ciphered text.
 ```if m < n, c = m**e mod n```
 ```m = c**d mod n```

 Both sender and reciever know the value of n.
 The sender knows the value of e, and only the receiver knows the value of d. 

 ```PU = {e, n}```
 ```PR = {d, n}```

#### RSA Key Generation
 The implementation infrastructure requires each user to have a public-private key pair where the public key is available to the world, while the private key is only known by the user.

 1. choose *p* and *q* privately such that *p* and *q* are two prime numbers and ```p!=q```
 2. Calcualte *n*, ```n = p * q```
 3. Calculate *Phi(n)* privately, ```Phi(n) = (p-1)(q-1)```
 4. choose e publicly such that ```1 < e < Phi(n)``` and *Phi(n), e* are relatively prime with each other i.e. ```gcd(Phi(n), e) = 1``` and ```d*e mod(Phi(n))=1```
 5. privately calcualte *d* such that ```d = e**-1 mod(Phi(n))``` and ```d < Phi(n)```


 ![DES Encryption-Decryption Scheme](https://github.com/ifarshgar/Encryption-Techniques/blob/main/RSA%20Encryption.png)

##### Relatively Prime Numbers
 Two integers are relatively prime if there is no integer greater than one that divides them both. In other words, they don't have any greater common divisor (GCD) other than 1. 

 A typical size for n is 1024-bits or 309 decimal digits less than 2**1024. 

#### E-Signature
 An electronic signature (e-signature) is a string of data that is attached to an electronic message in order to guarantee its authenticity, identify the signatory and link the content to that signatory (thereby protecting the recipient against repudiation by the sender). The e-signature provides an effective means of guaranteeing the authenticity and integrity of any document during its life and its importance. To ensure authenticity and integrity of a document, electronic signatures can be applied upon their creation. 


![DES Encryption-Decryption Scheme](https://github.com/ifarshgar/Encryption-Techniques/blob/main/E-Signature.jpg)

 ###### Hash function 
 It is a specific function that generates a defined number of bits of hash of the original message. The hashed message is secure and unique.

