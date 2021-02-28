import string

def ceasarCipher(message,n):
    encryptedList=[]
    for char in message:
        if char in string.ascii_letters or char in "1234567890":
            encryptedList.append(chr(ord(char)+n))
        else:
            encryptedList.append(char)
    return "".join(encryptedList)

message=input("ENTER THE STRING :")
n=int(input('ENTER THE NUMBER OF NUMBER OF LETTERS TO SHIFT :'))
print(ceasarCipher(message,n))
