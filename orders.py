from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle

class order_details:
    def update_emp3(self):
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()
                     data=[self.e_id.get(),self.o_id.get()]
                     cur.execute('UPDATE ORDER_DETAILS SET EMP_ID=:EMP_ID WHERE ORDER_ID=:ORDER_ID',data )
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while updating Employee details of order:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','Employee Data Successfully Updated')

    def update_emp(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        oid_label=Label(self.frame2,text='Enter Order Id:',font=('Times New Roman',20),padx=4,pady=10)
        oid_label.grid(row=0,column=0)
        oid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.o_id,font=('Times New Roman',20))
        oid_entry.delete(0,END)
        oid_entry.grid(row=0,column=1)

        
        

        search_button=Button(self.frame2,text='Search',command=self.check_order,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        search_button.grid(row=0,column=2)

    def update_emp2(self):

        eid_label=Label(self.frame2,text='Employee Id:',font=('Times New Roman',20),padx=4,pady=8)
        eid_label.grid(row=1,column=0)
        eid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_id,font=('Times New Roman',20))
        eid_entry.grid(row=1,column=1)

        update_button=Button(self.frame2,text='Update',command=self.update_emp3,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        update_button.grid(row=2,column=2)


    def check_order(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT ORDER_ID FROM ORDERS')
            row=cur.fetchall()
            for record in row:
                  if(self.o_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.update_emp2()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()

    def update_status3(self):
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()
                     data=[self.status.get(),self.o_id.get()]
                     cur.execute('UPDATE ORDER_DETAILS SET STATUS=:STATUS WHERE ORDER_ID=:ORDER_ID',data )
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while updating Status of order:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','Status Successfully Updated')

    def update_status(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        oid_label=Label(self.frame2,text='Enter Order Id:',font=('Times New Roman',20),padx=4,pady=10)
        oid_label.grid(row=0,column=0)
        oid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.o_id,font=('Times New Roman',20))
        oid_entry.delete(0,END)
        oid_entry.grid(row=0,column=1)

        
        

        search_button=Button(self.frame2,text='Search',command=self.check_order2,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        search_button.grid(row=0,column=2)

    def update_status2(self):
            status_label=Label(self.frame2,text='Employee Id:',font=('Times New Roman',20),padx=4,pady=8)
            status_label.grid(row=1,column=0)
            status_entry=ttk.Combobox(self.frame2,width=23,textvariable=self.status,font=('Times New Roman',20),state='readonly')
            status_entry["value"]=('Order Placed','Order Shipped','Order Out for Delivery','Delivered','Order Returned')
            status_entry.grid(row=1,column=1)

            update_button=Button(self.frame2,text='Update',command=self.update_status3,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
            update_button.grid(row=2,column=2)

    

    def check_order2(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT ORDER_ID FROM ORDERS')
            row=cur.fetchall()
            for record in row:
                  if(self.o_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.update_status2()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()


    def order_details(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=590)
        scroll_x=ttk.Scrollbar(self.frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.frame2,orient=VERTICAL)

        self.Order_Details_Table=ttk.Treeview(self.frame2,column=("order_id","cust_id","prod_id","eid","quantity","price","order_date","order_status","delivery_address","payment_id","payment_mode","card_type","card_no","cardholder","card_exp_date","cvv"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Order_Details_Table.xview)
        scroll_y.config(command=self.Order_Details_Table.yview)

        self.Order_Details_Table.heading("order_id",text="Order Id")
        self.Order_Details_Table.heading("cust_id",text="Customer Id")
        self.Order_Details_Table.heading("prod_id",text="Product Id")
        self.Order_Details_Table.heading("eid",text="Employee Id")
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
        self.Order_Details_Table.column("cust_id",width=50)
        self.Order_Details_Table.column("prod_id",width=50)
        self.Order_Details_Table.column("eid",width=50)
        self.Order_Details_Table.column("quantity",width=50)
        self.Order_Details_Table.column("price",width=50)
        self.Order_Details_Table.column("order_date",width=100)
        self.Order_Details_Table.column("order_status",width=100)
        self.Order_Details_Table.column("delivery_address",width=200)
        self.Order_Details_Table.column("payment_id",width=80)
        self.Order_Details_Table.column("payment_mode",width=100)
        self.Order_Details_Table.column("card_type",width=100)
        self.Order_Details_Table.column("card_no",width=150)
        self.Order_Details_Table.column("cardholder",width=150)
        self.Order_Details_Table.column("card_exp_date",width=100)
        self.Order_Details_Table.column("cvv",width=50)
        
        

        self.Order_Details_Table.pack(fill=BOTH,expand=1)
        

        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT ORDERS.ORDER_ID,CUST_ID,PRO_ID,EMP_ID,ORDER_QUANTITY,ORDER_PRICE,ORDER_DATE,STATUS,DELIVERY_ADDRESS,PAYMENT_ID,PAYMENT_MODE,CARD_TYPE,CARD_NO,CARDHOLDER_NAME,CARD_EXP_DATE,CVV FROM ORDERS JOIN ORDER_DETAILS ON ORDERS.ORDER_ID=ORDER_DETAILS.ORDER_ID JOIN PAYMENT ON PAYMENT.ORDER_ID=ORDERS.ORDER_ID')
        row1=cur.fetchall()
        
        if(len(row1)!=0):
            self.Order_Details_Table.delete(*self.Order_Details_Table.get_children())
            for i in (row1):
                self.Order_Details_Table.insert("",END,value=i)
                conn.commit()
        conn.close()



    def __init__(self, root=None):
        self.root= root
        self.root.geometry('1350x700+0+0')
        self.root.title("Supplier Details")

        label1=Label(self.root,text='ORDERS',bg='black',fg='gold',font=('Times New Roman',40,'bold'),bd=4,relief=RIDGE)
        label1.place(x=0,y=0,width=1350)

        frame1=LabelFrame(self.root,text='Menu',font=('arial',15),bd=4,relief=RIDGE)
        frame1.place(x=0,y=70,width=400,height=600)

        add_button=Button(frame1,text='DISPLAY ALL ORDERS',command=self.order_details,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        add_button.grid(row=0,column=0)

        update_button=Button(frame1,text='UPDATE EMPLOYEE ID',command=self.update_emp,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        update_button.grid(row=1,column=0)

        delete_button=Button(frame1,text='UPDATE ORDER\n STATUS',command=self.update_status,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        delete_button.grid(row=2,column=0)

        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)

        self.o_id=StringVar()
        self.e_id=StringVar()
        self.status=StringVar()


        





        


if __name__=='__main__':
    root=Tk()
    obj=order_details(root)
    root.mainloop()