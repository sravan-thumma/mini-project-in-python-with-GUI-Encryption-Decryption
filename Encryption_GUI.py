import tkinter as tk
import random
import string
win=tk.Tk()
win.title('Encryption')
win.geometry('300x200')
colours=["cyan","blue","light green"]
Colour=win.configure(background = random.choice(colours))
tk.Label(win,text="Enter the message: ").grid(row=0,column=0)
e1=tk.Entry(win,width=30)
e1.grid(row=0,column=1)
def message():
    import math
    from playsound import playsound
    playsound('play.mp3')
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

    s=(e1.get())
    ls=count_spaces(s)
    msg=encryption(s)
    msg+=ls
    l=len(msg)
    msg=msg[:l-1]
    msg=msg[::-1]
    txt=rot13(msg)
    l1=tk.Label(win,text="The encrypted message is:").grid(row=4,column=0)
    l2=tk.Label(win,text=txt).grid(row=4,column=1)
    print("The encrypted message is:",txt)
tk.Button(win,text="Quit",command=win.quit).grid(row=2,column=0)
tk.Button(win,text="Submit",command=message).grid(row=2,column=1)
win.mainloop()

