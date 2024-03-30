from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle



# Tkinter GUI code for employee page:
class emp_details:
    def add_data(self):
            if(self.e_id.get()=="" or self.e_name.get()=="" or self.e_mob.get()=="" or self.e_add.get()==""or self.e_position.get()=="" or self.e_sal.get()=="" ):
                messagebox.showwarning('Error','All field are Mandotory')
            else:
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()
                     e_data=[self.e_id.get(),self.e_name.get(),self.e_mob.get(),self.e_add.get(),self.e_position.get(),self.e_sal.get()]
                     cur.execute('INSERT INTO EMP VALUES(:1,:2,:3,:4,:5,:6)',e_data)
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while inserting employee details:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','Employee Data Successfully Added')

    def add_employee(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        id_label=Label(self.frame2,text='Employee Id:',font=('Times New Roman',20),padx=4,pady=10)
        id_label.grid(row=0,column=0)
        id_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_id,font=('Times New Roman',20))
        id_entry.delete(0,END)
        id_entry.grid(row=0,column=1)

        name_label=Label(self.frame2,text='Employee Name:',font=('Times New Roman',20),padx=4,pady=10)
        name_label.grid(row=1,column=0)
        name_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_name,font=('Times New Roman',20))
        name_entry.delete(0,END)
        name_entry.grid(row=1,column=1)  

        mob_label=Label(self.frame2,text='Employee Mobile No:',font=('Times New Roman',20),padx=4,pady=10)
        mob_label.grid(row=2,column=0)
        mob_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_mob,font=('Times New Roman',20))
        mob_entry.delete(0,END)
        mob_entry.grid(row=2,column=1) 

        address_label=Label(self.frame2,text='Employee Address:',font=('Times New Roman',20),padx=4,pady=10)
        address_label.grid(row=3,column=0)
        address_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_add,font=('Times New Roman',20))
        address_entry.delete(0,END)
        address_entry.grid(row=3,column=1)

        position_label=Label(self.frame2,text='Employee Position:',font=('Times New Roman',20),padx=4,pady=10)
        position_label.grid(row=4,column=0)
        position_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_position,font=('Times New Roman',20))
        position_entry.delete(0,END)
        position_entry.grid(row=4,column=1)

        sal_label=Label(self.frame2,text='Employee Salary:',font=('Times New Roman',20),padx=4,pady=10)
        sal_label.grid(row=5,column=0)
        sal_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_sal,font=('Times New Roman',20))
        sal_entry.delete(0,END)
        sal_entry.grid(row=5,column=1)


        submit_button=Button(self.frame2,text='Submit',command=self.add_data,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        submit_button.grid(row=6,column=1)


    def update_data(self):
                try:
                     conn=cx_Oracle.connect('c##project/1234@localhost')
                     cur=conn.cursor()

                     e_data=[self.e_name.get(),self.e_mob.get(),self.e_add.get(),self.e_position.get(),self.e_sal.get(),self.e_id.get()]
                     cur.execute('UPDATE EMP SET EMP_NAME=:EMP_NAME,EMP_MOB=:EMP_MOB,EMP_ADDRESS=:EMP_ADDRESS,POSITION=:POSITION,SAL=:SAL WHERE EMP_ID=:EMP_ID',e_data )
                except Exception as err:
                     messagebox.showerror('Warning',f'Error while updating Employee details:{str(err)}')
                else:
                     conn.commit()
                     conn.close()
                     messagebox.showinfo('Successful','Employee Data Successfully Updated')

    def search_employee(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        eid_label=Label(self.frame2,text='Enter Employee Id:',font=('Times New Roman',20),padx=4,pady=10)
        eid_label.grid(row=0,column=0)
        eid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_id,font=('Times New Roman',20))
        eid_entry.delete(0,END)
        eid_entry.grid(row=0,column=1)

        
        

        search_button=Button(self.frame2,text='Search',command=self.check_employee,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        search_button.grid(row=0,column=2)

    def update_employee(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT EMP_NAME,EMP_MOB,EMP_ADDRESS,POSITION,SAL FROM EMP WHERE EMP_ID=:EMP_ID',[self.e_id.get()])
        row1=cur.fetchall()

    
        for record in row1:
            self.e_name.set(record[0])
            self.e_mob.set(record[1])
            self.e_add.set(record[2])
            self.e_position.set(record[3])
            self.e_sal.set(record[4])
        
        
            name_label=Label(self.frame2,text='Employee Name',font=('Times New Roman',20),padx=4,pady=8)
            name_label.grid(row=1,column=0)
            name_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_name,font=('Times New Roman',20))
            name_entry.grid(row=1,column=1)

            mobile_label=Label(self.frame2,text='Employee Mobile No:',font=('Times New Roman',20),padx=4,pady=8)
            mobile_label.grid(row=2,column=0)
            mobile_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_mob,font=('Times New Roman',20))
            mobile_entry.grid(row=2,column=1)  

            address_label=Label(self.frame2,text='Employee Address:',font=('Times New Roman',20),padx=4,pady=8)
            address_label.grid(row=3,column=0)
            address_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_add,font=('Times New Roman',20))
            address_entry.grid(row=3,column=1) 

            position_label=Label(self.frame2,text='Employee Position:',font=('Times New Roman',20),padx=4,pady=8)
            position_label.grid(row=4,column=0)
            position_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_position,font=('Times New Roman',20))
            position_entry.grid(row=4,column=1) 

            sal_label=Label(self.frame2,text='Employee Salary:',font=('Times New Roman',20),padx=4,pady=8)
            sal_label.grid(row=5,column=0)
            sal_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_sal,font=('Times New Roman',20))
            sal_entry.grid(row=5,column=1) 




        update_button=Button(self.frame2,text='Update',command=self.update_data,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        update_button.grid(row=6,column=2)


    def check_employee(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT EMP_ID FROM EMP')
            row=cur.fetchall()
            for record in row:
                  if(self.e_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.update_employee()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()

    

        
    def delete_data(self):
        try:
            conn=cx_Oracle.connect('c##project/1234@localhost')
            cur=conn.cursor()
            cur.execute('DELETE FROM EMP WHERE EMP_ID=:EMP_ID',[self.e_id.get()])
        except Exception as err:
            messagebox.showerror('Warning',f'Error while deleting Employee details:{str(err)}')
        else:
            conn.commit()
            conn.close()
            messagebox.showinfo('Successful','Employee Data Successfully Deleted')    

    def delete_employee(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        eid_label=Label(self.frame2,text='Enter Employee Id:',font=('Times New Roman',20),padx=4,pady=10)
        eid_label.grid(row=0,column=0)
        eid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_id,font=('Times New Roman',20))
        eid_entry.delete(0,END)
        eid_entry.grid(row=0,column=1)

        
        

        delete_button=Button(self.frame2,text='Delete',command=self.check_delete,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        delete_button.grid(row=0,column=2)

    def check_delete(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT EMP_ID FROM EMP')
            row=cur.fetchall()
            for record in row:
                  if(self.e_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.delete_data()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()

    def employee_details(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        scroll_x=ttk.Scrollbar(self.frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.frame2,orient=VERTICAL)

        self.Employee_Details_Table=ttk.Treeview(self.frame2,column=("eid","ename","emob","eadd","position","sal"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Employee_Details_Table.xview)
        scroll_y.config(command=self.Employee_Details_Table.yview)

        self.Employee_Details_Table.heading("eid",text="Employee Id")
        self.Employee_Details_Table.heading("ename",text="Employee Name")
        self.Employee_Details_Table.heading("emob",text="Employee Mobile No")
        self.Employee_Details_Table.heading("eadd",text="Employee Address")
        self.Employee_Details_Table.heading("position",text="Employee Position")
        self.Employee_Details_Table.heading("sal",text="Employee Salary")
        

        self.Employee_Details_Table["show"]="headings"
        self.Employee_Details_Table.column("eid",width=150)
        self.Employee_Details_Table.column("ename",width=150)
        self.Employee_Details_Table.column("emob",width=150)
        self.Employee_Details_Table.column("eadd",width=150)
        self.Employee_Details_Table.column("position",width=150)
        self.Employee_Details_Table.column("sal",width=150)
        

        self.Employee_Details_Table.pack(fill=BOTH,expand=1)
        

        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT * FROM EMP')
        row1=cur.fetchall()
        if(len(row1)!=0):
            self.Employee_Details_Table.delete(*self.Employee_Details_Table.get_children())
            for i in (row1):
                self.Employee_Details_Table.insert("",END,value=i)
                conn.commit()
        conn.close()

    def update_salary(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            data=[self.e_id.get(),self.amt.get()]
            cur.callproc('empsalaryincr',data)
        except Exception as err:
            messagebox.showerror('Warning',f'Error while increasing Employee salary:{str(err)}')
        else:
            conn.commit()
            conn.close()
            messagebox.showinfo('Successful','Employee salary Increased Successfully')

    def salary_increment(self):
        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)
        

        eid_label=Label(self.frame2,text='Enter Employee Id:',font=('Times New Roman',20),padx=4,pady=10)
        eid_label.grid(row=0,column=0)
        eid_entry=ttk.Entry(self.frame2,width=23,textvariable=self.e_id,font=('Times New Roman',20))
        eid_entry.delete(0,END)
        eid_entry.grid(row=0,column=1)

        amount_label=Label(self.frame2,text='Enter Salary Increased by:',font=('Times New Roman',20),padx=4,pady=10)
        amount_label.grid(row=1,column=0)
        amount_entry=ttk.Entry(self.frame2,width=23,textvariable=self.amt,font=('Times New Roman',20))
        amount_entry.delete(0,END)
        amount_entry.grid(row=1,column=1)

        
        

        submit_button=Button(self.frame2,text='Submit',command=self.check_emp,bg='black',fg='gold',font=('Times New Roman',20,'bold'),bd=4,relief=RIDGE,width=10)
        submit_button.grid(row=2,column=2)

    def check_emp(self):
        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        try:
            count=0
            cur.execute('SELECT EMP_ID FROM EMP')
            row=cur.fetchall()
            for record in row:
                  if(self.e_id.get()==record[0]):
                       count=count+1
            if(count>0):
                 self.update_salary()
            else:
             messagebox.showerror('Warning','No Data Found')
                  
        finally:
            conn.commit()
            conn.close()



    def __init__(self, root=None):
        self.root= root
        self.root.geometry('1350x700+0+0')
        self.root.title("Employee Details")

        label1=Label(self.root,text='EMPLOYEE DETAILS',bg='black',fg='gold',font=('Times New Roman',40,'bold'),bd=4,relief=RIDGE)
        label1.place(x=0,y=0,width=1350)

        frame1=LabelFrame(self.root,text='Menu',font=('arial',15),bd=4,relief=RIDGE)
        frame1.place(x=0,y=70,width=400,height=600)

        add_button=Button(frame1,text='ADD EMPLOYEE',command=self.add_employee,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        add_button.grid(row=0,column=0)

        update_button=Button(frame1,text='UPDATE EMPLOYEE',command=self.search_employee,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        update_button.grid(row=1,column=0)

        delete_button=Button(frame1,text='DELETE EMPLOYEE',command=self.delete_employee,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        delete_button.grid(row=2,column=0)

        displayall_button=Button(frame1,text='DISPLAY ALL EMPLOYEE',command=self.employee_details,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        displayall_button.grid(row=3,column=0)

        
        sal_incr_button=Button(frame1,text='INCREASE SALARY',command=self.salary_increment,bg='black',fg='gold',width=22,font=('arial',20,'bold'),bd=4,relief=RIDGE)
        sal_incr_button.grid(row=4,column=0)



        self.frame2=Frame(self.root,bd=4,relief=RIDGE)
        self.frame2.place(x=410,y=70,width=930,height=600)

        self.e_id=StringVar()
        self.e_name=StringVar()
        self.e_mob=IntVar()
        self.e_add=StringVar()
        self.e_position=StringVar()
        self.e_sal=IntVar()
        self.amt=IntVar()


        





        


if __name__=='__main__':
    root=Tk()
    obj=emp_details(root)
    root.mainloop()