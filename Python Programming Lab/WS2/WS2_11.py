import math

#function to find the LCM
def lcm(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = math.gcd(lcm, a[i])
  return lcm

a=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS IN THE LIST (5-8) :"))
#finding the lcm of first 3 elements inorder to fill the list A
for i in range(3):
    a.append(int(input("ENTER THE {}' ELEMENT :".format(i+1))))
lcm=lcm(a)
for i in range(3,n):
    a.append(int(lcm*(i+1)))
print("LIST A :")
print(a)
#sclicing the middle elements from a and storing it in c
sliced=slice(int((n/2)-1),int((n/2)+1))
c=list(a[sliced])
print("LIST C :")
print(c)
#taking backup of a in b
b=a
print("LIST B :")
print(b)
#deleting the middle elements of a
del a[int((n/2)-1)]
del a[int(n/2)-1]
print("LIST A AFTER DELETING :")
print(a)
#restoring a by inserting c inbetween a
if n%2 ==0:
    a[-(int((n/2)-1)):0]=c
else:
    a[-(int(n/2)):0]=c
print("LIST A AFTER RESTORING :")
print(a)