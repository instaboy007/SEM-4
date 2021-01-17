#recursively find the maximum number
def findMax(arr):
    if(len(arr)==1):
        return arr[0]
    else :
        first=findMax(arr[1:])
        return arr[0] if first < arr[0] else first

#get input and pass it to recursive function
if __name__ == "__main__" :
    arr=[]
    n=int(input("ENTER THE NUMBER OF INTEGERS :"))
    for i in range(n):
        arr.append(int(input("ENTER THE {}'st ELEMENT :".format(i+1))))
    print(str(findMax(arr))+" is The Maximum Number ") 