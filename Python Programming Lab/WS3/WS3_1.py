string=input("ENTER THE STRING:")
if len(string)==0:
    print('STRING EMPTY!')
else:
    print(f'THE ENTERED STRING IS :{string}')
    vowelString=[]
    for ch in string:
        if ch in " aeiouAEIOU" or ch in "1234567890":
            vowelString.extend(ch)
    print(f'THE STRING WITHOUT CONSONANTS IS :{"".join(vowelString)}')

