import string
def encrypt():
    pt=input ("Enter the plaintext:").lower().replace(" ","")
    key=input("enter the key:").lower().replace(" ","")
    letters=list(string.ascii_lowercase)
    ki=0
    ct=""
    for i in range(len(pt)):
        li=(letters.index(pt[i])+letters.index(key[ki%len(key)]))%26
        ki +=1
        ct +=letters[li]
    print("The cipher text is ",ct)
    decrypt(ct,key)

def decrypt(ct,key):
    ki=0
    pt=""
    letters=list(string.ascii_lowercase)
    for i in range(len(ct)):
        li=(letters.index(ct[i])-letters.index(key[ki%len(key)]))%26
        ki+=1
        pt +=letters[li]
    print(" The plaintext is ",pt)
    
while(1):
    c=int(input("Enter choice:"))
    if c==1:
        encrypt()
    else:
        break
