def getInput(s):
    n=int(input("ENTER THE NUMBER OF ELEMENTS IN SET:"))
    for i in range(n):
        s.add(int(input("ENTER THE {}'st ELEMENT :".format(i+1))))
    return s

setA=set()
setB=set()
setA=getInput(setA)
setB=getInput(setB)

print(setA.union(setB))
print(setA.intersection(setB))
print(setA.difference(setB))
print(setA.symmetric_difference(setB))