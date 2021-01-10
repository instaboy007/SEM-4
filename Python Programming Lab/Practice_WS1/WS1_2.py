list=[]
n=4
for i in range(0,n):
    print("ENTER {}'st ELEMENT".format(i+1))
    element=str(input())
    list.append(element)
#print(list)
s=[]
for i in range(0,n):
    string=list[i]
    index=string.rfind('.')
    s.append(string[index+1:])
print(s)