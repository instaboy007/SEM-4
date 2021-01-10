def removeDuplicates(list):
    list=set(list)
    return list

list=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS IN THE LIST :"))
for i in range(n):
    list.append(int(input("ENTER THE {}'st ELEMENT :".format(i+1))))
list=removeDuplicates(list)
print(list)
