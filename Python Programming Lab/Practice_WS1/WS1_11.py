def kaprekar(num):
    square=str(num**2)
    left=""
    right=""
    if(len(square)%2==0):
        left=square[0:len(square)//2]
        right=square[len(square)//2:]
        print(int(left)+int(right))
        if( int(left) + int(right) == num ):
            print(str(left)+" + "+str(right))
            return True
    elif (int(square[:len(square)//2])+int(square[len(square)//2+1]))==num:
        print(str(left)+" + "+str(right))
        return True
    return False


number=int(input("ENTER THE NUMBER :"))
if number>3:
    if (kaprekar(number)==True):
        print('TRUE, The given Number {} is a Kaprekar Number '.format(number))
    else:
        print('FALSE, The given Number {} is Not Kaprekar Number '.format(number))
elif number==1:
    print('TRUE, The given Number {} is a Kaprekar Number '.format(number))
else:
    print("FALSE, The given Number {} is Not Kaprekar Number ".format(number))