from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from customer import customer_details
from product import product_details
from supplier import supplier_details
from orders import order_details
from feedback import feedback_details
from emp import emp_details

# Tkinter GUI code for admin main page:
class adminmainpage:
    def __init__(self, root=None):
        self.admin= root
        self.admin.geometry('1350x700+0+0')
        self.admin.title("Trends Admin Page")

        label1=Label(self.admin,text='TRENDS ADMIN PAGE',bg='black',fg='gold',font=('Times New Roman',40,'bold'),bd=4,relief=RIDGE)
        label1.place(x=0,y=0,width=1350)

        frame1=Frame(self.admin,bd=4,relief=RIDGE)
        frame1.place(x=0,y=60,width=1350,height=500)


        img1=Image.open(r"trends1.jpg")
        img1=img1.resize((900,500),Image.LANCZOS)
        self.img1=ImageTk.PhotoImage(img1)

        label2=Label(frame1,image=self.img1,bd=4,relief=RIDGE)
        label2.place(x=0,y=0,width=900,height=500)

        frame2=Frame(frame1,bd=4,relief=RIDGE)
        frame2.place(x=900,y=0,width=440,height=480)

        cust_button=Button(frame2,text='CUSTOMER',command=self.customer_page,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=26)
        cust_button.grid(row=0,column=0)

        prod_button=Button(frame2,text='PRODUCT',command=self.product_page,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=26)
        prod_button.grid(row=1,column=0)

        order_button=Button(frame2,text='ORDER',command=self.order_page,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=26)
        order_button.grid(row=2,column=0)

        supp_button=Button(frame2,text='SUPPLIER',command=self.supplier_page,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=26)
        supp_button.grid(row=3,column=0)

        emp_button=Button(frame2,text='EMPLOYEE',command=self.emp_page,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=26)
        emp_button.grid(row=4,column=0)

        feedback_button=Button(frame2,text='FEEDBACK',command=self.feedback_page,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=26)
        feedback_button.grid(row=5,column=0)

        payment_button=Button(frame2,text='PAYMENT',bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=26)
        payment_button.grid(row=6,column=0)


        frame3=Frame(self.admin,bd=4,relief=RIDGE)
        frame3.place(x=0,y=550,width=1350,height=150)


        img2=Image.open(r"women1.jpg")
        img2=img2.resize((310,150),Image.LANCZOS)
        self.img2=ImageTk.PhotoImage(img2)

        label3=Label(frame3,image=self.img2,bd=4,relief=RIDGE)
        label3.place(x=0,y=0,width=310,height=150)

        img3=Image.open(r"men.jpg")
        img3=img3.resize((310,150),Image.LANCZOS)
        self.img3=ImageTk.PhotoImage(img3)

        label4=Label(frame3,image=self.img3,bd=4,relief=RIDGE)
        label4.place(x=320,y=0,width=310,height=150)

        img4=Image.open(r"children.jpg")
        img4=img4.resize((310,150),Image.LANCZOS)
        self.img4=ImageTk.PhotoImage(img4)

        label5=Label(frame3,image=self.img4,bd=4,relief=RIDGE)
        label5.place(x=650,y=0,width=310,height=150)

        img5=Image.open(r"children2.jpg")
        img5=img5.resize((310,150),Image.LANCZOS)
        self.img5=ImageTk.PhotoImage(img5)

        label6=Label(frame3,image=self.img5,bd=4,relief=RIDGE)
        label6.place(x=980,y=0,width=310,height=150)
        
    def customer_page(self):
        self.new=Toplevel(self.admin)
        self.cust=customer_details(self.new)

    def product_page(self):
        self.new=Toplevel(self.admin)
        self.prod=product_details(self.new)

    def supplier_page(self):
        self.new=Toplevel(self.admin)
        self.supp=supplier_details(self.new)

    def emp_page(self):
        self.new=Toplevel(self.admin)
        self.emp=emp_details(self.new)

    def order_page(self):
        self.new=Toplevel(self.admin)
        self.order=order_details(self.new)

    def feedback_page(self):
        self.new=Toplevel(self.admin)
        self.fdbk=feedback_details(self.new)

if __name__=='__main__':
    root=Tk()
    obj=adminmainpage(root)
    root.mainloop()