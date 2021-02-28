def equalChunks(inputlist):
    for i in range(0, len(inputlist), 3):  
        yield inputlist[i:i + 3]

inputlist=[]
n=int(input('ENTER THE SIZE OF THE LIST :'))
for i in range(n):
    inputlist.append(input(f'ENTER THE {i+1} ELEMENT OF THE LIST :'))
if len(inputlist)==0:
    print("List Empty!")
else:
    print(inputlist)
    inputlist=list(equalChunks(inputlist))
    print(inputlist)