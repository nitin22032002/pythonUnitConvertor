def decimalto(n,m):
    if int(m)!=1:
        l="0123456789ABCDEF"
        a=""
        while True:
            if n==0:
                break
            a+=str(int(n)%int(m))+" "
            n=int(n)//m
        if var2.get()=="binary":
            a=a.replace(" ","")
            return a[::-1]
        else:
            b=""
            a=list(a.split())
            for item in a:
              b+=l[int(item)]
            return b[::-1]
    else:
        return n
def decimalfrom(n,m):
    l="0123456789ABCDEF"
    n=str(n)[::-1]
    ans=0
    for i in range(0,len(n)):
        ans+=int(l.index(n[i].upper()))*(int(m)**i)
    return ans
def conversion(list1,list2):
    global lable,y
    if var1.get()!="NONE" or var2.get()!="NONE":
        x = value1.get()
        try:
            x=float(x)
            test=1
        except:
            test=0
        if test==1:
            try:
                lable.destroy()
            except:
                pass
            y = (float(x) * list1[list2.index(var1.get())] / list1[list2.index(var2.get())])
            lable = Label(text=f"{y}\n\n1{var1.get()}={(y / float(value1.get()))}{var2.get()}", bg="white", fg="gray",
                          font="comicsansms 13 bold", borderwidth=3, relief=SUNKEN)
            lable.place(x=180, y=130)
        else:
            msg.showerror("ERROR", "Entry area not be empty or character not be convertable")
            value1.set(0)
    else:
        msg.showerror("ERROR","Dimension not be none")
from tkinter import *
import tkinter.messagebox as msg
from PIL import Image,ImageTk
root=Tk()
image1=Image.open("mesure.jpg")
image=ImageTk.PhotoImage(image1)
Label(image=image).place(x=0,y=0)
root.geometry("477x283")
root.wm_iconphoto(True,image)
root.title("UNIT CONVERTOR")
lengthlist=["mm","cm","dm","m","dam","hm","km","inch","foot","yard","miles"]
weightlist=["mg","ct(carat)","g","kg","ton"]
temperaturelist=["K","C","F"]
volumelist=["ml","cm cube","dm cube","m cube","l","dl","cl"]
timelist=["mili second","second","minute","hours","days","weeks","months","years"]
datalist=["bit","byte","kb","mb","gb","tb"]
numbersystemlist=["decimal","binary","octa","hexa"]
list1=[lengthlist,weightlist,temperaturelist,volumelist,timelist,datalist,numbersystemlist]
list2=["Length","Weight","Temperature","Volume","Time","Data","Number system"]
def convert():
    if text.get()=="Length":
        cm=[0.1,1,10,100,1000,10000,100000,2.54,30.48,91.44,160934.4]
        conversion(cm,lengthlist)
    elif text.get()=="Data":
        bit=[1,8,8192,8388608,8589934560,8.79609302e12]
        conversion(bit,datalist)
    elif text.get()=="Number system":
        global lable2
        if var1.get()!="NONE" and var2.get()!="NONE":
            x=value1.get()
            if x!="":
                try:
                    lable2.destroy()
                except:
                    pass
                if var1.get()=="decimal":
                    dec=[10,2,8,16]
                    ans="("+str(decimalto(x,dec[numbersystemlist.index(var2.get())]))+")"+str(dec[numbersystemlist.index(var2.get())])
                    st=f"{var2.get()} = {dec[numbersystemlist.index(var2.get())]} bits "
                else:
                    dec = [10, 2, 8, 16]
                    ans=decimalfrom(x,dec[numbersystemlist.index(var1.get())])
                    ans = "("+str(decimalto(ans, dec[numbersystemlist.index(var2.get())]))+")"+str(dec[numbersystemlist.index(var2.get())])
                    st = f"{var2.get()} = {dec[numbersystemlist.index(var2.get())]} bits "
                lable2=Label(text=f"{ans}\n\n{st}",bg="white",fg="gray",font="comicsansms 13 bold",borderwidth=3,relief=SUNKEN)
                lable2.place(x=180,y=130)
            else:
                msg.showerror("ERROR","Entry area not be empty or character not be convertable")
                value1.set(0)
        else:
            msg.showerror("ERROR","Dimension not be none")
    elif text.get()=="Volume":
        ml=[1,1,1000,1000000,1000,100,10]
        conversion(ml,volumelist)
    elif text.get()=="Time":
        ms=[1,1000,60000,3600000,86400000,604800000,2592000000,31536000000]
        conversion(ms,timelist)
    elif text.get()=="Weight":
        mg=[1,200,1000,1000000,1000000000]
        conversion(mg,weightlist)
    elif text.get()=="Temperature":
        global lable1
        if var1.get()!="NONE" and var2.get()!="NONE":
            x=value1.get()
            try:
                x = float(x)
                test = 1
            except:
                test = 0
            if test==1:
                try:
                    lable1.destroy()
                except:
                    pass
                if var1.get()=="C" and var2.get()=="F":
                    value=(9*x/5)+32
                    st="F = 9xC/5 + 32"
                elif var1.get()=="C" and var2.get()=="K":
                    value=273+x
                    st="K = C + 273"
                elif var1.get()=="F" and var2.get()=="K":
                    value=(x-32)*5/9+273
                    st="K = (F - 32 ) x 5/9 + 273"
                elif var1.get()=="F" and var2.get()=="C":
                    value = (x - 32) * 5 / 9
                    st = "C = (F - 32 ) x 5/9"
                elif var1.get()=="K" and var2.get()=="C":
                    value=x-273
                    st="C = K - 273"
                elif var1.get()=="K" and var2.get()=="F":
                    value=((x-273)*9/5)+32
                    st="F = (K - 273 ) x 9/5 + 32"
                else:
                    value=x
                    st=var1.get()+" = "+var1.get()
                lable1 = Label(text=f"{value}\n\n{st}",bg="white",fg="gray",font="comicsansms 13 bold",borderwidth=3,relief=SUNKEN)
                lable1.place(x=180, y=130)
            else:
                msg.showerror("ERROR","Entry box not be empty or character not be convertable")
                value1.set(0)
        else:
            msg.showerror("ERROR","Dimension not be none")
def back():
    for item in [lable,lable1,lable2]:
        try:
            item.destroy()
        except:
            pass
    ask2.destroy()
    convertbutton.destroy()
    backbutton.destroy()
    textarea.destroy()
    ask1.destroy()
    main()
def nextfunc():
    global var1,var2,value1,ask2,convertbutton,ask1,backbutton,textarea
    if text.get()!="NONE":
        menu.destroy()
        nextbutton.destroy()
        var1= StringVar()
        var1.set("NONE")
        t=list1[list2.index(text.get())]
        ask1 = OptionMenu(root, var1, *t)
        ask1.place(x=70, y=80)
        value1=StringVar()
        textarea=Entry(textvariable=value1,bg="white",fg="gray",font="comicsansms 15 bold",borderwidth=3,relief=SUNKEN)
        textarea.place(x=180,y=80)
        var2=StringVar()
        var2.set("NONE")
        ask2 = OptionMenu(root, var2, *t)
        ask2.place(x=70, y=160)
        convertbutton=Button(text="Convert",command=convert,font="comicsansms 15 bold",borderwidth=2,relief=GROOVE,background="white",fg="gray")
        convertbutton.place(x=180,y=240)
        backbutton=Button(text="BACK",command=back,font="comicsansms 15 bold",borderwidth=2,relief=GROOVE,background="white",fg="gray")
        backbutton.place(x=403,y=2)
    else:
        msg.showerror("ERROR","Please select some dimension not left it None")
def main():
    global text,menu,nextbutton
    text=StringVar()
    text.set("NONE")
    menu=OptionMenu(root,text,*list2)
    menu.place(x=100,y=100)
    nextbutton=Button(text="next",command=nextfunc,font="comicsansms 15 bold",borderwidth=2,relief=GROOVE,background="white",fg="gray")
    nextbutton.place(x=290,y=95)
lable1=2
lable=1
lable2=3
main()
root.mainloop()