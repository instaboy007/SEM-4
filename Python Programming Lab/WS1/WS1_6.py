dictionary={
        "converse":"conserve",
        "lela":"ella",
        "road":"rod",
        "peter":"potter",
        "1234":"4213"
}


def findMethasis(dictionary):
    for key,value in dictionary.items():
        if(len(key)!=len(value)):
            continue
        keyList=list(key)#key will be in a list
        valueList=list(value)#value will be in a list
        for i in range(len(keyList)):
            if keyList[i] != valueList[i]: #chracters doesnt match
                index=valueList.index(keyList[i])#used to find the index
                temp=valueList[i] #basic swapping is done using temp variable
                valueList[i]=valueList[index]
                valueList[index]=temp
                if(str(keyList)==str(valueList)):
                    print(key+" & "+value+" form a Metathesis Pair")

if __name__=="__main__":
    findMethasis(dictionary)