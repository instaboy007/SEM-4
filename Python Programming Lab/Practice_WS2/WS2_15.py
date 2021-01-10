import random,string

passwordLength = int(input("ENTER THE LENGTH OF THE PASSWORD :"))
passwordCharacters = string.ascii_letters + string.digits + string.punctuation
password = []
for x in range(passwordLength):
    password.append(random.choice(passwordCharacters))
string=""
print("PASSWORD")
print(string.join(password))