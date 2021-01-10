def RLEncoding(string):
    encoded_string=""
    i=0
    while i<len(string):
        count=1
        while i+1<len(string) and string[i]==string[i+1] :
            count+=1
            i+=1
        encoded_string+=str(count)+string[i]
        i+=1
    return encoded_string
    
hsl=input("ENTER THE HYPOTHETICAL SCAN LINE :")
print(RLEncoding(hsl))