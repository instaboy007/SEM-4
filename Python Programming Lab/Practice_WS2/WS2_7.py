def getInput(s):
    n=int(input("ENTER THE NUMBER OF ELEMENTS IN SET:"))
    for i in range(n):
        s.add(int(input("ENTER THE {}'st ELEMENT :".format(i+1))))
    return s

setA=set()
setB=set()
setA=getInput(setA)
setB=getInput(setB)
sorted(setA)
sorted(setB)

if setA==setB:
    print("SETS ARE EQUAL")
else:
    B1=[i for i in setA if i not in setB]
    B2=[i for i in setB if i not in setA]
    print(B1)
    print(B2)