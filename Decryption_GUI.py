import tkinter as tk
import random
import string
win=tk.Tk()
win.title('Decryption')
win.geometry('300x200')
colours=["cyan","blue","light green"]
Colour=win.configure(background = random.choice(colours))
tk.Label(win,text="Enter Encrypted message: ").grid(row=0,column=0)
e1=tk.Entry(win,width=30)
e1.grid(row=0,column=1)
def message():
    from playsound import playsound
    playsound('play.mp3')
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

    s=(e1.get())
    s=s[::-1]
    tr=rot13(s)
    s=tr
    a=s.split(" ")
    sp=a[-1]
    if(sp[0].isnumeric())==True:
        a.pop()
        temp=len(a[0])
        s=decryption(a)
        s=space(s,sp)
        l1=tk.Label(win,text="The Orginal message is:").grid(row=4,column=0)
        l2=tk.Label(win,text=s).grid(row=4,column=1)
        print(s)
    else:
        re=""
        temp=len(a[0])
        s=decryption(a)
        for i in s:
            re+=i
        l1=tk.Label(win,text="The Orginal message is:").grid(row=4,column=0)
        l2=tk.Label(win,text=re).grid(row=4,column=1)
        print(re)
tk.Button(win,text="Quit",command=win.quit).grid(row=2,column=0)
tk.Button(win,text="Submit",command=message).grid(row=2,column=1)
win.mainloop()
