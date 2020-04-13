import math
import string
def rot13(txt):
    rot13trans=str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 123456789','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghi@!#^~{":;?/|}>')
    return txt.translate(rot13trans)
def count_spaces(s):
    ls=[]
    sp=""
    for i in range(len(s)):
        if(s[i]==' ' or s[i]=='\n' or s[i]=='\t'):
            ls.append(i*99998)
    for i in ls:
        sp+=str(i)+','
    return sp

def encryption(s):
    s=s.replace(" ","")
    l=len(s)
    sq=l**0.5
    r=int(math.floor(sq))
    c=int(math.ceil(sq))
    check=r*c
    if(check<l):
        r=r+1
    re=""
    for i in range(c):
        if(i==0):
            re=re+(s[i::c])
        else:
            re=re+" "+(s[i::c])
    return re+' '

s=input("Enter the message:")
ls=count_spaces(s)
msg=encryption(s)
msg+=ls
l=len(msg)
msg=msg[:l-1]
msg=msg[::-1]
txt=rot13(msg)
print(txt)
