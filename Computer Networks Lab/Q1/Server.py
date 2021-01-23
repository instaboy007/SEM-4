import string
import ast
from base64 import b64encode, b64decode
import hashlib 
from Cryptodome.Cipher import AES
import os 
from Cryptodome.Random import get_random_bytes

def subCipherDecrypt(encryptMessage,decryptMessage):
    #simple substitution is done here 
    for char in encryptMessage:
        if char in allLetters:
            temp=subDic[char]
            decryptMessage.append(temp)
        else:
            temp=char
            decryptMessage.append(temp)
    decryptMessage="".join(decryptMessage)
    return decryptMessage

def decrypt(encryptMessage, password):
    # decode the dictionary entries from base64
    salt = b64decode(encryptMessage['salt'])
    cipher_text = b64decode(encryptMessage['cipher_text'])
    nonce = b64decode(encryptMessage['nonce'])
    tag = b64decode(encryptMessage['tag'])
    
    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted


allLetters=string.ascii_letters
#fileb is read and text is copied to encryptmessage
FileB=open("FileB.txt","r")
encryptMessage=FileB.read()
#string is transformed into a dictionary
encryptMessage=ast.literal_eval(encryptMessage)
FileB.close()
#empty list to store the final decrypted message
Message=[]
subDic={}

password="instaboy"
#AES-256 decryption is done here
encryptMessage=decrypt(encryptMessage,password)
encryptMessage=bytes.decode(encryptMessage)
#substitution ciper decryption is done here
key=len(encryptMessage)
#creating substitution dictionary
for i in range(len(allLetters)):
    subDic[allLetters[i]]=allLetters[(i-key)%len(allLetters)]

FileC=open("FileC.txt","w")
FileC.write(subCipherDecrypt(encryptMessage,Message))
FileC.close()
