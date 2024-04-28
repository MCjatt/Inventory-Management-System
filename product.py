from tkinter import*
from tkinter import ttk, messagebox
import sqlite3

class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1520x880+230+40')
        self.root.title('Inventory Management System')
        self.root.config(bg="White")
        self.root.focus_force()

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()


        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=760,height=860)

        title=Label(product_Frame, text="Manage Product Details", font=("goudy old style",22), bg = "#5177ca", fg="white").pack(side=TOP, fill=X)

        lbl_category=Label(product_Frame, text="Category", font=("goudy old style",20),bg="white").place(x=40,y=90)
        lbl_supplier=Label(product_Frame, text="Supplier", font=("goudy old style",20),bg="white").place(x=40,y=170)
        lbl_product_name=Label(product_Frame, text="Name", font=("goudy old style",20),bg="white").place(x=40,y=250)
        lbl_price=Label(product_Frame, text="Price", font=("goudy old style",20),bg="white").place(x=40,y=330)
        lbl_quantity=Label(product_Frame, text="Quantity", font=("goudy old style",20),bg="white").place(x=40,y=410)
        lbl_status=Label(product_Frame, text="Status", font=("goudy old style",20),bg="white").place(x=40,y=490)

        #txt_category=Label(product_Frame, text="Category", font=("goudy old style",20),bg="white").place(x=40,y=80)
        cmb_cat=ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list,state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_cat.place(x=300,y=94,width=300, height=30)
        cmb_cat.current(0)

        #txt_category=Label(product_Frame, text="Category", font=("goudy old style",20),bg="white").place(x=40,y=80)
        cmb_sup=ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list,state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_sup.place(x=300,y=174,width=300, height=30)
        cmb_sup.current(0)

        txt_name=Entry(product_Frame, textvariable=self.var_name,bg="light yellow", font=("goudy old style",15)).place(x=300,y=254,width=300, height=30)
        txt_price=Entry(product_Frame, textvariable=self.var_price,bg="light yellow", font=("goudy old style",15)).place(x=300,y=334,width=300, height=30)
        txt_quantity=Entry(product_Frame, textvariable=self.var_quantity,bg="light yellow", font=("goudy old style",15)).place(x=300,y=414,width=300, height=30)
        #txt_status=Entry(product_Frame, textvariable=self.var_status,bg="light yellow", font=("goudy old style",15)).place(x=300,y=484,width=300, height=30)

        cmb_status=ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active","Inactive"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_status.place(x=300,y=494,width=300, height=30)
        cmb_status.current(0)

         #==Button==#
        btn_add=Button(product_Frame, text="Add", command=self.add, font=("goudy old style",15),bg="#35ca4d",fg="black", cursor="hand2", relief=RIDGE).place(x=40,y=660,width=165,height=50)
        btn_update=Button(product_Frame, text="Update",command=self.update, font=("goudy old style",15),bg="#c9b3ff",fg="black", cursor="hand2", relief=RIDGE).place(x=210,y=660,width=165,height=50)
        btn_delete=Button(product_Frame, text="Delete",command=self.delete, font=("goudy old style",15),bg="#ff696f",fg="black", cursor="hand2", relief=RIDGE).place(x=380,y=660,width=165,height=50)
        btn_clear=Button(product_Frame, text="Clear",command=self.clear, font=("goudy old style",15),bg="#feff97",fg="black", cursor="hand2", relief=RIDGE).place(x=550,y=660,width=165,height=50)

        SearchFrame=LabelFrame(self.root, text="Search Product", bg="white", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=800,y=5,width=700,height=70)

        #==Optioms==#
        cmb_search=ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select","Category","Supplier","Name",),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=200)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style",15),bg="light yellow")
        txt_search.place(x=220,y=10, width=250)

        btn_search=Button(SearchFrame, text="Search",command=self.search, font=("goudy old style",15),bg="#3ec141", cursor="hand2").place(x=475,y=10,width=170,height=30)


        #==Product Details Table==#

        emp_frame=Frame(self.root,bd=3, relief=RIDGE, bg="grey")
        emp_frame.place(x=800,y=80,width=700, height=790)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.ProductTable=ttk.Treeview(emp_frame,columns=("pid", "category", "supplier", "name", "price", "quantity","status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.ProductTable.heading("pid",text="P ID")
        self.ProductTable.heading("category",text="Category")
        self.ProductTable.heading("supplier",text="Supplier")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("quantity",text="Quantity")
        self.ProductTable.heading("status",text="Status")

    
        self.ProductTable["show"]="headings"

        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("category",width=100)
        self.ProductTable.column("supplier",width=100)
        self.ProductTable.column("name",width=90)
        self.ProductTable.column("price",width=90)
        self.ProductTable.column("quantity",width=90)
        self.ProductTable.column("status",width=90)

        self.ProductTable.pack(fill=BOTH, expand=1)
        self.ProductTable.bind("<ButtonRelease-1>", self.get_data)

        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.show()
        



#=====================================

    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select name from category")
            cat=cur.fetchall()
            self.cat_list.append("Emplty")
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
                #print(catList)
            cur.execute("select name from supplier")
            sup=cur.fetchall()
            self.sup_list.append("Empty")
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_name.get()=="" or self.var_price.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","All fields are required", parent=self.root)
            else:
                cur.execute("select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This name is already assigned", parent=self.root)
                else:
                    cur.execute("Insert into product (category, supplier, name, price, quantity,status) values(?,?,?,?,?,?)",(
                                                        self.var_cat.get(),
                                                        self.var_sup.get(),
                                                        self.var_name.get(),
                                                        self.var_price.get(),
                                                        self.var_quantity.get(),
                                                        self.var_status.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Product added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            rows = cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        print(row)
        self.var_pid.set(row[0])
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_quantity.set(row[5]),
        self.var_status.set(row[6]),


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","Product ID is required", parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid product ID", parent=self.root)
                else:
                    cur.execute("Update product set category=?, supplier=?, name=?, price=?, quantity=?,status=? where pid=?",(
                                                        self.var_cat.get(),
                                                        self.var_sup.get(),
                                                        self.var_name.get(),
                                                        self.var_price.get(),
                                                        self.var_quantity.get(),
                                                        self.var_status.get(),
                                                        self.var_pid.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","Product ID is required", parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Product ID", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to delete this product?", parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",self.var_pid.get())
                        con.commit()
                        self.clear()
                        messagebox.showinfo("Delete","Product deleted successfully", parent=self.root)

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)


    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_quantity.set("")
        self.var_status.set("Active")
        self.var_pid.set("") 
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select what to search", parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Search input is required")
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)



if __name__=="__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()