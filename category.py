from tkinter import*
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1520x880+230+40')
        self.root.title('Inventory Management System')
        self.root.config(bg="White")
        self.root.focus_force()
        #==Variables==
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
    
        #==Title==#
        lbl_title=Label(self.root, text="Manage Product Category", font=("goudy old style",30), bg='#5177ca',fg='white').pack(side=TOP, fill=X)
        lbl_name=Label(self.root, text="Enter category name :", font=("goudy old style",20), bg='white').place(x=50,y=120)
        txt_name=Entry(self.root, textvariable=self.var_name, font=("goudy old style",20), bg='light yellow').place(x=50,y=175)

        btn_add=Button(self.root, text="Add",command=self.add, font=("goudy old style",15), bg="#35ca4d",cursor="hand2",fg="white").place(x=360,y=175, width=150, height=38)
        btn_delete=Button(self.root, text="Delete",command=self.delete, font=("goudy old style",15), bg="red",cursor="hand2",fg="white").place(x=520,y=175, width=150, height=38)


 #==Category Details Display==#

        cat_frame=Frame(self.root,bd=3, relief=RIDGE, bg="grey")
        cat_frame.place(x=900,y=170,width=400, height=600)
        #cat_frame.place(x=0,y=600,relwidth=1)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)


        self.categoryTable=ttk.Treeview(cat_frame,columns=("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.categoryTable.heading("cid", text="C ID")
        self.categoryTable.heading("name",text="Name")

        self.categoryTable["show"]="headings"

        self.categoryTable.column("cid",width=1)
        self.categoryTable.column("name",width=100)

        self.categoryTable.pack(fill=BOTH, expand=1)
        self.categoryTable.bind("<ButtonRelease-1>", self.get_data)

        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        self.show()

#==Functions==#


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","Category name is required", parent=self.root)
            else:
                cur.execute("select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This category already exists!", parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(
                                                    self.var_name.get(),  
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Category added successfully", parent=self.root)
                    #self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)
        self.show()



    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows = cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)

        
    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","Select category first", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid category, try again", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to delete this category?", parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category deleted successfully", parent=self.root)
                        #self.clear()
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
                        

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)



if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()