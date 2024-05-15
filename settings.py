from tkinter import*
from tkinter import ttk, messagebox
import sqlite3

class settingClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1520x880+230+40')
        self.root.title('Inventory Management System')
        self.root.config(bg="White")
        self.root.focus_force()
    
        self.bus_name=StringVar()
        self.bus_add1=StringVar()
        self.bus_add2=StringVar()
        self.bus_add3=StringVar()
        self.bus_discount=StringVar()

        title=Label(self.root, text='Inventory Management System', font=("goudy old style",35, "bold"), bg="#5177ca", fg="white").place(x=0,y=0,relwidth=1,height=70)
        lbl_bus_name=Label(self.root, text="Shop Name", font=("goudy old style", 20), bg="white", fg="Black").place(x=10, y=110)
        txt_bus_name=Entry(self.root, textvariable=self.bus_name, font=("goudy old style", 18), bg="light yellow", fg="Black").place(x=170, y=112, height=30)

        lbl_bus_add1=Label(self.root, text="Address 1", font=("goudy old style", 20), bg="white", fg="Black").place(x=10, y=160)
        txt_bus_add1=Entry(self.root, textvariable=self.bus_add1, font=("goudy old style", 18), bg="light yellow", fg="Black").place(x=170, y=162, height=30)

        lbl_bus_add2=Label(self.root, text="Address 2", font=("goudy old style", 20), bg="white", fg="Black").place(x=10, y=210)
        txt_bus_add2=Entry(self.root, textvariable=self.bus_add2, font=("goudy old style", 18), bg="light yellow", fg="Black").place(x=170, y=212, height=30)

        lbl_bus_add3=Label(self.root, text="Address 3", font=("goudy old style", 20), bg="white", fg="Black").place(x=10, y=260)
        txt_bus_add3=Entry(self.root, textvariable=self.bus_add3, font=("goudy old style", 18), bg="light yellow", fg="Black").place(x=170, y=262, height=30)

        lbl_bus_discount=Label(self.root, text="Discount", font=("goudy old style", 20), bg="white", fg="Black").place(x=10, y=310)
        txt_bus_discount=Entry(self.root, textvariable=self.bus_discount, font=("goudy old style", 18), bg="light yellow", fg="Black").place(x=170, y=312, height=30)

        btn_save=Button(self.root, text="Save", command=self.save, font=("goudy old style", 15, "bold"), bg="green").place(x=1400, y=820)

        #=====================================

    def save(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.bus_name.get()=="" or self.bus_add1.get()=="" or self.bus_add2.get()=="" or self.bus_add3.get()=="": #or self.var_name.get()==:
                messagebox.showerror("Error","All fields are required", parent=self.root)
            else:
                cur.execute("select * from settings where name=?",(self.bus_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This name is already assigned", parent=self.root)
                else:
                    cur.execute("Update settings set name=?, address1=?, address2=?, address3=?, discount=? where pid=1",(
                                                            self.bus_name.get(),
                                                            self.bus_add1.get(),
                                                            self.bus_add2.get(),
                                                            self.bus_add3.get(),
                                                            self.bus_discount.get(),
                                                            
                            ))
                    con.commit()
                    messagebox.showinfo("Success","Settings saved", parent=self.root)
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = settingClass(root)
    root.mainloop()


#Create a db for name, address and discount value.
#add/update in settings menu.
#fetch values in billing section