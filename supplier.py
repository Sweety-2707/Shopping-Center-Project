from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle



# Tkinter GUI code for customer page:
class supplier_details:
    def add_data(self):
            if(self.s_id.get()=="" or self.s_name.get()=="" or self.s_mob.get()=="" or self.s_add.get()=="" ):
                messagebox.showwarning('Error','All field are Mandotory')
            else:
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()
                     s_data=[self.s_id.get(),self.s_name.get(),self.s_mob.get(),self.s_add.get()]
                     cur.execute('INSERT INTO SUPPLIER VALUES(:1,:2,:3,:4)',s_data)
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while inserting supplier details:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','Supplier Data Successfully Added')

    def add_supplier(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        id_label=Label(self.frame2,text='Supplier Id:',font=('Times New Roman',20),padx=4,pady=10)
        id_label.grid(row=0,column=0)
        id_entry=ttk.Entry(self.frame2,width=23,textvariable=self.s_id,font=('Times New Roman',20))
        id_entry.delete(0,END)
        id_entry.grid(row=0,column=1)

        name_label=Label(self.frame2,text='Supplier Name:',font=('Times New Roman',20),padx=4,pady=10)
        name_label.grid(row=1,column=0)
        name_entry=ttk.Entry(self.frame2,width=23,textvariable=self.s_name,font=('Times New Roman',20))
        name_entry.delete(0,END)
        name_entry.grid(row=1,column=1)  

        mob_label=Label(self.frame2,text='Supplier Mobile No:',font=('Times New Roman',20),padx=4,pady=10)
        mob_label.grid(row=2,column=0)
        mob_entry=ttk.Entry(self.frame2,width=23,textvariable=self.s_mob,font=('Times New Roman',20))
        mob_entry.delete(0,END)
        mob_entry.grid(row=2,column=1) 

        address_label=Label(self.frame2,text='Supplier Address',font=('Times New Roman',20),padx=4,pady=10)
        address_label.grid(row=3,column=0)
        address_entry=ttk.Entry(self.frame2,width=23,textvariable=self.s_add,font=('Times New Roman',20))
        address_entry.delete(0,END)
        address_entry.grid(row=3,column=1)


        submit_button=Button(self.frame2,text='Submit',command=self.add_data,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        submit_button.grid(row=4,column=1)


    def update_data(self):
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()

                     s_data=[self.s_name.get(),self.s_mob.get(),self.s_add.get(),self.s_id.get()]
                     cur.execute('UPDATE SUPPLIER SET SUP_NAME=:SUP_NAME,SUP_MOBILE=:SUP_MOBILE,SUP_ADDRESS=:SUP_ADDRESS WHERE SUP_ID=:SUP_ID',s_data )
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while updating Supplier details:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','Supplier Data Successfully Updated')

    def search_supplier(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        sid_label=Label(self.frame2,text='Enter Supplier Id:',font=('Times New Roman',20),padx=4,pady=10)
        sid_label.grid(row=0,column=0)
        sid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.s_id,font=('Times New Roman',20))
        sid_entry.delete(0,END)
        sid_entry.grid(row=0,column=1)

        
        

        search_button=Button(self.frame2,text='Search',command=self.check_supplier,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        search_button.grid(row=0,column=2)

    def update_supplier(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT SUP_NAME,SUP_MOBILE,SUP_ADDRESS FROM SUPPLIER WHERE SUP_ID=:SUP_ID',[self.s_id.get()])
        row1=cur.fetchall()

    
        for record in row1:
            self.s_name.set(record[0])
            self.s_mob.set(record[1])
            self.s_add.set(record[2])
        
        
            name_label=Label(self.frame2,text='Supplier Name',font=('Times New Roman',20),padx=4,pady=8)
            name_label.grid(row=1,column=0)
            name_entry=ttk.Entry(self.frame2,width=23,textvariable=self.s_name,font=('Times New Roman',20))
            name_entry.grid(row=1,column=1)

            mobile_label=Label(self.frame2,text='Supplier Mobile No:',font=('Times New Roman',20),padx=4,pady=8)
            mobile_label.grid(row=2,column=0)
            mobile_entry=ttk.Entry(self.frame2,width=23,textvariable=self.s_mob,font=('Times New Roman',20))
            mobile_entry.grid(row=2,column=1)  

            address_label=Label(self.frame2,text='Supplier Address:',font=('Times New Roman',20),padx=4,pady=8)
            address_label.grid(row=3,column=0)
            address_entry=ttk.Entry(self.frame2,width=23,textvariable=self.s_add,font=('Times New Roman',20))
            address_entry.grid(row=3,column=1) 




        update_button=Button(self.frame2,text='Update',command=self.update_data,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        update_button.grid(row=4,column=2)


    def check_supplier(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT SUP_ID FROM SUPPLIER')
            row=cur.fetchall()
            for record in row:
                  if(self.s_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.update_supplier()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()

    

        
    def delete_data(self):
        try:
            conn=cx_Oracle.connect('c##project/1234@localhost')
            cur=conn.cursor()
            cur.execute('DELETE FROM SUPPLIER WHERE SUP_ID=:SUP_ID',[self.s_id.get()])
        except Exception as err:
            messagebox.showerror('Warning',f'Error while deleting supplier details:{str(err)}')
        else:
            conn.commit()
            conn.close()
            messagebox.showinfo('Successful','Supplier Data Successfully Deleted')    

    def delete_supplier(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        sid_label=Label(self.frame2,text='Enter Supplier Id:',font=('Times New Roman',20),padx=4,pady=10)
        sid_label.grid(row=0,column=0)
        sid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.s_id,font=('Times New Roman',20))
        sid_entry.delete(0,END)
        sid_entry.grid(row=0,column=1)

        
        

        delete_button=Button(self.frame2,text='Delete',command=self.check_delete,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        delete_button.grid(row=0,column=2)

    def check_delete(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT SUP_ID FROM SUPPLIER')
            row=cur.fetchall()
            for record in row:
                  if(self.s_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.delete_data()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()

    def supplier_details(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        scroll_x=ttk.Scrollbar(self.frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.frame2,orient=VERTICAL)

        self.Supplier_Details_Table=ttk.Treeview(self.frame2,column=("sid","sname","smob","sadd"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Supplier_Details_Table.xview)
        scroll_y.config(command=self.Supplier_Details_Table.yview)

        self.Supplier_Details_Table.heading("sid",text="Supplier Id")
        self.Supplier_Details_Table.heading("sname",text="Supplier Name")
        self.Supplier_Details_Table.heading("smob",text="Supplier Mobile No")
        self.Supplier_Details_Table.heading("sadd",text="Supplier Address")
        

        self.Supplier_Details_Table["show"]="headings"
        self.Supplier_Details_Table.column("sid",width=150)
        self.Supplier_Details_Table.column("sname",width=150)
        self.Supplier_Details_Table.column("smob",width=150)
        self.Supplier_Details_Table.column("sadd",width=150)
        

        self.Supplier_Details_Table.pack(fill=BOTH,expand=1)
        

        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT * FROM SUPPLIER')
        row1=cur.fetchall()
        if(len(row1)!=0):
            self.Supplier_Details_Table.delete(*self.Supplier_Details_Table.get_children())
            for i in (row1):
                self.Supplier_Details_Table.insert("",END,value=i)
                conn.commit()
        conn.close()



    def __init__(self, root=None):
        self.root= root
        self.root.geometry('1350x700+0+0')
        self.root.title("Supplier Details")

        label1=Label(self.root,text='SUPPLIER DETAILS',bg='black',fg='gold',font=('Times New Roman',40,'bold'),bd=4,relief=RIDGE)
        label1.place(x=0,y=0,width=1350)

        frame1=LabelFrame(self.root,text='Menu',font=('arial',15),bd=4,relief=RIDGE)
        frame1.place(x=0,y=70,width=400,height=600)

        add_button=Button(frame1,text='ADD SUPPLIER',command=self.add_supplier,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        add_button.grid(row=0,column=0)

        update_button=Button(frame1,text='UPDATE SUPPLIER',command=self.search_supplier,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        update_button.grid(row=1,column=0)

        delete_button=Button(frame1,text='DELETE SUPPLIER',command=self.delete_supplier,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        delete_button.grid(row=2,column=0)

        displayall_button=Button(frame1,text='DISPLAY ALL SUPPLIER',command=self.supplier_details,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        displayall_button.grid(row=3,column=0)

        



        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)

        self.s_id=StringVar()
        self.s_name=StringVar()
        self.s_mob=IntVar()
        self.s_add=StringVar()


        





        


if __name__=='__main__':
    root=Tk()
    obj=supplier_details(root)
    root.mainloop()