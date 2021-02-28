import random
import collections

def findFreq(randList):
    freqList=[]
    freqList.append(collections.Counter(randomList))
    return freqList
randomList=[]
start=int(input('ENTER THE STARTING RANGE:'))
end=int(input('ENTER THE ENDING RANGE:'))
for i in range(100):
    randomList.append(random.randint(start,end))
freqList=findFreq(randomList)

print(randomList)
print(freqList)