number=int(input("ENTER THE NUMBER :"))
numberCpy=number
if number<0:
    print("INVALID NUMBER !")
count=0
while number>0:
    number=int(number/10)
    count+=1
print(str(numberCpy)+" HAS "+str(count)+" DIGITS")