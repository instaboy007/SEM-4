def ceasarCipher(string):
    key=4
    encryptedList=[]
    for char in string:
        encryptedList.append(chr(ord(char)+key))
    return "".join(encryptedList)

if __name__=="__main__":
    string=input("ENTER THE STRING :")
    print(ceasarCipher(string))