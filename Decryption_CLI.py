import string
sravan-thumma/Encryption-Decryption-mini-project-with-GUI
def rot13(txt):
    rot13trans=str.maketrans('NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghi@!#^~{":;?/|}>','ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 123456789')
    return txt.translate(rot13trans)
def add_spaces(a):
    dummy=[]
    for i in a:
        tmp=len(i)
        diff=abs(temp-tmp)
        if(temp>tmp):
            i+=diff*' '
            dummy.append(i)
        else:
            dummy.append(i)
    return dummy

def decryption(a):
    l=add_spaces(a)
    s=[]
    for i in range(len(l[0])):
        for j in l:
            s+=j[i]
    return s

def space(s,sp):
    result=""
    se=sp
    se=sp.replace(","," ")
    ls=se.split(" ")
    if(ls[-1]==' '):
        ls.pop()
    for i in ls:
        s.insert(int(int(i)/99998),' ')
    for i in s:
        result+=i
    return result

s=input("Enter Encrypted message:")
s=s[::-1]
s=rot13(s)
a=s.split(" ")
sp=a[-1]
if(sp[0].isnumeric())==True:
    a.pop()
    temp=len(a[0])
    s=decryption(a)
    s=space(s,sp)
    print(s)
else:
    re=""
    temp=len(a[0])
    s=decryption(a)
    for i in s:
        re+=i
    print(re)
