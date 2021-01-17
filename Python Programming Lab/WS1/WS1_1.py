#used to find the frequency
def Frequency(str,ch):
    count=0
    for i in range(len(str)):
        if str[i]==ch :
            count+=1
    return count

#create a vector pair(frequency,character) sort it in descending order and print it
def mostFrequent(str):
    n=len(str)
    vect=[]
    for i in range(n):
        vect.append((Frequency(str,str[i]),str[i]))
    vect.sort(reverse=True)
    for i in range(len(vect)):
        print(vect[i][1],end="")

#fetch the input string and passing it to mostFrequent function
if __name__ == "__main__":
    str=input("ENTER THE STRING :")
    mostFrequent(str)
