from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle

class feedback_details:
    def __init__(self, root=None):
        self.root= root
        self.root.geometry('1350x700+0+0')
        self.root.title("Feedback Details")

        label1=Label(self.root,text='FEEDBACKS',bg='black',fg='gold',font=('Times New Roman',40,'bold'),bd=4,relief=RIDGE)
        label1.place(x=0,y=0,width=1350)

        self.frame1=Frame(self.root,bd=4,relief=RIDGE)
        self.frame1.place(x=0,y=70,width=1350,height=630)
        scroll_x=ttk.Scrollbar(self.frame1,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.frame1,orient=VERTICAL)

        self.feedback_Details_Table=ttk.Treeview(self.frame1,column=("order_id","cust_id","pro_id","rating","comment"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.feedback_Details_Table.xview)
        scroll_y.config(command=self.feedback_Details_Table.yview)

        self.feedback_Details_Table.heading("order_id",text="Order Id")
        self.feedback_Details_Table.heading("cust_id",text="Customer Id")
        self.feedback_Details_Table.heading("pro_id",text="Product Id")
        self.feedback_Details_Table.heading("rating",text="Rating")
        self.feedback_Details_Table.heading("comment",text="Comment")

        self.feedback_Details_Table["show"]="headings"
        self.feedback_Details_Table.column("order_id",width=100)
        self.feedback_Details_Table.column("cust_id",width=100)
        self.feedback_Details_Table.column("pro_id",width=100)
        self.feedback_Details_Table.column("rating",width=100)
        self.feedback_Details_Table.column("comment",width=400)
        

        self.feedback_Details_Table.pack(fill=BOTH,expand=1)
        

        conn=cx_Oracle.connect('c##project/1234@localhost')
        cur=conn.cursor()
        cur.execute('SELECT FEEDBACK.ORDER_ID,CUST_ID,PRO_ID,RATING,FEEDBACK_COMMENT FROM FEEDBACK JOIN ORDERS ON FEEDBACK.ORDER_ID=ORDERS.ORDER_ID')
        row1=cur.fetchall()
        
        if(len(row1)!=0):
            self.feedback_Details_Table.delete(*self.feedback_Details_Table.get_children())
            for i in (row1):
                self.feedback_Details_Table.insert("",END,value=i)
                conn.commit()
        conn.close()

if __name__=='__main__':
    root=Tk()
    obj=feedback_details(root)
    root.mainloop()