def vigenere(inp,key):
    p=""
    key=[ord(i)-97 if i.isalpha() else ord(i) for i in key.lower()]
    ctr=0
    for j in inp.lower():
        if j.isalpha():
            s=ord(j)-97
            cipher=(s+key[ctr])%26
            j=chr(cipher+97)
            ctr=(ctr+1)%len(key)
        p+=j
    return p

if __name__=="__main__":
    print("a")
    inp=input("enter the plain text:")
    key=input("enter the key string")
    c=vigenere(inp,key)
    print(c)
