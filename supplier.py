from tkinter import*
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1520x880+230+40')
        self.root.title('Inventory Management System')
        self.root.config(bg="White")
        self.root.focus_force()
        #===================================================
        #All Variables
        #self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_sup_name=StringVar()
        self.var_sup_email=StringVar()
        self.var_sup_contact=StringVar()



        #==Search Frame==#
        SearchFrame=LabelFrame(self.root, text="Search Employee", bg="white", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=450,y=50,width=600,height=70)

        #==Optioms==#
        lbl_search=Label(SearchFrame, text="Search by invoice no.",bg="white", font=("goudy old style",15))
        lbl_search.place(x=10,y=10)

        txt_search=Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style",15),bg="light yellow")
        txt_search.place(x=200,y=10)

        btn_search=Button(SearchFrame, text="Search",command=self.search, font=("goudy old style",15),bg="#3ec141", cursor="hand2").place(x=430,y=10,width=150,height=30)

        #==Title==#
        title=Label(self.root, text="Supplier Details", font=("goudy old style",15), bg = "#5177ca", fg="white").place(x=0,y=150,width=1520)

        #==Content==#
        #==Row 1
        lbl_sup_invoice=Label(self.root, text="Invoice No", font=("goudy old style",15), bg = "white", fg="black").place(x=75,y=250)
        
        txt_empid=Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style",15), bg = "light yellow", fg="black").place(x=175,y=250, width=280)

        #==Row 2
        lbl_name=Label(self.root, text="Name", font=("goudy old style",15), bg = "white", fg="black").place(x=75,y=320)
        txt_name=Entry(self.root, textvariable=self.var_sup_name, font=("goudy old style",15), bg = "light yellow", fg="black").place(x=175,y=320, width=280)
        
        #==Row 3
        lbl_email=Label(self.root, text="Email", font=("goudy old style",15), bg = "white", fg="black").place(x=75,y=400)

        txt_email=Entry(self.root, textvariable=self.var_sup_email, font=("goudy old style",15), bg = "light yellow", fg="black").place(x=175,y=400, width=280)   

        #==Row 4
        lbl_sup_contact=Label(self.root, text="Contact", font=("goudy old style",15), bg = "white", fg="black").place(x=75,y=480)
        txt_sup_contact=Entry(self.root, textvariable=self.var_sup_contact ,font=("goudy old style",15), bg = "Light yellow", fg="black").place(x=175, y=480, width=280)


        #==Button==#
        btn_add=Button(self.root, text="Add",command=self.add, font=("goudy old style",15),bg="#35ca4d",fg="black", cursor="hand2", relief=RIDGE).place(x=926,y=480,width=110,height=30)
        btn_update=Button(self.root, text="Update",command=self.update, font=("goudy old style",15),bg="#c9b3ff",fg="black", cursor="hand2", relief=RIDGE).place(x=1046,y=480,width=110,height=30)
        btn_delete=Button(self.root, text="Delete",command=self.delete, font=("goudy old style",15),bg="#ff696f",fg="black", cursor="hand2", relief=RIDGE).place(x=1166,y=480,width=110,height=30)
        btn_clear=Button(self.root, text="Clear",command=self.clear, font=("goudy old style",15),bg="#feff97",fg="black", cursor="hand2", relief=RIDGE).place(x=1286,y=480,width=110,height=30)

        #==Employee Details Display==#

        emp_frame=Frame(self.root,bd=3, relief=RIDGE, bg="grey")
        emp_frame.place(x=0,y=600,relwidth=1)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)


        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice", "name", "email", "contact"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.supplierTable.heading("invoice",text="Invoice no")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("email",text="Email")
        self.supplierTable.heading("contact",text="Contact")

        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("email",width=100)
        self.supplierTable.column("contact",width=90)

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)

        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.show()
#==========================================================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","Invoice is required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This invoice no. already exists!", parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice, name, email, contact) values(?,?,?,?)",(
                                                    self.var_sup_invoice.get(),
                                                    self.var_sup_name.get(),
                                                    self.var_sup_email.get(),
                                                    self.var_sup_contact.get()  
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        print(row)
        self.var_sup_invoice.set(row[0])
        self.var_sup_name.set(row[1])
        self.var_sup_email.set(row[2])
        self.var_sup_contact.set(row[3])


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","Invoice no. is required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid invoice no.", parent=self.root)
                else:
                    cur.execute("Update supplier set name=?, email=?, contact=? where invoice=?",(
                                                    self.var_sup_name.get(),
                                                    self.var_sup_email.get(),
                                                    self.var_sup_contact.get(),
                                                    self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","Invoice no. is required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid invoice no.", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to delete this supplier?", parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier deleted successfully", parent=self.root)
                        self.clear()
                        

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)


    def clear(self):
        self.var_sup_invoice.set("")
        self.var_sup_name.set("")
        self.var_sup_email.set("")
        self.var_sup_contact.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Search input is required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()