from tkinter import*
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import BillClass
from settings import settingClass


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080+0+0')
        self.root.title('Inventory Management System')
        self.root.config(bg="white")
        #==Title==#
        title=Label(self.root, text='ShelfStock', font=("goudy old style",35, "bold"), bg="#292929", fg="light grey").place(x=0,y=0,relwidth=1,height=70)

        #==btn-logout==#
        btn_logout=Button(self.root,text="logout",font=('times new roman',15,"bold"),bg="yellow", cursor='hand2').place(x=1700,y=15,height=50,width=170)

        #==clock==#
       # self.lbl_clock=Label(self.root, text='Welcome to Inventory Management System\t\t Date: DD+MM+YY\t\t Time: HH:MM:SS', font=("Times new roman",15))
       #self.lbl_clock.place(x=0,y=0,relwidth=1,height=150)

       #==Left Menu==#
        LeftMenu=Frame(self.root,bg='white')
        LeftMenu.place(x=0,y=102,width=200,height=600)
        
        #==Left menu Label==#
        lbl_menu=Label(LeftMenu, text='Menu',font=('goudy old style',30),bg='Light Blue', relief=RIDGE).pack(side=TOP, fill=X)
        btn_employee=Button(LeftMenu, text='Employee', command=self.employee,font=('times new roman',20),bg='white',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier=Button(LeftMenu, text='Supplier',command=self.supplier,font=('times new roman',20),bg='white',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_category=Button(LeftMenu, text='Category',command=self.category,font=('times new roman',20),bg='white',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_product=Button(LeftMenu, text='Product',command=self.product,font=('times new roman',20),bg='white',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_sales=Button(LeftMenu, text='Sales',command=self.sales, font=('times new roman',20),bg='white',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_Billing=Button(LeftMenu, text='Billing',command=self.billing, font=('times new roman',20),bg='#fffd80',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_settings=Button(LeftMenu, text='Settings',command=self.setting, font=('times new roman',20),bg='#fffd80',bd=3,cursor="hand2").pack(side=TOP, fill=X)
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

    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)

    def setting(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=settingClass(self.new_win)          



if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
            