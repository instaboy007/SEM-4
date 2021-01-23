import string
from base64 import b64encode, b64decode
import hashlib 
from Cryptodome.Cipher import AES
import os 
from Cryptodome.Random import get_random_bytes

def subCipherEncrypt(encryptMessage):
    #simple substituion is done here
    for char in message:
        if char in allLetters:
            temp=subDic[char]
            encryptMessage.append(temp)
        else:
            temp=char
            encryptMessage.append(temp)
    encryptMessage="".join(encryptMessage)
    return encryptMessage

def encrypt(message,password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(message, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }

#fileAis read
allLetters=string.ascii_letters
FileA=open("FileA.txt","r")
message=FileA.read()
#empty list to store encrypted message
encryptMessage=[]
FileA.close()
subDic={}
key=len(message)
#substitution dictionary is created
for i in range(len(allLetters)):
    subDic[allLetters[i]]=allLetters[(i+key)%len(allLetters)]

password="instaboy"
FileB=open("FileB.txt","w")
#substitution cipher encryption is done
encryptMessage=subCipherEncrypt(encryptMessage)
#AES-256 encryption is done here
FileB.write(str(encrypt(encryptMessage,password)))
FileB.close()
