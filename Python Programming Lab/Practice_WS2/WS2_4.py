x=set()
n=int(input("ENTER THE NUMBER OF ELEMENTS :"))
for i in range(n):
    x.add(int(input("ENTER THE {}'st ELEMENT :".format(i+1))))
print(str(max(x))+" is The Maximum Value")
print(str(min(x))+" is The Minimum Value")