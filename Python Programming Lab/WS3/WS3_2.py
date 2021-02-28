name=input('ENTER NAME :')
if len(name)==0:
    print('STRING EMPTY!')
else:
    name=name.split()
    if len(name)==1:
        print("".join(name))
    else:
        abbName=''
        for i in range(len(name)-1):
            abbName+=str(name[i][0:1])+'.'
        abbName+=str(name[len(name)-1])
        print(abbName)
    
