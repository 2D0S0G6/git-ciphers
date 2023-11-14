def rot(inp,key):
    b=""
    for i in inp.lower():
        if i.isalpha():

            a=ord(i)-97
            a=(a+key)%26
            i=chr(a+97)
        b+=i
    return b
if __name__=="__main__":
    a=input("enter a string")
    c=int(input("enter your shift key"))
    b=rot(a,c)
    print(b)
