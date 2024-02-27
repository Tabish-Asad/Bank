import sys
from tkinter import *
from tkinter import messagebox
import random
#from PIL import Image,ImageTk

def submit():
    a=e1.get()
    b=e2.get()
    if(a==None and b==None):
        sys.exit()
    else:
        acno=random.randint(30050000,40050000)
        en.insert(0,str(acno))
        messagebox.showinfo("Successful","Successfully Submitted")

def withdrawl():
    def minus():
        amt = int(de1.get())
        pamt = int(e2.get())
        namt = pamt - amt
        de2.insert(0, str(namt))

    withwin=Tk()
    withwin.configure(bg="Black")
    withwin.geometry("450x400")
    dl1=Label(withwin, text="Enter Amount", font=("Times New Roman", 15), padx=20,bg="#808080",fg="White")
    dl2=Label(withwin, text="Available Amount", font=("Times New Roman", 15), padx=2,bg="#808080",fg="White")

    db1=Button(withwin, text="Withdraw", font=("Times New Roman", 15), padx=20,bg="#808080",fg="White",command=minus)


    de1=Entry(withwin,width=30)
    de2=Entry(withwin,width=30)





    dl1.place(x=10,y=10)
    de1.place(x=180,y=10)
    dl2.place(x=10,y=50)
    de2.place(x=180,y=60)
    db1.place(x=180,y=250)

    withwin.mainloop()

def deposit():
    def add():
        amt = int(de1.get())
        pamt = int(e2.get())
        namt = amt + pamt
        de2.insert(0, str(namt))

    depwin=Tk()
    depwin.configure(bg="Black")
    depwin.geometry("450x400")
    dl1=Label(depwin, text="Enter Amount", font=("Times New Roman", 15), padx=20,bg="#808080",fg="White")
    dl2=Label(depwin, text="Available Amount", font=("Times New Roman", 15), padx=2,bg="#808080",fg="White")

    db1=Button(depwin, text="Deposit", font=("Times New Roman", 15), padx=20,bg="#808080",fg="White",command=add)


    de1=Entry(depwin,width=30)
    de2=Entry(depwin,width=30)





    dl1.place(x=10,y=10)
    de1.place(x=180,y=10)
    dl2.place(x=10,y=50)
    de2.place(x=180,y=60)
    db1.place(x=180,y=250)

    depwin.mainloop()
#    amt=e2.get()



def accountdet():
    #name=input(e1.get())+input(e4.get())
    #e11.insert(END,name)



    w1=Tk()
    w1.configure(bg="Black")
    w1.geometry("800x650")
    h11=Label(w1,text="Account Details",font="Elephant 20 bold", bg="#808080", fg="Black", borderwidth=3, padx=25, pady=10, relief=RAISED)
    l11 = Label(w1, text="Name", font=("Times New Roman", 20), padx=48,bg="#808080",fg="White")
    l44 = Label(w1, text="Mobile No", font=("Times New Roman", 20), padx=9,bg="#808080",fg="White")
    l22 = Label(w1, text="Balance", font=("Times New Roman", 20), padx=35,bg="#808080",fg="White")
    l33 = Label(w1, text="Account Type", font=("Times New Roman", 20), padx=1,bg="#808080",fg="White")
    l55 = Label(w1, text="Branch", font=("Times New Roman", 20), padx=39,bg="#808080",fg="White")
    l66 = Label(w1, text="IFSC CODE", font=("Times New Roman", 20), padx=10,bg="#808080",fg="White")
    l77 = Label(w1, text="Account No", font=("Times New Roman", 20), padx=12,bg="#808080",fg="White")
    lp=Label(w1,text="Pin",font=("Times New Roman",20),padx=60,bg="#808080",fg="White")

    e11 = Entry(w1,width=30)
    e22 = Entry(w1,width=30)
    e33 = Entry(w1,width=30)
    e44 = Entry(w1,width=30)
    e55 = Entry(w1,width=30)
    e66 = Entry(w1,width=30)
    enn = Entry(w1,width=30)
    ep=Entry(w1,width=30)
#bank details
    b="Main Py Branch" #branch
    e55.insert(0,str(b))#branch
    a="PYBK0001234"#ifsc
    e66.insert(0,str(a))#ifsc
    ac=en.get()#ac no
    enn.insert(0,ac)#ac no
    naf=e1.get()#first name
    nal=e4.get()#second name
    nam=naf+" "+nal
    e11.insert(0,str(nam))#name
    ba=e2.get()#bal
    e22.insert(0,ba)#bal
    mo=e9.get()#mobile
    e44.insert(0,mo)#mobile
    pin=random.randint(1000,9999)
    ep.insert(0,pin)

    b11 = Button(w1, text="Exit", font=("Times New Roman", 20),padx=88, bg="#808080", fg="white",command=sys.exit)
    b22 = Button(w1, text="Deposit Amount", font=("Times New Roman", 20),padx=20, bg="#808080", fg="White",command=deposit)
    b33 = Button(w1, text="Withdraw Amount", font=("Times New Roman", 20),padx=10, bg="#808080", fg="White", command=withdrawl)
    b44 = Button(w1, text="Change Pin", font=("Times New Roman", 20),padx=50, bg="#808080", fg="White")



    h11.place(x=5,y=5)
    h11.pack()


    l11.place(x=10, y=100)
    e11.place(x=180, y=110)
    l22.place(x=10, y=140)
    e22.place(x=180, y=150)
    l33.place(x=10, y=180)
    e33.place(x=180, y=190)
    l44.place(x=400, y=100)
    e44.place(x=550, y=110)
    l55.place(x=10, y=220)
    e55.place(x=180, y=230)
    l66.place(x=10, y=260)
    e66.place(x=180, y=270)
    l77.place(x=10, y=300)
    enn.place(x=180, y=310)
    b11.place(x=500, y=400)
    b22.place(x=500, y=460)
    b33.place(x=50,y=400)
    b44.place(x=50,y=460)
    lp.place(x=10,y=340)
    ep.place(x=180,y=350)
    w1.mainloop()


window=Tk()
window.configure(bg="#FF82AB")
window.geometry("850x700")

h1=Label(window,text="Py Bank",font="Elephant 30 bold", bg="black", fg="white", borderwidth=10, padx=25, pady=10, relief=RAISED)
l1=Label(window,text="First Name",font=("Times New Roman",20), padx=20,bg="#191970",fg="White")
l4=Label(window,text="Last Name",font=("Times New Roman",20),padx=12,bg="#191970",fg="White")
l2=Label(window,text="Mother Name",font=("Times New Roman",20),padx=9,bg="#191970",fg="White")
l3=Label(window,text="Father Name",font=("Times New Roman",20),padx=9,bg="#191970",fg="White")
l5=Label(window,text="First Deposite",font=("Times New Roman",20),padx=3,bg="#191970",fg="White")
l6=Label(window,text="Aadhaar Id",font=("Times New Roman",20),padx=18,bg="#191970",fg="White")
l7=Label(window,text="Account No",font=("Times New Roman",20),padx=12,bg="#191970",fg="White")
l8=Label(window,text="Address",font=("Times New Roman",20),padx=34,bg="#191970",fg="White")
l9=Label(window,text="Mobile",font=("Times New Roman",20),padx=38,bg="#191970",fg="White")
l10=Label(window,text="Gender",font=("Times New Roman",20),padx=38,bg="#191970",fg="White")


option = StringVar()
R1 = Radiobutton(window, text="MALE", value="male",font=("Times New Roman",12), var=option,padx=20,bg="Black",fg="#FF82AB")
R2 = Radiobutton(window, text="FEMALE", value="female",font=("Times New Roman",12), var=option,padx=10,bg="Black",fg="#FF82AB")
R1.pack()
R2.pack()

#option.trace('w', print_var)


e1=Entry(width=30)
e2=Entry(width=30)
e3=Entry(width=30)
e4=Entry(width=30)
e5=Entry(width=30)
e6=Entry(width=30)
#e7=Entry(width=30)
e8=Entry(width=91)
e9=Entry(width=30)
en=Entry(width=30)



b1=Button(window, text="Submit", font=("Times New Roman",15),padx=45,bg="Black",fg="#FF82AB", command=submit)
b2=Button(window,text="Account Details",font=("Times New Roman",15),padx=15,bg="Black",fg="#FF82AB",command=accountdet)

h1.pack()
l1.place(x=10,y=100)
e1.place(x=180,y=110)
l2.place(x=10,y=140)
e2.place(x=180,y=150)
l3.place(x=10,y=180)
e3.place(x=180,y=190)
l4.place(x=400,y=100)
e4.place(x=550,y=110)
l5.place(x=10,y=220)
e5.place(x=180,y=230)
l6.place(x=10,y=260)
e6.place(x=180,y=270)
l7.place(x=10,y=300)
en.place(x=180,y=310)
b1.place(x=250,y=500)
b2.place(x=420,y=500)
l8.place(x=10,y=340)
e8.place(x=180,y=350)
l9.place(x=10,y=380)
e9.place(x=180,y=390)
l10.place(x=10,y=420)
R1.place(x=180,y=425)
R2.place(x=300,y=425)

window.mainloop()