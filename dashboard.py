from tkinter import*
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080+0+0')
        self.root.title('Inventory Management System')
        self.root.config(bg="white")
        #==Title==#
        title=Label(self.root, text='Inventory Management System', font=("goudy old style",35), bg="#5177ca", fg="white").place(x=0,y=0,relwidth=1,height=70)

        #==btn-logout==#
        btn_logout=Button(self.root,text="logout",font=('times new roman',15,"bold"),bg="yellow", cursor='hand2').place(x=1700,y=15,height=50,width=170)

        #==clock==#
       # self.lbl_clock=Label(self.root, text='Welcome to Inventory Management System\t\t Date: DD+MM+YY\t\t Time: HH:MM:SS', font=("Times new roman",15))
       #self.lbl_clock.place(x=0,y=0,relwidth=1,height=150)

       #==Left Menu==#
        LeftMenu=Frame(self.root,bd=5,relief=RIDGE,bg='light grey')
        LeftMenu.place(x=0,y=102,width=200,height=400)
        
        #==Left menu Label==#
        lbl_menu=Label(LeftMenu, text='Menu',font=('goudy old style',30),bg='#d3f099', relief=RIDGE).pack(side=TOP, fill=X)
        btn_employee=Button(LeftMenu, text='Employee', command=self.employee,font=('times new roman',20),bg='Light grey',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier=Button(LeftMenu, text='Supplier',command=self.supplier,font=('times new roman',20),bg='Light grey',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_category=Button(LeftMenu, text='Category',command=self.category,font=('times new roman',20),bg='Light grey',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_product=Button(LeftMenu, text='Product',command=self.product,font=('times new roman',20),bg='Light grey',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_sales=Button(LeftMenu, text='Sales',command=self.sales, font=('times new roman',20),bg='Light grey',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_exit=Button(LeftMenu, text='Exit',font=('times new roman',20),bg='light blue',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        #lbl_menu=Label(LeftMenu, text='Menu',font=('times new roman',20),bg='#009688').pack(side=TOP, fill=X)     

        #==Content==#
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bd=5, relief=RIDGE , bg="#8bbea1",fg="white",font=('goudy old style',25, "bold")) 
        self.lbl_employee.place(x=350,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]",bd=5, relief=RIDGE , bg="#8bbea1",fg="white",font=('goudy old style',25, "bold")) 
        self.lbl_supplier.place(x=800,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[0]",bd=5, relief=RIDGE , bg="#8bbea1",fg="white",font=('goudy old style',25, "bold")) 
        self.lbl_category.place(x=1200,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[0]",bd=5, relief=RIDGE , bg="#8bbea1",fg="white",font=('goudy old style',25, "bold")) 
        self.lbl_product.place(x=350,y=350,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[0]",bd=5, relief=RIDGE , bg="#8bbea1",fg="white",font=('goudy old style',25, "bold")) 
        self.lbl_sales.place(x=800,y=350,height=150,width=300)

        #=======================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)          



if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
            