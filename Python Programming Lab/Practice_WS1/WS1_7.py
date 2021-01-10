def checkPangram(string):
    list=[]
    for i in range(26):
        list.append(False)
    for character in string.lower():
        if character !=" ":
            list[ord(character)-ord('a')]=True
    for status in list:
        if(status==False):
            return False
    return True

string=input("ENTER THE STRING:")
if(checkPangram(string)):
    print('" '+string+' "'+ ' is a Paragram ')
else:
    print('" '+string+' "'+ ' is not a Paragram ')

