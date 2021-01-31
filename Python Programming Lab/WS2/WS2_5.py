def getinput(a):
    for i in range(n):
        a.append(float(input("ENTER THE {}' ELEMENT :".format(i+1))))
    return a
def normaliseList(list):
    normList=[]
    for i in range(n):
        normList.append(round((list[i]-min(list))/(max(list)-min(list)),2))
    return normList

if __name__=="__main__":
    list=[]
    n=int(input("ENTER THE NUMBER OF ELEMENTS IN THE LIST:"))
    print("ENTER THE ELEMENTS OF THE LIST :")
    list=getinput(list)
    print(normaliseList(list))