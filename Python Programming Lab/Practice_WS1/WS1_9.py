def centeredAverage(num):
    return (sum(num)-max(num)-min(num))/(len(num)-2)

arr=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS IN THE ARRAY:"))
for i in range(n):
    arr.append(int(input("ENTER THE {}'st ELEMENT :".format(i+1))))
print(centeredAverage(arr))
