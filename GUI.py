from tkinter import *
from PIL import ImageTk
from PIL import Image

root=Tk()

root.title("Simple Image Viewer Application")
myImg1=ImageTk.PhotoImage(Image.open("C:/Users/user/Pictures/Saved Pictures/ronin.jpg"))
myImg2=ImageTk.PhotoImage(Image.open("C:/Users/user/Pictures/Saved Pictures/Kakashi.jpg"))
myImg3=ImageTk.PhotoImage(Image.open("C:/Users/user/Pictures/Saved Pictures/Levi.jpg"))
myImg4=ImageTk.PhotoImage(Image.open("C:/Users/user/Pictures/Saved Pictures/Haschwalth.jpg"))
myImg5=ImageTk.PhotoImage(Image.open("C:/Users/user/Pictures/Saved Pictures/Uryu.png"))




def forward(Img_num):
    global myLabel
    global b4
    global b5
    myLabel.grid_forget()
    myLabel=Label(image=ImgList[Img_num-1])
    myLabel.grid(row=0,column=0,columnspan=3,padx=2,pady=2)
    if Img_num==5:
        b4=Button(root,text=">>",command=lambda:forward(Img_num+1),state=DISABLED).grid(row=1,column=2)
    else:
        
        b4=Button(root,text=">>",command=lambda:forward(Img_num+1)).grid(row=1,column=2)
    b5=Button(root,text="<<",command=lambda:backward(Img_num-1)).grid(row=1,column=0)
    b6=Button(root,text="Exit",command=root.quit).grid(row=1,column=1)
    
    

def backward(Img_num):
    global myLabel
    global b4
    global b5
    myLabel.grid_forget()
    myLabel=Label(image=ImgList[Img_num-1])
    myLabel.grid(row=0,column=0,columnspan=3,padx=2,pady=2)
    if Img_num==1:
        b5=Button(root,text="<<",command=lambda:backward(Img_num-1),state=DISABLED).grid(row=1,column=0)
    else:
        b5=Button(root,text="<<",command=lambda:backward(Img_num-1)).grid(row=1,column=0)
    b4=Button(root,text=">>",command=lambda:forward(Img_num+1)).grid(row=1,column=2)
    b6=Button(root,text="Exit",command=root.quit).grid(row=1,column=1)


b1=Button(root,text=">>",command=lambda:forward(2)).grid(row=1,column=2)
b2=Button(root,text="<<",command=backward,state=DISABLED).grid(row=1,column=0)
b3=Button(root,text="Exit",command=root.quit).grid(row=1,column=1)

ImgList=[myImg1,myImg2,myImg3,myImg4,myImg5]

myLabel=Label(image=myImg1)
myLabel.grid(row=0,column=0,columnspan=3,padx=2,pady=2)




root.mainloop()
