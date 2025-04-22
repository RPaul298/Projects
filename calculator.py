from tkinter import *
root=Tk()
e1=Entry(root,width=40,borderwidth=5,fg="Blue",bg="White")
e1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)



def myclick(num):
    c1=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(c1)+str(num))

def myAdd():
    global v1
    global m
    m="add"
    v1=e1.get()
    e1.delete(0,END)
    
def myEqual():
    v2=e1.get()
    e1.delete(0,END)
    if m=="add":
        e1.insert(0,int(v1)+int(v2))
    elif m=="sub":
        e1.insert(0,int(v1)-int(v2))
    elif m=="mul":
        e1.insert(0,int(v1)*int(v2))
    elif m=="div":
        e1.insert(0,int(v1)/int(v2))
    
    
def mySub():
    global v1
    global m
    m="sub"
    v1=e1.get()
    e1.delete(0,END)

def myMul():
    global v1
    global m
    m="mul"
    v1=e1.get()
    e1.delete(0,END)

def myDiv():
    global v1
    global m
    m="div"
    v1=e1.get()
    e1.delete(0,END)
    
def myClear():
    global v1
    global math
    v1=0
    e1.delete(0,END)
    

    

myButton1=Button(root,text="1",fg="Black",bg="White",padx=40,pady=20,command=lambda:myclick(1))
myButton2=Button(root,text="2",fg="Black",bg="White",padx=40,pady=20,command=lambda:myclick(2))
myButton3=Button(root,text="3",fg="Black",bg="White",padx=40,pady=20,command=lambda:myclick(3))
myButton4=Button(root,text="4",fg="Black",bg="White",padx=40,pady=20,command=lambda:myclick(4))
myButton5=Button(root,text="5",fg="Black",bg="White",padx=40,pady=20,command=lambda:myclick(5))
myButton6=Button(root,text="6",fg="Black",bg="White",padx=40,pady=20,command=lambda:myclick(6))
myButton7=Button(root,text="7",fg="Black",bg="White",padx=40,pady=20,command=lambda:myclick(7))
myButton8=Button(root,text="8",fg="Black",bg="White",padx=40,pady=20,command=lambda:myclick(8))
myButton9=Button(root,text="9",fg="Black",bg="White",padx=40,pady=20,command=lambda:myclick(9))
myButton15=Button(root,text="0",fg="Black",bg="White",padx=40,pady=20,command=lambda:myclick(0))

myButton10=Button(root,text="+",fg="Black",bg="White",padx=40,pady=20,command=myAdd)
myButton11=Button(root,text="-",fg="Black",bg="White",padx=40,pady=20,command=mySub)
myButton12=Button(root,text="*",fg="Black",bg="White",padx=40,pady=20,command=myMul)
myButton13=Button(root,text="/",fg="Black",bg="White",padx=40,pady=20,command=myDiv)
myButton14=Button(root,text="=",fg="Black",bg="White",padx=40,pady=20,command=myEqual)

myButton16=Button(root,text="Clear",fg="Black",bg="White",padx=120,pady=20,command=myClear)

myButton1.grid(row=1,column=0)
myButton2.grid(row=1,column=1)
myButton3.grid(row=1,column=2)
myButton4.grid(row=2,column=0)
myButton5.grid(row=2,column=1)
myButton6.grid(row=2,column=2)
myButton7.grid(row=3,column=0)
myButton8.grid(row=3,column=1)
myButton9.grid(row=3,column=2)
myButton15.grid(row=4,column=0)
myButton10.grid(row=4,column=1)
myButton11.grid(row=4,column=2)
myButton12.grid(row=5,column=0)
myButton13.grid(row=5,column=1)
myButton14.grid(row=5,column=2)
myButton16.grid(row=6,column=0,columnspan=3)



root.mainloop()




