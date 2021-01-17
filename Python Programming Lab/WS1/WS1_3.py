dnaString=input("ENTER THE DNA SEQUENCE :")
dnaList=['A','C','G','T']
dnaDict=dict.fromkeys(dnaList,0) #(mapping)dnaDict will contain(key from dnaList,frequency)
for i in dnaString.upper():
    if i not in dnaList:#if tthe sequence is incorrect
        print("ENTER VALID SEQUENCE!")
        dnaDict.clear()
        break
    dnaDict[i]+=1 #if sequence is clear then count the frequency

print(dnaDict)