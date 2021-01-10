def has22(arr):
    for i in range(len(arr)-1):
        if arr[i]==2 and arr[i+1]==2:
            return True
    return False


has_22=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS IN THE ARRAY :"))
for i in range(n):
    has_22.append(int(input("ENTER THE {}'st ELEMENT :".format(i+1))))
if(has22(has_22)):
    print("TRUE")
else:
    print("FALSE")
    
#print(has22([1,2,2]))
#print(has22([1,2,1,2]))
#print(has22([2,1,2]))
