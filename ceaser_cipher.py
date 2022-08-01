import string
def encrypt():
    pt=input("pt: ").lower().replace(" ","")
    key=int(input("key: "))
    ct=""
    
    for ele in pt:
        ascii =ord(ele)
        ascii -=ord('a')
        ascii +=key
        ascii %=26
        ascii +=ord('a')
        ct +=chr(ascii)
    print("ct :", ct)
    
def decrypt():
    ct= input("ct: ").lower().replace(" ","")
    key= int(input("key: "))
    pt=""
    for ele in ct:
        ascii = ord(ele)
        ascii -= ord('a')
        ascii -=key
        ascii %=26
        ascii += ord('a')
        pt +=chr(ascii)
    print("pt: ",pt)
    
while(1):
    c= int(input("Enter your choice:"))
    if c==1:
        encrypt()
    elif c==2:
        decrypt()
    else:
        break
