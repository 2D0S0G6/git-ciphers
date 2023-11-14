def affine(inp,a,b):
    p=""
    for i in inp.lower():
        if i.isalpha():
            s=ord(i)-97
            cipher=((a*s) + (b))%26
            i=chr(cipher+97)
        p+=i
    return p

if __name__=="__main__":
    print("a")
    inp=input("enter the plain text:")
    a , b=map(int,input("enter the keyvalue pair").split())
    c=affine(inp,a,b)
    print(c)
