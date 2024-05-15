from tkinter import*
from tkinter import ttk, messagebox
import sqlite3

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1520x880+230+40')
        self.root.title('Inventory Management System')
        self.root.config(bg="White")
        self.root.focus_force()
        #===================================================
        #All Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id=StringVar()
        self.var_emp_gender=StringVar()
        self.var_emp_contact=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_dob=StringVar()
        self.var_emp_doj=StringVar()
        self.var_emp_email=StringVar()
        self.var_emp_pass=StringVar()
        self.var_emp_utype=StringVar()
        self.var_emp_salary=StringVar()
#        self.txt_address=StringVar()


        #==Search Frame==#
        SearchFrame=LabelFrame(self.root, text="Search Employee", bg="white", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=450,y=50,width=600,height=70)

        #==Optioms==#
        cmb_search=ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select","eid","Email","Name", "Contact","Salary"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style",15),bg="light yellow")
        txt_search.place(x=200,y=10)

        btn_search=Button(SearchFrame, text="Search",command=self.search, font=("goudy old style",15),bg="#3ec141", cursor="hand2").place(x=430,y=10,width=150,height=30)

        #==Title==#
        title=Label(self.root, text="Employee Details", font=("goudy old style",15), bg = "#5177ca", fg="white").place(x=0,y=150,width=1520)

        #==Content==#
        #==Row 1
        lbl_empid=Label(self.root, text="Emp ID", font=("goudy old style",15), bg = "white", fg="black").place(x=75,y=250)
        lbl_gender=Label(self.root, text="Gender", font=("goudy old style",15), bg = "white", fg="black").place(x=456,y=250)
        lbl_contact=Label(self.root, text="Contact", font=("goudy old style",15), bg = "white", fg="black").place(x=926,y=250)

        txt_empid=Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style",15), bg = "light yellow", fg="black").place(x=155,y=250, width=280)
        #txt_gender=Entry(self.root, textvariable=self.var_emp_gender, font=("goudy old style",15), bg = "white", fg="black").place(x=610,y=250, width=280)
        cmb_gender=ttk.Combobox(self.root, textvariable=self.var_emp_gender, values=("Select","Male","Female", "Other"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_gender.place(x=610,y=250, width=280)
        cmb_gender.current(0)


        txt_contact=Entry(self.root, textvariable=self.var_emp_contact, font=("goudy old style",15), bg = "light yellow", fg="black").place(x=1070,y=250, width=280)
        #==Row 2
        lbl_name=Label(self.root, text="Name", font=("goudy old style",15), bg = "white", fg="black").place(x=75,y=320)
        lbl_dob=Label(self.root, text="Date of Birth", font=("goudy old style",15), bg = "white", fg="black").place(x=456,y=320)
        lbl_doj=Label(self.root, text="Date of Joining", font=("goudy old style",15), bg = "white", fg="black").place(x=926,y=320)

        txt_name=Entry(self.root, textvariable=self.var_emp_name, font=("goudy old style",15), bg = "light yellow", fg="black").place(x=155,y=320, width=280)
        txt_dob=Entry(self.root, textvariable=self.var_emp_dob, font=("goudy old style",15), bg = "Light yellow", fg="black").place(x=610,y=320, width=280)
        txt_doj=Entry(self.root, textvariable=self.var_emp_doj, font=("goudy old style",15), bg = "light yellow", fg="black").place(x=1070,y=320, width=280)

        #==Row 3
        lbl_email=Label(self.root, text="Email", font=("goudy old style",15), bg = "white", fg="black").place(x=75,y=400)
        lbl_pass=Label(self.root, text="Password", font=("goudy old style",15), bg = "white", fg="black").place(x=456,y=400)
        lbl_utype=Label(self.root, text="User Type", font=("goudy old style",15), bg = "white", fg="black").place(x=926,y=400)

        txt_email=Entry(self.root, textvariable=self.var_emp_email, font=("goudy old style",15), bg = "light yellow", fg="black").place(x=155,y=400, width=280)
        txt_pass=Entry(self.root, textvariable=self.var_emp_pass, font=("goudy old style",15), bg = "Light yellow", fg="black").place(x=610,y=400, width=280)
        txt_utype=Entry(self.root, textvariable=self.var_emp_utype, font=("goudy old style",15), bg = "light yellow", fg="black").place(x=1070,y=400, width=280)
        cmb_utype=ttk.Combobox(self.root, textvariable=self.var_emp_utype, values=("Admin","Employee","HR", "Other"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_utype.place(x=1070,y=400, width=280)
        cmb_utype.current(0)   

        #==Row 4
        lbl_address=Label(self.root, text="Address", font=("goudy old style",15), bg = "white", fg="black").place(x=75,y=480)
        lbl_salary=Label(self.root, text="Salary", font=("goudy old style",15), bg = "white", fg="black").place(x=456,y=480)

        self.txt_address=Text(self.root, font=("goudy old style",15), bg = "light yellow", fg="black")
        self.txt_address.place(x=155,y=480, width=280, height=90)
        txt_salary=Entry(self.root, textvariable=self.var_emp_salary, font=("goudy old style",15), bg = "Light yellow", fg="black").place(x=610, y=480, width=280)
        

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


        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid", "name", "email", "gender", "contact", "dob","doj","pass","utype","address","salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="DOB")
        self.EmployeeTable.heading("doj",text="DOJ")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Sal")
    
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=90)
        self.EmployeeTable.column("contact",width=90)
        self.EmployeeTable.column("dob",width=90)
        self.EmployeeTable.column("doj",width=90)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=90)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=90)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.show()
#==========================================================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","Employee ID is required", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This ID is already assigned", parent=self.root)
                else:
                    cur.execute("Insert into employee (eid, name, email, gender, contact, dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                    self.var_emp_id.get(),
                                                    self.var_emp_name.get(),
                                                    self.var_emp_email.get(),
                                                    self.var_emp_gender.get(),
                                                    self.var_emp_contact.get(),
                                                    self.var_emp_dob.get(),
                                                    self.var_emp_doj.get(),
                                                    self.var_emp_pass.get(),
                                                    self.var_emp_utype.get(),
                                                    self.txt_address.get('1.0', END),
                                                    self.var_emp_salary.get(),    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        print(row)
        self.var_emp_id.set(row[0])
        self.var_emp_name.set(row[1])
        self.var_emp_email.set(row[2])
        self.var_emp_gender.set(row[3])
        self.var_emp_contact.set(row[4])
        self.var_emp_dob.set(row[5])
        self.var_emp_doj.set(row[6])
        self.var_emp_pass.set(row[7])
        self.var_emp_utype.set(row[8])
        self.txt_address.delete('1.0', END),
        self.txt_address.insert(END, row[9]),
        self.var_emp_salary.set(row[10]) 


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","Employee ID is required", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("Update employee set name=?, email=?, gender=?, contact=?, dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                                    self.var_emp_name.get(),
                                                    self.var_emp_email.get(),
                                                    self.var_emp_gender.get(),
                                                    self.var_emp_contact.get(),
                                                    self.var_emp_dob.get(),
                                                    self.var_emp_doj.get(),
                                                    self.var_emp_pass.get(),
                                                    self.var_emp_utype.get(),
                                                    self.txt_address.get('1.0', END),
                                                    self.var_emp_salary.get(), 
                                                    self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","Employee ID is required", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to delete this employee?", parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",self.var_emp_id.get())
                        con.commit()
                        self.clear()
                        messagebox.showinfo("Delete","Employee deleted successfully", parent=self.root)

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)


    def clear(self):
        self.var_emp_id.set("")
        self.var_emp_name.set("")
        self.var_emp_email.set("")
        self.var_emp_gender.set("Select")
        self.var_emp_contact.set("")
        self.var_emp_dob.set("")
        self.var_emp_doj.set("")
        self.var_emp_pass.set("")
        self.var_emp_utype.set("Admin")
        self.txt_address.delete('1.0', END),
        self.var_emp_salary.set("") 
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
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()