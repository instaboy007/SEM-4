string=input("ENTER THE SENTENCE :").split(" ")
words=[]
for i in string:
    if not i in words:
        words.append(i)
    else:
        continue
words.sort()
print((' ').join(words))    