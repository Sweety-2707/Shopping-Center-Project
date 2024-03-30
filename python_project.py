import os
from datetime import date
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from adminpage import adminmainpage
from tkinter import messagebox
from tkinter import ttk
import cx_Oracle

# Tkinter GUI code start:
class welcomeScreen:
    def __init__(self, window=None):
        self.master = window
        window.geometry('1350x700+0+0')

        img2=Image.open(r"trends1.jpg")
        img2=img2.resize((1350,700),Image.LANCZOS)
        self.img2=ImageTk.PhotoImage(img2)
        label3=Label(window,image=self.img2,bd=4,relief=RIDGE)
        label3.place(x=0,y=0,width=1350,height=700)

        window.title("Trends Clothing center")
        window.iconbitmap("favicon (3).ico")
        window.configure(bg='#023047')
        window.configure(cursor="arrow")
 
        self.Canvas1 = tk.Canvas(window, background="white", borderwidth="0", insertbackground="black",
                                 relief="ridge",
                                 selectbackground="blue", selectforeground="white")
        self.Canvas1.place(relx=0.21, rely=0.31, relheight=0.5, relwidth=0.56)
 
        self.Button1 = tk.Button(self.Canvas1, command=self.selectEmployee, activebackground="black",
                                 activeforeground="#000000", background="black", disabledforeground="#a3a3a3",
                                 foreground="gold", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="gold", pady="0",
                                 text='''ADMIN''')
        self.Button1.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Button1.place(relx=0.15, rely=0.583, height=40, width=220)
 
        self.Button2 = tk.Button(self.Canvas1, command=self.selectCustomer, activebackground="black",
                                 activeforeground="gold", background="black", disabledforeground="#a3a3a3",
                                 foreground="gold", borderwidth="1", highlightbackground="gold",
                                 highlightcolor="gold", pady="0",
                                 text='''CUSTOMER''',relief=RIDGE)
        self.Button2.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Button2.place(relx=0.617, rely=0.583, height=40, width=220)
 
        self.Label1 = tk.Label(self.Canvas1, background="white", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 30 -weight bold", foreground="black",
                               text='''Please select your role''')
        self.Label1.place(relx=0.18, rely=0.2, height=55, width=500)
 
    def selectEmployee(self):
        self.master.withdraw()
        adminLogin(Toplevel(self.master))

    def selectCustomer(self):
        self.master.withdraw()
        CustomerLogin(Toplevel(self.master))


class adminLogin:
    def __init__(self, window=None):
        self.master = window
        window.geometry('1350x700+0+0')
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Admin")
        window.configure(background="gold")
 
        global Canvas1
        Canvas1 = tk.Canvas(window, background="#ffffff", relief="ridge",
                            selectbackground="gold")
        Canvas1.place(relx=0.108, rely=0.142, relheight=0.715, relwidth=0.798)
 
        self.Label1 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 30 -weight bold", foreground="#00254a",
                               text="TRENDS SHOPPING CENTRE")
        self.Label1.place(relx=0.03, rely=0.1, height=60, width=550)
        
 
        global Label2
        Label2 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        Label2.place(relx=0.067, rely=0.283, height=300, width=500)
        global _img0
        _img0=Image.open(r"adminLogin1.png")
        _img0=_img0.resize((500,300),Image.LANCZOS)
        _img0=ImageTk.PhotoImage(_img0)
        Label2.configure(image=_img0)
        
        global Canvas2
        Canvas2 = tk.Canvas(Canvas1, background="#ffff00", relief="ridge")
        Canvas2.place(relx=0.6, rely=0.13, relheight=0.8, relwidth=0.350)

        self.Label5 = tk.Label(Canvas2,background="yellow", disabledforeground="#a3a3a3",
                          font="-family {Segoe UI} -size 18 -weight bold", foreground="#00254a",
                          text="ADMIN LOGIN")
        self.Label5.place(relx=0.18, rely=0.12, height=71, width=250)

        self.Entry1 = tk.Entry(Canvas2, background="#ffffff", borderwidth="2", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6",
                               highlightcolor="#004080", insertbackground="black")
        self.Entry1.place(relx=0.25, rely=0.4, height=25, relwidth=0.52)
 
        self.Entry1_1 = tk.Entry(Canvas2, show='*', background="#ffffff", borderwidth="2",
                                 disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000",
                                 highlightbackground="#d9d9d9", highlightcolor="#004080", insertbackground="black",
                                 selectbackground="blue", selectforeground="white")
        self.Entry1_1.place(relx=0.25, rely=0.52, height=25, relwidth=0.52)
 
        self.Label3 = tk.Label(Canvas2, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label3.place(relx=0.1, rely=0.4, height=21, width=34)
        global new_img1
        new_img1=ImageTk.PhotoImage(file="user1.png")
        self.Label3.configure(image=new_img1)
 
        self.Label4 = tk.Label(Canvas2, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label4.place(relx=0.1, rely=0.52, height=21, width=34)
        global new_img2
        new_img2=ImageTk.PhotoImage(file="lock1.png")
        self.Label4.configure(image=new_img2)
 
 
        self.Button = tk.Button(Canvas2, text="Login", borderwidth="0", width=10, background="white",
                                foreground="#00254a",
                                font="-family {Segoe UI} -size 10 -weight bold",
                                command=lambda: self.login(self.Entry1.get(), self.Entry1_1.get()))
        self.Button.place(relx=0.55, rely=0.8)
 
        self.Button_back = tk.Button(Canvas2, text="Back", borderwidth="0", width=10, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold",
                                     command=self.back)
        self.Button_back.place(relx=0.2, rely=0.8)
 
 
    def back(self):
        self.master.withdraw()
        welcomeScreen(Toplevel(self.master))
 
 
    def login(self, admin_id, admin_password):
        id=admin_id
        pas=admin_password
        if id=='admin' and pas=='1234':
            self.master.withdraw()
            adminmainpage(Toplevel(self.master))
        else:
            messagebox.showerror('Warning','No Data Found')
 
 
class CustomerLogin:
    def __init__(self, window=None):
        self.master = window
        window.geometry('1350x700+0+0')
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Customer")
        window.configure(background="#00254a")
 
        global Canvas1
        Canvas1 = tk.Canvas(window, background="#ffffff", insertbackground="black", relief="ridge",
                            selectbackground="blue", selectforeground="white")
        Canvas1.place(relx=0.108, rely=0.142, relheight=0.715, relwidth=0.798)
 
        Label1 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                          font="-family {Segoe UI} -size 30 -weight bold", foreground="#00254a",
                          text="TRENDS SHOPPING CENTRE")
        Label1.place(relx=0.03, rely=0.1, height=60, width=550)
 
        global Label2
        Label2 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        Label2.place(relx=0.067, rely=0.283, height=250, width=450)
        global _img0
        _img0=Image.open(r"shopping2.png")
        _img0=_img0.resize((550,300),Image.LANCZOS)
        _img0=ImageTk.PhotoImage(_img0)
        Label2.configure(image=_img0)
 
        global Canvas2
        Canvas2 = tk.Canvas(Canvas1, background="powderblue", insertbackground="black", relief="ridge",
                            selectbackground="blue", selectforeground="white")
        Canvas2.place(relx=0.6, rely=0.13, relheight=0.8, relwidth=0.350)
        self.Entry1 = tk.Entry(Canvas2, background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6",
                               highlightcolor="#004080", insertbackground="black")
        self.Entry1.place(relx=0.25, rely=0.32, height=25, relwidth=0.52)
 
        self.Entry1_1 = tk.Entry(Canvas2, show='*', background="#e2e2e2", borderwidth="2",
                                 disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000",
                                 highlightbackground="#d9d9d9", highlightcolor="#004080", insertbackground="black",
                                 selectbackground="blue", selectforeground="white")
        self.Entry1_1.place(relx=0.25, rely=0.45, height=25, relwidth=0.52)
 
        Label3 = tk.Label(Canvas2, background="powderblue", disabledforeground="#a3a3a3", foreground="#000000")
        Label3.place(relx=0.15, rely=0.32, height=21, width=34)
 
        global img1
        img1= Image.open(r"user1.png")
        img1= img1.resize((30,18),Image.LANCZOS)
        img1 = ImageTk.PhotoImage(img1)
        Label3.configure(image=img1)
        
        self.Label4 = tk.Label(Canvas2)
        self.Label4.place(relx=0.15, rely=0.45, height=21, width=34)
        global _img2
        _img2=Image.open(r"lock.png")
        _img2=_img2.resize((30,18),Image.LANCZOS)
        _img2=ImageTk.PhotoImage(_img2)
        self.Label4.configure(image=_img2, background="powderblue")
 
        self.Label5 = tk.Label(Canvas2,background="powderblue", disabledforeground="#a3a3a3",
                          font="-family {Segoe UI} -size 18 -weight bold", foreground="#00254a",
                          text="USER LOGIN")
        self.Label5.place(relx=0.18, rely=0.12, height=71, width=250)

        self.Button_forget = tk.Button(Canvas2, text="Forgot Your Password?", borderwidth="0", width=40, background="powderblue",
                                foreground="#00254a",
                                font="-family {Segoe UI} -size 10 -weight bold",
                                command=lambda: self.login(self.Entry1.get(), self.Entry1_1.get()))
        self.Button_forget.place(relx=0.05, rely=0.52)

        self.Button_create = tk.Button(Canvas2, text="Register New User", borderwidth="0", width=40, background="powderblue",
                                foreground="#00254a",
                                font="-family {Segoe UI} -size 10 -weight bold",
                                command=self.create_user)
        self.Button_create.place(relx=0.05, rely=0.62)
        

        self.Button = tk.Button(Canvas2, text="Login", borderwidth="0", width=15, background="#00254a",
                                foreground="#ffffff",
                                font="-family {Segoe UI} -size 10 -weight bold",
                                command=lambda: self.login(self.Entry1.get(), self.Entry1_1.get()))
        self.Button.place(relx=0.5, rely=0.8)
 
        self.Button_back = tk.Button(Canvas2, text="Back", borderwidth="0", width=15, background="#00254a",
                                     foreground="#ffffff",
                                     font="-family {Segoe UI} -size 10 -weight bold",
                                     command=self.back)
        self.Button_back.place(relx=0.15, rely=0.8)
 
        global customer_img
        customer_img = tk.PhotoImage(file="lock1.png")
 
    def back(self):
        self.master.withdraw()
        welcomeScreen(Toplevel(self.master))



    def login(self, user_id, user_password):
        id=user_id
        pas=user_password
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()

        try:
            cur.execute('SELECT USER_ID,PASSWORD,CUST_ID FROM USER_DETAILS')
            row=cur.fetchall()
            for record in row:
                if(id==record[0] and pas==record[1]):
                    global customer_id
                    customer_id=record[2]
                    self.master.withdraw()
                    customermainpage(Toplevel(self.master))
                if(id==record[0] and pas!=record[1]):
                    messagebox.showerror('Warning','Wrong Password')
                if(id!=record[0] and pas!=record[1]):
                    messagebox.showerror('Warning','No User Found')
                  
        finally:
            conn.commit()
            conn.close()
        
    def create_user(self):
        self.master.withdraw()
        RegisterUser(Toplevel(self.master))


class RegisterUser:
    def add_data(self):
        if(self.name.get()=="" or self.mobile.get()=="" or self.email.get()=="" or self.gender.get()=="" or self.uname.get()=="" or self.password.get()==""):
                messagebox.showwarning('Error','All field are Mandotory')
        
        else:
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()
                     c_data=[self.name.get(),self.mobile.get(),self.email.get(),self.gender.get()]
                     cur.execute('INSERT INTO CUSTOMER(CUST_NAME,CUST_MOB,CUST_EMAIL,GENDER) VALUES(:1,:2,:3,:4)',c_data)
                     cur.execute('SELECT MAX(CUST_ID) FROM CUSTOMER')
                     row=cur.fetchall()
                     for record in row:
                        self.id.set(record[0])
                     user=[self.uname.get(),self.password.get(),self.id.get()]
                     cur.execute('INSERT INTO USER_DETAILS VALUES(:1,:2,:3)',user)
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while Registration of New User:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','You have Successfully Registered!')


    def __init__(self, root=None):
        self.window = root
        self.window.geometry('1350x700+0+0')
        self.window.title("New User Registration")
        self.window.configure(background="#00254a")

        self.id=StringVar()
        self.name=StringVar()
        self.mobile=IntVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.uname=StringVar()
        self.password=StringVar()
 
        global Canvas1
        Canvas1 = tk.Canvas(self.window, background="#ffffff", insertbackground="black", relief="ridge",
                            selectbackground="blue", selectforeground="white")
        Canvas1.place(relx=0.108, rely=0.142, relheight=0.715, relwidth=0.798)
 
        Label1 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                          font="-family {Segoe UI} -size 30 -weight bold", foreground="#00254a",
                          text="REGISTER HERE")
        Label1.place(relx=0.4, rely=0.1, height=60, width=550)

        global Label2
        Label2 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        Label2.place(relx=0, rely=0.05, height=500, width=400)
        global _img0
        _img0=Image.open(r"register.png")
        _img0=_img0.resize((400,500),Image.LANCZOS)
        _img0=ImageTk.PhotoImage(_img0)
        Label2.configure(image=_img0)

        global Label3
        Label3 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                          font="-family {Segoe UI} -size 13", foreground="#00254a",
                          text="Name:")
        Label3.place(relx=0.4, rely=0.3, height=60, width=60)
        self.Entry1 = tk.Entry(Canvas1, textvariable=self.name,background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6",
                               highlightcolor="#004080", insertbackground="black")
        self.Entry1.place(relx=0.4, rely=0.4, relheight=0.05, relwidth=0.23)

        global Label4
        Label4 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                          font="-family {Segoe UI} -size 13", foreground="#00254a",
                          text="Contact No:")
        Label4.place(relx=0.68, rely=0.3, height=60, width=100)
        self.Entry2 = tk.Entry(Canvas1, textvariable=self.mobile,background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6",
                               highlightcolor="#004080", insertbackground="black")
        self.Entry2.place(relx=0.68, rely=0.4, relheight=0.05, relwidth=0.23)

        global Label5
        Label5 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                          font="-family {Segoe UI} -size 13", foreground="#00254a",
                          text="Email ID:")
        Label5.place(relx=0.4, rely=0.45, height=60, width=100)
        self.Entry3 = tk.Entry(Canvas1,textvariable=self.email, background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6",
                               highlightcolor="#004080", insertbackground="black")
        self.Entry3.place(relx=0.4, rely=0.55, relheight=0.05, relwidth=0.23)

        global Label6
        Label6 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                          font="-family {Segoe UI} -size 13", foreground="#00254a",
                          text="Gender:")
        Label6.place(relx=0.68, rely=0.45, height=60, width=60)
        self.Entry4=ttk.Combobox(Canvas1,textvariable=self.gender,font=('TkFixedFont'),state='readonly')
        self.Entry4["value"]=('Male','Female','Others')
        self.Entry4.place(relx=0.68, rely=0.55, relheight=0.05, relwidth=0.23)

        global Label7
        Label7 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                          font="-family {Segoe UI} -size 13", foreground="#00254a",
                          text="User Name:")
        Label7.place(relx=0.4, rely=0.60, height=60, width=100)
        self.Entry5 = tk.Entry(Canvas1, textvariable=self.uname,background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6",
                               highlightcolor="#004080", insertbackground="black")
        self.Entry5.place(relx=0.4, rely=0.70, relheight=0.05, relwidth=0.23)

        global Label8
        Label8 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                          font="-family {Segoe UI} -size 13", foreground="#00254a",
                          text="Password:")
        Label8.place(relx=0.68, rely=0.60, height=60, width=100)
        self.Entry6 = tk.Entry(Canvas1,textvariable=self.password, background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6",
                               highlightcolor="#004080", insertbackground="black")
        self.Entry6.place(relx=0.68, rely=0.70, relheight=0.05, relwidth=0.23)

        back_button=Button(Canvas1,text='Back',command=self.back,bg='#00254a',fg='white',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        back_button.place(relx=0.55, rely=0.82, relheight=0.1, relwidth=0.15)

        submit_button=Button(Canvas1,text='Submit',command=self.add_data,bg='#00254a',fg='white',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        submit_button.place(relx=0.75, rely=0.82, relheight=0.1, relwidth=0.15)

    def back(self):
        self.window.withdraw()
        CustomerLogin(Toplevel(self.window))


class customermainpage:
    def product(self):
        self.frame2=Frame(self.frame1,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=0,width=930,height=490)
        scroll_x=ttk.Scrollbar(self.frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.frame2,orient=VERTICAL)

        self.Product_Details_Table=ttk.Treeview(self.frame2,column=("prod_id","prod_name","prod_price","prod_quant","category"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Product_Details_Table.xview)
        scroll_y.config(command=self.Product_Details_Table.yview)

        self.Product_Details_Table.heading("prod_id",text="Product Id")
        self.Product_Details_Table.heading("prod_name",text="Product Name")
        self.Product_Details_Table.heading("prod_price",text="Product Price")
        self.Product_Details_Table.heading("prod_quant",text="Product Quantity")
        self.Product_Details_Table.heading("category",text="Category")
        
  

        self.Product_Details_Table["show"]="headings"
        self.Product_Details_Table.column("prod_id",width=150)
        self.Product_Details_Table.column("prod_name",width=150)
        self.Product_Details_Table.column("prod_price",width=150)
        self.Product_Details_Table.column("prod_quant",width=150)
        self.Product_Details_Table.column("category",width=150)
        

        self.Product_Details_Table.pack(fill=BOTH,expand=1)
        

        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT PRO_ID,PRO_NAME,PROD_SP,PRO_QUANTITY,CATEGORY FROM PRODUCT')
        row1=cur.fetchall()
        if(len(row1)!=0):
            self.Product_Details_Table.delete(*self.Product_Details_Table.get_children())
            for i in (row1):
                self.Product_Details_Table.insert("",END,value=i)
                conn.commit()
        conn.close()

    def product_bill(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT PROD_SP FROM PRODUCT WHERE PRO_ID=:PRO_ID',[self.p_id.get()])
        row1=cur.fetchone()
        eachprice=IntVar()
        for record in row1:
            eachprice.set(record)

        self.price.set(self.quantity.get() * eachprice.get())


        

        cur.close()
        conn.close()

    def proceed_order(self):
        if(self.mode.get()=='Offline'):
                messagebox.showinfo('PaymentInfo','Payment will be received Cash On Delivery')
        if(self.mode.get()=="Online"):
            cardtype_label=Label(self.frame2,text=' Card Type:',font=('Times New Roman',20),padx=4,pady=10)
            cardtype_label.grid(row=4,column=0)
            cardtype_entry=ttk.Combobox(self.frame2,width=23,textvariable=self.cardtype,font=('Times New Roman',20),state='readonly')
            cardtype_entry.delete(0,END)
            cardtype_entry["value"]=('RuPay','Visa','MasterCard')
            cardtype_entry.grid(row=4,column=1)

            cardno_label=Label(self.frame2,text=' Card Number:',font=('Times New Roman',20),padx=4,pady=10)
            cardno_label.grid(row=5,column=0)
            cardno_entry=ttk.Entry(self.frame2,width=23,textvariable=self.cardno,font=('Times New Roman',20))
            cardno_entry.delete(0,END)
            cardno_entry.grid(row=5,column=1)

            cardholder_label=Label(self.frame2,text=' Card Holder Name:',font=('Times New Roman',20),padx=4,pady=10)
            cardholder_label.grid(row=6,column=0)
            cardholder_entry=ttk.Entry(self.frame2,width=23,textvariable=self.cardholder,font=('Times New Roman',20))
            cardholder_entry.delete(0,END)
            cardholder_entry.grid(row=6,column=1)

            

            cardexp_label=Label(self.frame2,text=' Card Exp date:',font=('Times New Roman',20),padx=4,pady=10)
            cardexp_label.grid(row=7,column=0)
            cardexp_entry=ttk.Entry(self.frame2,width=23,textvariable=self.cardexp,font=('Times New Roman',20))
            cardexp_entry.delete(0,END)
            cardexp_entry.grid(row=7,column=1)

            cvv_label=Label(self.frame2,text=' CVV:',font=('Times New Roman',20),padx=4,pady=10)
            cvv_label.grid(row=8,column=0)
            cvv_entry=ttk.Entry(self.frame2,width=23,textvariable=self.cvv,font=('Times New Roman',20))
            cvv_entry.delete(0,END)
            cvv_entry.grid(row=8,column=1)
                

    def place_order(self):
        if(self.p_id.get()=="" or self.quantity.get()=="" or self.price.get()=="" ):
                messagebox.showwarning('Error','All field are Mandotory')
        else:
            try:
                conn=cx_Oracle.connect('c##project/1234@localhost')
                cur=conn.cursor()
                o_data=['1',customer_id,self.p_id.get(),self.quantity.get(),self.price.get()]
                cur.execute('INSERT INTO ORDERS VALUES(:1,:2,:3,:4,:5)',o_data)
                cur.execute('SELECT MAX(ORDER_ID) FROM ORDERS')
                row=cur.fetchall()
                for record in row:
                    self.o_id.set(record[0])
                p_data=['1',self.o_id.get(),self.mode.get(),self.cardtype.get(),self.cardno.get(),self.cardholder.get(),self.cardexp.get(),self.cvv.get()]               
                cur.execute('INSERT INTO PAYMENT VALUES(:1,:2,:3,:4,:5,:6,:7,:8)',p_data)
                
            except Exception as err:
                messagebox.showerror('Warning',f'Error while placing an Order:{str(err)}')
            else:
                conn.commit()
                conn.close()
                messagebox.showinfo('Successful','Order Successfully Placed')
 

    def order(self):
        self.frame2=Frame(self.frame1,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=0,width=930,height=490)

        pid_label=Label(self.frame2,text='Product ID:',font=('Times New Roman',20),padx=4,pady=10)
        pid_label.grid(row=0,column=0)
        pid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.p_id,font=('Times New Roman',20))
        pid_entry.delete(0,END)
        pid_entry.grid(row=0,column=1)

        quantity_label=Label(self.frame2,text='Order Quantity:',font=('Times New Roman',20),padx=4,pady=10)
        quantity_label.grid(row=1,column=0)
        quantity_entry=ttk.Entry(self.frame2,width=23,textvariable=self.quantity,font=('Times New Roman',20))
        quantity_entry.delete(0,END)
        quantity_entry.grid(row=1,column=1)

        price_label=Label(self.frame2,text='Order Price:',font=('Times New Roman',20),padx=4,pady=10)
        price_label.grid(row=2,column=0)
        price_entry=ttk.Entry(self.frame2,width=23,textvariable=self.price,font=('Times New Roman',20))
        price_entry.grid(row=2,column=1)

        paymentmode_label=Label(self.frame2,text='Payment Mode:',font=('Times New Roman',20),padx=4,pady=10)
        paymentmode_label.grid(row=3,column=0)
        paymentmode_entry=ttk.Combobox(self.frame2,width=23,textvariable=self.mode,font=('Times New Roman',20),state='readonly')
        paymentmode_entry["value"]=('Online','Offline')
        paymentmode_entry.grid(row=3,column=1)


        bill_button=Button(self.frame2,text='Bill',command=self.product_bill,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        bill_button.grid(row=1,column=3)

        proceed_button=Button(self.frame2,text='Proceed',command=self.proceed_order,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        proceed_button.grid(row=2,column=3)

        submit_button=Button(self.frame2,text='Place Order',command=self.place_order,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        submit_button.grid(row=3,column=3)

    def order_details(self):
        self.frame2=Frame(self.frame1,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=0,width=930,height=490)
        scroll_x=ttk.Scrollbar(self.frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.frame2,orient=VERTICAL)

        self.Order_Details_Table=ttk.Treeview(self.frame2,column=("order_id","prod_id","quantity","price","order_date","order_status","delivery_address","payment_id","payment_mode","card_type","card_no","cardholder","card_exp_date","cvv"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Order_Details_Table.xview)
        scroll_y.config(command=self.Order_Details_Table.yview)

        self.Order_Details_Table.heading("order_id",text="Order Id")
        self.Order_Details_Table.heading("prod_id",text="Product Id")
        self.Order_Details_Table.heading("quantity",text="Order Quantity")
        self.Order_Details_Table.heading("price",text="Order Price")
        self.Order_Details_Table.heading("order_date",text="Ordre Date")
        self.Order_Details_Table.heading("order_status",text="Ordre Status")
        self.Order_Details_Table.heading("delivery_address",text="Delivery Address")
        self.Order_Details_Table.heading("payment_id",text="Payment Id")
        self.Order_Details_Table.heading("payment_mode",text="Payment Mode")
        self.Order_Details_Table.heading("card_type",text="Card Type")
        self.Order_Details_Table.heading("card_no",text="Card No")
        self.Order_Details_Table.heading("cardholder",text="Card Holder Naame")
        self.Order_Details_Table.heading("card_exp_date",text="Card Expiry date")
        self.Order_Details_Table.heading("cvv",text="CVV")
        
  

        self.Order_Details_Table["show"]="headings"
        self.Order_Details_Table.column("order_id",width=50)
        self.Order_Details_Table.column("prod_id",width=50)
        self.Order_Details_Table.column("quantity",width=50)
        self.Order_Details_Table.column("price",width=50)
        self.Order_Details_Table.column("order_date",width=100)
        self.Order_Details_Table.column("order_status",width=100)
        self.Order_Details_Table.column("delivery_address",width=300)
        self.Order_Details_Table.column("payment_id",width=80)
        self.Order_Details_Table.column("payment_mode",width=100)
        self.Order_Details_Table.column("card_type",width=100)
        self.Order_Details_Table.column("card_no",width=200)
        self.Order_Details_Table.column("cardholder",width=200)
        self.Order_Details_Table.column("card_exp_date",width=100)
        self.Order_Details_Table.column("cvv",width=50)

        self.Order_Details_Table.pack(fill=BOTH,expand=1)
        

        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT ORDERS.ORDER_ID,PRO_ID,ORDER_QUANTITY,ORDER_PRICE,ORDER_DATE,STATUS,DELIVERY_ADDRESS,PAYMENT_ID,PAYMENT_MODE,CARD_TYPE,CARD_NO,CARDHOLDER_NAME,CARD_EXP_DATE,CVV FROM ORDERS JOIN ORDER_DETAILS ON ORDERS.ORDER_ID=ORDER_DETAILS.ORDER_ID JOIN PAYMENT ON PAYMENT.ORDER_ID=ORDERS.ORDER_ID  WHERE CUST_ID=:1',{'1':customer_id})
        row1=cur.fetchall()
        
        if(len(row1)!=0):
            self.Order_Details_Table.delete(*self.Order_Details_Table.get_children())
            for i in (row1):
                self.Order_Details_Table.insert("",END,value=i)
                conn.commit()
        conn.close()

    def product_bill(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT PROD_SP FROM PRODUCT WHERE PRO_ID=:PRO_ID',[self.p_id.get()])
        row1=cur.fetchone()
        eachprice=IntVar()
        for record in row1:
            eachprice.set(record)

        self.price.set(self.quantity.get() * eachprice.get())

        cur.close()
        conn.close()
        

    def feedback(self):
        self.frame2=Frame(self.frame1,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=0,width=930,height=490)

        oid_label=Label(self.frame2,text='Order ID:',font=('Times New Roman',20),padx=4,pady=10)
        oid_label.grid(row=0,column=0)
        oid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.o_id,font=('Times New Roman',20))
        oid_entry.delete(0,END)
        oid_entry.grid(row=0,column=1)

        proceed_button=Button(self.frame2,text='Proceed',command=self.proceed_feedback,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        proceed_button.grid(row=3,column=2)

    def proceed_feedback(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            cur.execute('SELECT ORDER_ID FROM ORDERS WHERE CUST_ID=:1',{'1':customer_id})
            oid=cur.fetchall()
            count=0
            for record in oid:
                if(self.o_id.get()==record[0]):
                    count=count+1
                    rating_label=Label(self.frame2,text='Rating(0-5):',font=('Times New Roman',20),padx=4,pady=10)
                    rating_label.grid(row=1,column=0)
                    rating_entry=ttk.Entry(self.frame2,width=23,textvariable=self.rating,font=('Times New Roman',20))
                    rating_entry.delete(0,END)
                    rating_entry.grid(row=1,column=1)

                    comment_label=Label(self.frame2,text='Comment:',font=('Times New Roman',20),padx=4,pady=10)
                    comment_label.grid(row=2,column=0)
                    comment_entry=ttk.Entry(self.frame2,width=23,textvariable=self.comment,font=('Times New Roman',20))
                    comment_entry.delete(0,END)
                    comment_entry.grid(row=2,column=1)

                    submit_button=Button(self.frame2,text='Submit',command=self.submit_feedback,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
                    submit_button.grid(row=3,column=4)
            if(count==0):
                messagebox.showerror('Warning','You have not placed any Order with given Order Id')
        except Exception as err:
            messagebox.showerror('Warning',f'Error while proceeding feedback:{str(err)}')
                  
        finally:
            conn.commit()
            conn.close()

    def submit_feedback(self):
        try:
            conn=cx_Oracle.connect('c##project/1234@localhost')
            cur=conn.cursor()
            data=[self.o_id.get(),self.rating.get(),self.comment.get()]
            cur.execute('INSERT INTO FEEDBACK VALUES(:1,:2,:3)',data)
            messagebox.showinfo('Successful','Feedback Posted Successfully!')
        except Exception as err:
            messagebox.showerror('Warning',f'Error while submitting feedback:{str(err)}')
        finally:
            conn.commit()
            conn.close()

    def cancel_order(self):
        self.frame2=Frame(self.frame1,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=0,width=930,height=490)

        oid_label=Label(self.frame2,text='Order ID:',font=('Times New Roman',20),padx=4,pady=10)
        oid_label.grid(row=0,column=0)
        oid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.o_id,font=('Times New Roman',20))
        oid_entry.delete(0,END)
        oid_entry.grid(row=0,column=1)

        proceed_button=Button(self.frame2,text='Cancel Order',command=self.proceed_cancel,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        proceed_button.grid(row=0,column=2)

    def proceed_cancel(self):
        try:
            conn=cx_Oracle.connect('c##project/1234@localhost')
            cur=conn.cursor()
            cur.execute('SELECT ORDER_ID FROM ORDERS WHERE CUST_ID=:1',{'1':customer_id})
            oid=cur.fetchall()
            count=0
            for record in oid:
                if(self.o_id.get()==record[0]):
                    count=count+1
                    cur.execute('DELETE FROM ORDERS WHERE ORDER_ID=:ORDER_ID',self.o_id.get())
                    messagebox.showinfo('Successfull','Order Cancelled Successfully!')
            if(count==0):
                messagebox.showerror('Warning','You have not placed any Order with given Order Id')
        except Exception as err:
            messagebox.showerror('Warning',f'Error while Cancelling Order:{str(err)}')
                  
        finally:
            conn.commit()
            conn.close()

    def change_address(self):
        self.frame2=Frame(self.frame1,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=0,width=930,height=490)

        oid_label=Label(self.frame2,text='Order ID:',font=('Times New Roman',20),padx=4,pady=10)
        oid_label.grid(row=0,column=0)
        oid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.o_id,font=('Times New Roman',20))
        oid_entry.delete(0,END)
        oid_entry.grid(row=0,column=1)

        proceed_button=Button(self.frame2,text='Proceed',command=self.proceed_change,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        proceed_button.grid(row=3,column=2)

    def proceed_change(self):
        try:
            conn=cx_Oracle.connect('c##project/1234@localhost')
            cur=conn.cursor()
            cur.execute('SELECT ORDER_ID FROM ORDERS WHERE CUST_ID=:1',{'1':customer_id})
            oid=cur.fetchall()
            count=0
            for record in oid:
                if(self.o_id.get()==record[0]):
                    count=count+1
                    address_label=Label(self.frame2,text='Delivery Address:',font=('Times New Roman',20),padx=4,pady=10)
                    address_label.grid(row=1,column=0)
                    address_entry=ttk.Entry(self.frame2,width=23,textvariable=self.address,font=('Times New Roman',20))
                    address_entry.delete(0,END)
                    address_entry.grid(row=1,column=1)

                    submit_button=Button(self.frame2,text='Submit',command=self.submit_change,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
                    submit_button.grid(row=3,column=3)
            if(count==0):
                messagebox.showerror('Warning','You have not placed any Order with given Order Id')
        except Exception as err:
            messagebox.showerror('Warning',f'Error while proceeding changes of delivery address:{str(err)}')   
        finally:
            conn.commit()
            conn.close()

    def submit_change(self):
        try:
            conn=cx_Oracle.connect('c##project/1234@localhost')
            cur=conn.cursor()
            cur.execute('UPDATE ORDER_DETAILS SET DELIVERY_ADDRESS=:1 WHERE ORDER_ID=:2',{'1':self.address.get(),'2':self.o_id.get()})
            messagebox.showinfo('Successful','You have upadated Delivery Address Successfully')
        except Exception as err:
            messagebox.showerror('Warning',f'Error while updating Delivery Address:{str(err)}')
        finally:
            conn.commit()
            conn.close()

    def update_data(self):
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()

                     c_data=[self.c_name.get(),self.c_mob.get(),self.c_email.get(),self.c_gender.get(),self.c_address.get(),customer_id]
                     cur.execute('UPDATE CUSTOMER SET CUST_NAME=:CUST_NAME,CUST_MOB=:CUST_MOB,CUST_EMAIL=:CUST_EMAIL,GENDER=:GENDER,CUST_ADDRESS=:CUST_ADDRESS WHERE CUST_ID=:CUST_ID',c_data)
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while updating customer details:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','Customer Data Successfully Updated')



    def update_customer(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT * FROM CUSTOMER WHERE CUST_ID=:CUST_ID',[customer_id])
        row1=cur.fetchall()

    
        for record in row1:
            self.c_name.set(record[1])
            self.c_mob.set(record[2])
            self.c_email.set(record[3])
            self.c_gender.set(record[4])
            self.c_address.set(record[6])

            self.frame2=Frame(self.frame1,bd=4,relief=RIDGE)
            self.frame2.place(x=410,y=0,width=930,height=490)
        
        
            name_label=Label(self.frame2,text='Customer Name',font=('Times New Roman',20),padx=4,pady=8)
            name_label.grid(row=0,column=0)
            name_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_name,font=('Times New Roman',20))
            name_entry.grid(row=0,column=1)

            mob_label=Label(self.frame2,text='Customer Mobile Number:',font=('Times New Roman',20),padx=4,pady=8)
            mob_label.grid(row=1,column=0)
            mob_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_mob,font=('Times New Roman',20))
            mob_entry.grid(row=1,column=1)  

            email_label=Label(self.frame2,text='Customer Email Id:',font=('Times New Roman',20),padx=4,pady=8)
            email_label.grid(row=2,column=0)
            email_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_email,font=('Times New Roman',20))
            email_entry.grid(row=2,column=1) 

            gender_label=Label(self.frame2,text='Gender',font=('Times New Roman',20),padx=4,pady=8)
            gender_label.grid(row=3,column=0)
            gender_entry=ttk.Combobox(self.frame2,width=23,textvariable=self.c_gender,font=('Times New Roman',20),state='readonly')
            gender_entry["value"]=('Male','Female','Others')
            gender_entry.grid(row=3,column=1)

            address_label=Label(self.frame2,text='Customer Address:',font=('Times New Roman',20),padx=4,pady=10)
            address_label.grid(row=4,column=0)
            address_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_address,font=('Times New Roman',20))
            address_entry.grid(row=4,column=1)

        
        update_button=Button(self.frame2,text='Update',command=self.update_data,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        update_button.grid(row=6,column=2)

        
            
    def __init__(self, root=None):
        self.p_id=StringVar()
        self.o_id=StringVar()
        self.quantity=IntVar()
        self.price=IntVar()
        self.mode=StringVar()
        self.cardtype=StringVar()
        self.cardno=IntVar()
        self.cardholder=StringVar()
        self.cardexp=StringVar()
        self.cvv=IntVar()
        self.rating=IntVar()
        self.comment=StringVar()
        self.address=StringVar()
        self.c_name=StringVar()
        self.c_mob=IntVar()
        self.c_address=StringVar()
        self.c_gender=StringVar()
        self.c_email=StringVar()


        self.admin= root
        self.admin.geometry('1350x700+0+0')
        self.admin.title("Trends Customer Page")

        label1=Label(self.admin,text='TRENDS SHOPPING CENTRE',bg='black',fg='gold',font=('Times New Roman',40,'bold'),bd=4,relief=RIDGE)
        label1.place(x=0,y=0,width=1350)

        self.frame1=Frame(self.admin,bd=4,relief=RIDGE)
        self.frame1.place(x=0,y=70,width=1350,height=620)

        self.frame2=LabelFrame(self.frame1,text='Menu',font=('arial',15),bd=4,relief=RIDGE)
        self.frame2.place(x=0,y=0,width=400,height=490)

        product_button=Button(self.frame2,text='PRODUCT',command=self.product,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        product_button.grid(row=0,column=0)

        order_button=Button(self.frame2,text='ORDER',command=self.order,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        order_button.grid(row=1,column=0)

        orderhistory_button=Button(self.frame2,text='ORDER DETAILS',command=self.order_details,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        orderhistory_button.grid(row=2,column=0)

        feedback_button=Button(self.frame2,text='FEEDBACK',command=self.feedback,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        feedback_button.grid(row=3,column=0)

        cancelorder_button=Button(self.frame2,text='CANCEL ORDER',command=self.cancel_order,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        cancelorder_button.grid(row=4,column=0)

        changeaddress_button=Button(self.frame2,text='CHANGE DELIVERY \n ADDRESS',command=self.change_address,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        changeaddress_button.grid(row=5,column=0)

        update_button=Button(self.frame2,text='UPDATE PROFILE',command=self.update_customer,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        update_button.grid(row=6,column=0)

        self.frame2=Frame(self.frame1,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=0,width=930,height=490)

        img1=Image.open(r"women1.jpg")
        img1=img1.resize((223,120),Image.LANCZOS)
        self.img1=ImageTk.PhotoImage(img1)
        label2=Label(self.admin,image=self.img1,bd=4,relief=RIDGE)
        label2.place(x=0,y=565,width=223,height=120)

        img2=Image.open(r"men2.jpg")
        img2=img2.resize((223,120),Image.LANCZOS)
        self.img2=ImageTk.PhotoImage(img2)
        label3=Label(self.admin,image=self.img2,bd=4,relief=RIDGE)
        label3.place(x=225,y=565,width=223,height=120)

        img3=Image.open(r"children.jpg")
        img3=img3.resize((223,120),Image.LANCZOS)
        self.img3=ImageTk.PhotoImage(img3)
        label4=Label(self.admin,image=self.img3,bd=4,relief=RIDGE)
        label4.place(x=450,y=565,width=223,height=120)

        img4=Image.open(r"women2.jpg")
        img4=img4.resize((223,120),Image.LANCZOS)
        self.img4=ImageTk.PhotoImage(img4)
        label5=Label(self.admin,image=self.img4,bd=4,relief=RIDGE)
        label5.place(x=675,y=565,width=223,height=120)
        
        img5=Image.open(r"men3.jpg")
        img5=img5.resize((223,120),Image.LANCZOS)
        self.img5=ImageTk.PhotoImage(img5)
        label6=Label(self.admin,image=self.img5,bd=4,relief=RIDGE)
        label6.place(x=900,y=565,width=223,height=120)

        img6=Image.open(r"children2.jpg")
        img6=img6.resize((223,120),Image.LANCZOS)
        self.img6=ImageTk.PhotoImage(img6)
        label7=Label(self.admin,image=self.img6,bd=4,relief=RIDGE)
        label7.place(x=1125,y=565,width=223,height=120)


 
root=tk.Tk()
top = welcomeScreen(root)
root.mainloop()
