pt = int(input("Enter the plan text"))
p = int(input("Enter the first prime number"))
q = int(input("Enter the second prime number"))
n = p*q
pi = (p-1)*(q-1)

e = int(input("Enter your public key e"))
x=1
while((e*x)%pi!=1):
    x+=1
print("corresponding d(private key) is ",x)
cip = (pt**e)%n
print("The cipher text is",cip)
dec = (cip**x)%n
print("The decrypted text is ",dec)
