import math
import random
message=int(input("Enter the message:"))
p=int(input("enter p value"))
q= int(input("Enter q value"))
phi=(p-1)*(q-1)
n=p*q
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
l1=[]
for r in range(3,phi,2):
    while True:
        if gcd(r,phi)==1:
            l1.append(r)
            break
        else:
            r +=1
print(l1)
l1=list(set(l1))
print(l1)
e=random.choice(l1)
print("e:",e)
d=1
while((d*e)%phi!=1):
    d+=1
print("d:",d)
def encrypt(me):
    en=me**e
    c=en%n
    print("Encrypted text is ",c)
    return c
def decrypt(c):
    dc=c**d
    orgi=dc%n
    print("Original txt is ",orgi)
    return orgi
c=encrypt(message)
orgi=decrypt(c)
