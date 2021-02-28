def getinput(list,n):
    for i in range(n):
        list.append(input(f'ENTER THE {i+1} ELEMENT OF THE LIST :'))
    return list

n1=int(input('ENTER THE SIZE OF LIST 1 :'))
n2=int(input('ENTER THE SIZE OF LIST 2 :'))
list1=[]
list2=[]
list1=getinput(list1,n1)
list2=getinput(list2,n2)
list3=[]
for i in range(1,n1,2):
    list3.append(list1[i])
for i in range(0,n2,2):
    list3.append(list2[i])
print(list3)