from tkinter import*
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import BillClass
from settings import settingClass
from sales_stats import sales_statsClass
import sqlite3
import time
import datetime
from datetime import datetime, timedelta
from tkinter import ttk, messagebox
import threading

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080+0+0')
        self.root.title('Inventory Management System')
        self.root.config(bg="white")
        #==Title==#
        title=Label(self.root, text='ShelfStock', font=("goudy old style",35, "bold"), bg="#EC7C26", fg="white").place(x=0,y=0,relwidth=1,height=70)

        #==btn-logout==#
        btn_logout=Button(self.root,text="logout",font=('goudy old style',15,"bold"),bg="yellow", cursor='hand2').place(x=1700,y=15,height=50,width=170)

        #==clock==#
       # self.lbl_clock=Label(self.root, text='Welcome to Inventory Management System\t\t Date: DD+MM+YY\t\t Time: HH:MM:SS', font=("goudy old style",15))
       #self.lbl_clock.place(x=0,y=0,relwidth=1,height=150)

       #==Left Menu==#
        LeftMenu=Frame(self.root,bg='white')
        LeftMenu.place(x=0,y=102,width=200,height=600)
        
        #==Left menu Label==#
        lbl_menu=Label(LeftMenu, text='Menu',font=('goudy old style',30),bg='Light Blue', relief=RIDGE).pack(side=TOP, fill=X)
        btn_employee=Button(LeftMenu, text='Employee', command=self.employee,font=('goudy old style',20),bg='white',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier=Button(LeftMenu, text='Supplier',command=self.supplier,font=('goudy old style',20),bg='white',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_category=Button(LeftMenu, text='Category',command=self.category,font=('goudy old style',20),bg='white',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_product=Button(LeftMenu, text='Product',command=self.product,font=('goudy old style',20),bg='white',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_sales=Button(LeftMenu, text='Sales',command=self.sales, font=('goudy old style',20),bg='white',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_Billing=Button(LeftMenu, text='Billing',command=self.billing, font=('goudy old style',20),bg='#fffd80',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_settings=Button(LeftMenu, text='Settings',command=self.setting, font=('goudy old style',20),bg='#fffd80',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_sales_stats=Button(LeftMenu, text='Track sales',command=self.sales_stats, font=('goudy old style',20),bg='#fffd80',bd=3,cursor="hand2").pack(side=TOP, fill=X)
        #lbl_menu=Label(LeftMenu, text='Menu',font=('times new roman',20),bg='#009688').pack(side=TOP, fill=X)     
        #==Content==#
        self.lbl_totalsales=Button(self.root,text="Total sales: 0", command=self.sales_stats,anchor="w" , bg="#f7d89e",font=('goudy old style',20)) 
        self.lbl_totalsales.place(x=350,y=150,height=60,width=550)

        self.lbl_totalearning=Button(self.root,text="Todays Earning: 0",anchor="w" , bg="#f7d89e",font=('goudy old style',20)) 
        self.lbl_totalearning.place(x=1050,y=150,height=60,width=550)

        #self.lbl_totalsales_shadow=Label(self.root, bg="black") 
        #self.lbl_totalsales.place(x=340,y=130,height=100,width=600)

        

        #=======================================================
        self.updateDashboard()  

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        self.total_sales()
    
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

    def sales_stats(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=sales_statsClass(self.new_win)         
        #self.updateDashboard()
        

        #self.root.after(5000, self.total_sales)






#===========================================================================================================================================#
#===========================================================================================================================================#
#===========================================================================================================================================#
        
        self.var_total_sales=StringVar()
        self.var_earnings=StringVar()
        self.var_items_sold=StringVar()
    
    def total_sales(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            filtered_rows=[]
            today=datetime.now()
            today_date = today.strftime('%Y-%m-%d')
            
            # Execute the query to select records for today's date
            cur.execute("SELECT * FROM sold")
            
            # Fetch all rows from the cursor
            rows = cur.fetchall()
            filtered_rows = [row for row in rows if row[6][:10] == today_date]
            self.var_total_sales=len(filtered_rows)
            #print(rows)
            #print(filtered_rows)
            self.lbl_totalsales.config(text=f"Total sales: {self.var_total_sales}")


        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)
    

    def todaysEarning(self):
        total=0.0
        qty=0
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            filtered_rows=[]
            today=datetime.now()
            today_date = today.strftime('%Y-%m-%d')
            
            # Execute the query to select records for today's date
            cur.execute("SELECT * FROM sold")
            
            # Fetch all rows from the cursor
            rows = cur.fetchall()
            filtered_rows = [row for row in rows if row[6][:10] == today_date]
            #print(filtered_rows)
            for price in filtered_rows:
                if price[3]!='1':
                    qty=float(price[3])*float(price[4])
                    total=total+qty
                else:
                    total=total+float(price[4])
            self.lbl_totalearning.config(text=f"Todays Earning: €{str(total)}")


        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)
        

    def updateDashboard(self):
        i=0
        i=i+1
        print(i)
        self.total_sales()
        self.todaysEarning()
        threading.Timer(5.0, self.updateDashboard).start()




        #self.todaysEarning()
    


        
               

#self.total_sales()



if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
            