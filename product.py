from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle



# Tkinter GUI code for customer page:
class product_details:
    def add_data(self):
            if(self.p_id.get()=="" or self.p_name.get()=="" or self.cp.get()=="" or self.quant.get()=="" or self.sp.get()=="" or self.s_id.get()=="" or self.category.get()==""):
                messagebox.showwarning('Error','All field are Mandotory')
            else:
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()
                     p_data=[self.p_id.get(),self.p_name.get(),self.cp.get(),self.quant.get(),self.sp.get(),self.s_id.get(),self.category.get(),0]
                     cur.execute('INSERT INTO PRODUCT VALUES(:1,:2,:3,:4,:5,:6,:7,:8)',p_data)
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while inserting product details:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','Product Data Successfully Added')

    def add_product(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        id_label=Label(self.frame2,text='Product Id:',font=('Times New Roman',20),padx=4,pady=10)
        id_label.grid(row=0,column=0)
        id_entry=ttk.Entry(self.frame2,width=23,textvariable=self.p_id,font=('Times New Roman',20))
        id_entry.delete(0,END)
        id_entry.grid(row=0,column=1)

        name_label=Label(self.frame2,text='Product Name:',font=('Times New Roman',20),padx=4,pady=10)
        name_label.grid(row=1,column=0)
        name_entry=ttk.Entry(self.frame2,width=23,textvariable=self.p_name,font=('Times New Roman',20))
        name_entry.delete(0,END)
        name_entry.grid(row=1,column=1)  

        cp_label=Label(self.frame2,text='Product Cost Price:',font=('Times New Roman',20),padx=4,pady=10)
        cp_label.grid(row=2,column=0)
        cp_entry=ttk.Entry(self.frame2,width=23,textvariable=self.cp,font=('Times New Roman',20))
        cp_entry.delete(0,END)
        cp_entry.grid(row=2,column=1) 

        quantity_label=Label(self.frame2,text='Product Quantity',font=('Times New Roman',20),padx=4,pady=10)
        quantity_label.grid(row=3,column=0)
        quantity_entry=ttk.Entry(self.frame2,width=23,textvariable=self.quant,font=('Times New Roman',20))
        quantity_entry.delete(0,END)
        quantity_entry.grid(row=3,column=1)

        sp_label=Label(self.frame2,text='Product Selling Price:',font=('Times New Roman',20),padx=4,pady=10)
        sp_label.grid(row=4,column=0)
        sp_entry=ttk.Entry(self.frame2,width=23,textvariable=self.sp,font=('Times New Roman',20))
        sp_entry.delete(0,END)
        sp_entry.grid(row=4,column=1)

        s_id_label=Label(self.frame2,text='Supplier Id:',font=('Times New Roman',20),padx=4,pady=10)
        s_id_label.grid(row=5,column=0)
        s_id_entry=ttk.Entry(self.frame2,width=23,textvariable=self.s_id,font=('Times New Roman',20))
        s_id_entry.delete(0,END)
        s_id_entry.grid(row=5,column=1)
        
        category_label=Label(self.frame2,text='Category:',font=('Times New Roman',20),padx=4,pady=10)
        category_label.grid(row=6,column=0)
        category_entry=ttk.Combobox(self.frame2,width=23,textvariable=self.category,font=('Times New Roman',20),state='readonly')
        category_entry["value"]=('Men','Women','Children')
        category_entry.grid(row=6,column=1) 

        submit_button=Button(self.frame2,text='Submit',command=self.add_data,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        submit_button.grid(row=7,column=1)


    def update_data(self):
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()

                     p_data=[self.p_name.get(),self.cp.get(),self.quant.get(),self.sp.get(),self.s_id.get(),self.category.get(),self.p_id.get()]
                     cur.execute('UPDATE PRODUCT SET PRO_NAME=:PRO_NAME,PROD_CP=:PROD_CP,PRO_QUANTITY=:PRO_QUANTITY,PROD_SP=:PROD_SP,SUPP_ID=:SUPP_ID,CATEGORY=:CATEGORY WHERE PRO_ID=:PRO_ID',p_data)
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while updating product details:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','Product Data Successfully Updated')

    def search_product(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        pid_label=Label(self.frame2,text='Enter Product Id:',font=('Times New Roman',20),padx=4,pady=10)
        pid_label.grid(row=0,column=0)
        pid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.p_id,font=('Times New Roman',20))
        pid_entry.delete(0,END)
        pid_entry.grid(row=0,column=1)

        
        

        search_button=Button(self.frame2,text='Search',command=self.check_product,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        search_button.grid(row=0,column=2)


    def update_product(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT PRO_NAME,PROD_CP,PRO_QUANTITY,PROD_SP,SUPP_ID,CATEGORY FROM PRODUCT WHERE PRO_ID=:PRO_ID',[self.p_id.get()])
        row1=cur.fetchall()

    
        for record in row1:
            self.p_name.set(record[0])
            self.cp.set(record[1])
            self.quant.set(record[2])
            self.sp.set(record[3])
            self.s_id.set(record[4])
            self.category.set(record[5])
        
        
            name_label=Label(self.frame2,text='Product Name',font=('Times New Roman',20),padx=4,pady=8)
            name_label.grid(row=1,column=0)
            name_entry=ttk.Entry(self.frame2,width=23,textvariable=self.p_name,font=('Times New Roman',20))
            name_entry.grid(row=1,column=1)

            cp_label=Label(self.frame2,text='Product Cost Price:',font=('Times New Roman',20),padx=4,pady=8)
            cp_label.grid(row=2,column=0)
            cp_entry=ttk.Entry(self.frame2,width=23,textvariable=self.cp,font=('Times New Roman',20))
            cp_entry.grid(row=2,column=1)  

            quantity_label=Label(self.frame2,text='Product Quantity:',font=('Times New Roman',20),padx=4,pady=8)
            quantity_label.grid(row=3,column=0)
            quantity_entry=ttk.Entry(self.frame2,width=23,textvariable=self.quant,font=('Times New Roman',20))
            quantity_entry.grid(row=3,column=1) 

            sp_label=Label(self.frame2,text='Product Selling Price:',font=('Times New Roman',20),padx=4,pady=8)
            sp_label.grid(row=4,column=0)
            sp_entry=ttk.Entry(self.frame2,width=23,textvariable=self.sp,font=('Times New Roman',20))
            sp_entry.grid(row=4,column=1)

            s_id_label=Label(self.frame2,text='Supplier Id:',font=('Times New Roman',20),padx=4,pady=8)
            s_id_label.grid(row=5,column=0)
            s_id_entry=ttk.Entry(self.frame2,width=23,textvariable=self.s_id,font=('Times New Roman',20))
            s_id_entry.grid(row=5,column=1)

            category_label=Label(self.frame2,text='Category:',font=('Times New Roman',20),padx=4,pady=8)
            category_label.grid(row=6,column=0)
            category_entry=ttk.Combobox(self.frame2,width=23,textvariable=self.category,font=('Times New Roman',20),state='readonly')
            category_entry["value"]=('Men','Women','Children')
            category_entry.grid(row=6,column=1)


        update_button=Button(self.frame2,text='Update',command=self.update_data,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        update_button.grid(row=7,column=2)

    def check_product(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT PRO_ID FROM PRODUCT')
            row=cur.fetchall()
            for record in row:
                  if(self.p_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.update_product()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()

        
    def delete_data(self):
        try:
            conn=cx_Oracle.connect('c##project/1234@localhost')
            cur=conn.cursor()
            cur.execute('DELETE FROM PRODUCT WHERE PRO_ID=:PRO_ID',[self.p_id.get()])
        except Exception as err:
            messagebox.showerror('Warning',f'Error while deleting product details:{str(err)}')
        else:
            conn.commit()
            conn.close()
            messagebox.showinfo('Successful','Product Data Successfully Deleted')    

    def delete_product(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        pid_label=Label(self.frame2,text='Enter Product Id:',font=('Times New Roman',20),padx=4,pady=10)
        pid_label.grid(row=0,column=0)
        pid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.p_id,font=('Times New Roman',20))
        pid_entry.delete(0,END)
        pid_entry.grid(row=0,column=1)

        
        

        delete_button=Button(self.frame2,text='Delete',command=self.check_delete,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        delete_button.grid(row=0,column=2)

    def check_delete(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT PRO_ID FROM PRODUCT')
            row=cur.fetchall()
            for record in row:
                  if(self.p_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.delete_data()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()

    def product_details(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        scroll_x=ttk.Scrollbar(self.frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.frame2,orient=VERTICAL)

        self.Prod_Details_Table=ttk.Treeview(self.frame2,column=("pid","pname","cp","quant","sp","sid","category","totalsold"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Prod_Details_Table.xview)
        scroll_y.config(command=self.Prod_Details_Table.yview)

        self.Prod_Details_Table.heading("pid",text="Product Id")
        self.Prod_Details_Table.heading("pname",text="Product Name")
        self.Prod_Details_Table.heading("cp",text="Product Cost Price")
        self.Prod_Details_Table.heading("quant",text="Product Quantity")
        self.Prod_Details_Table.heading("sp",text="Product Selling Price")
        self.Prod_Details_Table.heading("sid",text="Supplier Id")
        self.Prod_Details_Table.heading("category",text="Category")
        self.Prod_Details_Table.heading("totalsold",text="Total Sold")
        
        

        self.Prod_Details_Table["show"]="headings"
        self.Prod_Details_Table.column("pid",width=150)
        self.Prod_Details_Table.column("pname",width=150)
        self.Prod_Details_Table.column("cp",width=150)
        self.Prod_Details_Table.column("quant",width=150)
        self.Prod_Details_Table.column("sp",width=150)
        self.Prod_Details_Table.column("sid",width=100)
        self.Prod_Details_Table.column("category",width=150)
        self.Prod_Details_Table.column("totalsold",width=150)
        

        self.Prod_Details_Table.pack(fill=BOTH,expand=1)
        

        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT * FROM PRODUCT')
        row1=cur.fetchall()
        if(len(row1)!=0):
            self.Prod_Details_Table.delete(*self.Prod_Details_Table.get_children())
            for i in (row1):
                self.Prod_Details_Table.insert("",END,value=i)
                conn.commit()
        conn.close()

    def update_stock(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            data=[self.p_id.get(),self.amt.get()]
            cur.callproc('STOCK_INCREMENT',data)
        except Exception as err:
            messagebox.showerror('Warning',f'Error while Stock Increment:{str(err)}')
        else:
            conn.commit()
            conn.close()
            messagebox.showinfo('Successful','Stock Increamented Successfully')

    def stock_increment(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        pid_label=Label(self.frame2,text='Enter Product Id:',font=('Times New Roman',20),padx=4,pady=10)
        pid_label.grid(row=0,column=0)
        pid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.p_id,font=('Times New Roman',20))
        pid_entry.delete(0,END)
        pid_entry.grid(row=0,column=1)

        amount_label=Label(self.frame2,text='Enter No. of New Stock:',font=('Times New Roman',20),padx=4,pady=10)
        amount_label.grid(row=1,column=0)
        amount_entry=ttk.Entry(self.frame2,width=23,textvariable=self.amt,font=('Times New Roman',20))
        amount_entry.delete(0,END)
        amount_entry.grid(row=1,column=1)

        
        

        submit_button=Button(self.frame2,text='Submit',command=self.check_product,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        submit_button.grid(row=2,column=2)

    def check_product(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT PRO_ID FROM PRODUCT')
            row=cur.fetchall()
            for record in row:
                  if(self.p_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.update_stock()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()


    def __init__(self, root=None):
        self.root= root
        self.root.geometry('1350x700+0+0')
        self.root.title("Product Details")

        label1=Label(self.root,text='PRODUCT DETAILS',bg='black',fg='gold',font=('Times New Roman',40,'bold'),bd=4,relief=RIDGE)
        label1.place(x=0,y=0,width=1350)

        frame1=LabelFrame(self.root,text='Menu',font=('arial',15),bd=4,relief=RIDGE)
        frame1.place(x=0,y=70,width=400,height=600)

        add_button=Button(frame1,text='ADD PRODUCT',command=self.add_product,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        add_button.grid(row=0,column=0)

        update_button=Button(frame1,text='UPDATE PRODUCT',command=self.search_product,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        update_button.grid(row=1,column=0)

        delete_button=Button(frame1,text='DELETE PRODUCT',command=self.delete_product,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        delete_button.grid(row=2,column=0)

        displayall_button=Button(frame1,text='DISPLAY ALL PRODUCT',command=self.product_details,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        displayall_button.grid(row=3,column=0)


        mostpaying_button=Button(frame1,text='STOCK INCREAMENT',command=self.stock_increment,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        mostpaying_button.grid(row=4,column=0)

        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)

        self.p_id=StringVar()
        self.p_name=StringVar()
        self.cp=IntVar()
        self.quant=IntVar()
        self.sp=IntVar()
        self.s_id=StringVar()
        self.totalsold=IntVar()
        self.category=StringVar()
        self.amt=IntVar()


        





        


if __name__=='__main__':
    root=Tk()
    obj=product_details(root)
    root.mainloop()