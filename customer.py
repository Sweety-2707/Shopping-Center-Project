from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle



# Tkinter GUI code for customer page:
class customer_details:
    def add_data(self):
            if(self.c_name.get()=="" or self.c_mob.get()=="" or self.c_email.get()=="" or self.c_gender.get()=="" or self.c_address.get()==""):
                messagebox.showwarning('Error','All field are Mandotory')
            else:
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()
                     c_data=['1',self.c_name.get(),self.c_mob.get(),self.c_email.get(),self.c_gender.get(),0,self.c_address.get()]
                     cur.execute('INSERT INTO CUSTOMER VALUES(:1,:2,:3,:4,:5,:6,:7)',c_data)
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while inserting customer details:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','Customer Data Successfully Added')

    def add_customer(self):
        
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        name_label=Label(self.frame2,text='Customer Name',font=('Times New Roman',20),padx=4,pady=10)
        name_label.grid(row=0,column=0)
        name_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_name,font=('Times New Roman',20))
        name_entry.delete(0,END)
        name_entry.grid(row=0,column=1)

        mob_label=Label(self.frame2,text='Customer Mobile Number:',font=('Times New Roman',20),padx=4,pady=10)
        mob_label.grid(row=1,column=0)
        mob_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_mob,font=('Times New Roman',20))
        mob_entry.delete(0,END)
        mob_entry.grid(row=1,column=1)  

        email_label=Label(self.frame2,text='Customer Email Id:',font=('Times New Roman',20),padx=4,pady=10)
        email_label.grid(row=2,column=0)
        email_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_email,font=('Times New Roman',20))
        email_entry.delete(0,END)
        email_entry.grid(row=2,column=1) 

        gender_label=Label(self.frame2,text='Gender',font=('Times New Roman',20),padx=4,pady=10)
        gender_label.grid(row=3,column=0)
        gender_entry=ttk.Combobox(self.frame2,width=23,textvariable=self.c_gender,font=('Times New Roman',20),state='readonly')
        gender_entry["value"]=('Male','Female','Others')
        gender_entry.grid(row=3,column=1)
        
        address_label=Label(self.frame2,text='Customer Address:',font=('Times New Roman',20),padx=4,pady=10)
        address_label.grid(row=4,column=0)
        address_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_address,font=('Times New Roman',20))
        address_entry.delete(0,END)
        address_entry.grid(row=4,column=1)

        submit_button=Button(self.frame2,text='Submit',command=self.add_data,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        submit_button.grid(row=5,column=1)


    def update_data(self):
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()

                     c_data=[self.c_name.get(),self.c_mob.get(),self.c_email.get(),self.c_gender.get(),self.c_address.get(),self.c_id.get()]
                     cur.execute('UPDATE CUSTOMER SET CUST_NAME=:CUST_NAME,CUST_MOB=:CUST_MOB,CUST_EMAIL=:CUST_EMAIL,GENDER=:GENDER,CUST_ADDRESS=:CUST_ADDRESS WHERE CUST_ID=:CUST_ID',c_data)
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while updating customer details:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','Customer Data Successfully Updated')

    def search_customer(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        cid_label=Label(self.frame2,text='Enter Customer Id:',font=('Times New Roman',20),padx=4,pady=10)
        cid_label.grid(row=0,column=0)
        cid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_id,font=('Times New Roman',20))
        cid_entry.delete(0,END)
        cid_entry.grid(row=0,column=1)

        
        

        search_button=Button(self.frame2,text='Search',command=self.check_customer,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        search_button.grid(row=0,column=2)


    def update_customer(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT * FROM CUSTOMER WHERE CUST_ID=:CUST_ID',[self.c_id.get()])
        row1=cur.fetchall()

    
        for record in row1:
            self.c_name.set(record[1])
            self.c_mob.set(record[2])
            self.c_email.set(record[3])
            self.c_gender.set(record[4])
            self.c_address.set(record[6])
        
        
            name_label=Label(self.frame2,text='Customer Name',font=('Times New Roman',20),padx=4,pady=8)
            name_label.grid(row=1,column=0)
            name_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_name,font=('Times New Roman',20))
            name_entry.grid(row=1,column=1)

            mob_label=Label(self.frame2,text='Customer Mobile Number:',font=('Times New Roman',20),padx=4,pady=8)
            mob_label.grid(row=2,column=0)
            mob_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_mob,font=('Times New Roman',20))
            mob_entry.grid(row=2,column=1)  

            email_label=Label(self.frame2,text='Customer Email Id:',font=('Times New Roman',20),padx=4,pady=8)
            email_label.grid(row=3,column=0)
            email_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_email,font=('Times New Roman',20))
            email_entry.grid(row=3,column=1) 

            gender_label=Label(self.frame2,text='Gender',font=('Times New Roman',20),padx=4,pady=8)
            gender_label.grid(row=4,column=0)
            gender_entry=ttk.Combobox(self.frame2,width=23,textvariable=self.c_gender,font=('Times New Roman',20),state='readonly')
            gender_entry["value"]=('Male','Female','Others')
            gender_entry.grid(row=4,column=1)

            address_label=Label(self.frame2,text='Customer Address:',font=('Times New Roman',20),padx=4,pady=10)
            address_label.grid(row=5,column=0)
            address_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_address,font=('Times New Roman',20))
            address_entry.grid(row=5,column=1)

        
        update_button=Button(self.frame2,text='Update',command=self.update_data,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        update_button.grid(row=6,column=2)

    def check_customer(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT CUST_ID FROM CUSTOMER')
            row=cur.fetchall()
            for record in row:
                  if(self.c_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.update_customer()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()

        
    def delete_data(self):
        try:
            conn=cx_Oracle.connect('c##project/1234@localhost')
            cur=conn.cursor()
            cur.execute('DELETE FROM CUSTOMER WHERE CUST_ID=:CUST_ID',[self.c_id.get()])
        except Exception as err:
            messagebox.showerror('Warning',f'Error while deleting customer details:{str(err)}')
        else:
            conn.commit()
            conn.close()
            messagebox.showinfo('Successful','Customer Data Successfully Deleted')    

    def delete_customer(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        cid_label=Label(self.frame2,text='Enter Customer Id:',font=('Times New Roman',20),padx=4,pady=10)
        cid_label.grid(row=0,column=0)
        cid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.c_id,font=('Times New Roman',20))
        cid_entry.delete(0,END)
        cid_entry.grid(row=0,column=1)

        
        

        delete_button=Button(self.frame2,text='Delete',command=self.check_delete,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        delete_button.grid(row=0,column=2)

    def check_delete(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT CUST_ID FROM CUSTOMER')
            row=cur.fetchall()
            for record in row:
                  if(self.c_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.delete_data()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()

    def customer_details(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        scroll_x=ttk.Scrollbar(self.frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.frame2,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(self.frame2,column=("Cust_Id","Cust_name","Cust_mob","Cust_email",'Cust_gender',"totalspent","Cust_address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Cust_Id",text="Customer Id")
        self.Cust_Details_Table.heading("Cust_name",text="Customer Name")
        self.Cust_Details_Table.heading("Cust_mob",text="Mobile No")
        self.Cust_Details_Table.heading("Cust_email",text="Email ID")
        self.Cust_Details_Table.heading("Cust_gender",text="Gender")
        self.Cust_Details_Table.heading("totalspent",text="Total Spent")
        self.Cust_Details_Table.heading("Cust_address",text="Address")
  

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.column("Cust_Id",width=100)
        self.Cust_Details_Table.column("Cust_name",width=200)
        self.Cust_Details_Table.column("Cust_mob",width=100)
        self.Cust_Details_Table.column("Cust_email",width=200)
        self.Cust_Details_Table.column("Cust_gender",width=100)
        self.Cust_Details_Table.column("totalspent",width=100)
        self.Cust_Details_Table.column("Cust_address",width=300)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        

        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT CUST_ID,CUST_NAME,CUST_MOB,CUST_EMAIL,GENDER,TOTAL_SPENT,CUST_ADDRESS FROM CUSTOMER')
        row1=cur.fetchall()
        if(len(row1)!=0):
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in (row1):
                self.Cust_Details_Table.insert("",END,value=i)
                conn.commit()
        conn.close()



    def __init__(self, root=None):
        self.root= root
        self.root.geometry('1350x700+0+0')
        self.root.title("Customer Details")

        label1=Label(self.root,text='CUSTOMER DETAILS',bg='black',fg='gold',font=('Times New Roman',40,'bold'),bd=4,relief=RIDGE)
        label1.place(x=0,y=0,width=1350)

        frame1=LabelFrame(self.root,text='Menu',font=('arial',15),bd=4,relief=RIDGE)
        frame1.place(x=0,y=70,width=400,height=600)

        add_button=Button(frame1,text='ADD CUSTOMER',command=self.add_customer,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        add_button.grid(row=0,column=0)

        update_button=Button(frame1,text='UPDATE CUSTOMER',command=self.search_customer,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        update_button.grid(row=1,column=0)

        delete_button=Button(frame1,text='DELETE CUSTOMER',command=self.delete_customer,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        delete_button.grid(row=2,column=0)

        displayall_button=Button(frame1,text='DISPLAY ALL CUSTOMER',command=self.customer_details,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        displayall_button.grid(row=3,column=0)


        mostpaying_button=Button(frame1,text='MOST PAYING CUSTOMER',bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        mostpaying_button.grid(row=4,column=0)

        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)

        self.c_name=StringVar()
        self.c_mob=IntVar()
        self.c_email=StringVar()
        self.c_gender=StringVar()
        self.c_id=StringVar()
        self.c_address=StringVar()
        

        





        


if __name__=='__main__':
    root=Tk()
    obj=customer_details(root)
    root.mainloop()