from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
import time
import datetime

class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080+0+0')
        self.root.title('Inventory Management System')
        self.root.config(bg="white")

        self.cart_list=[]
        #==Title==#
        title=Label(self.root, text='Inventory Management System', font=("goudy old style",35, "bold"), bg="#5177ca", fg="white").place(x=0,y=0,relwidth=1,height=70)

        #==btn-logout==#
        btn_logout=Button(self.root,text="logout",font=('times new roman',15,"bold"),bg="yellow", cursor='hand2').place(x=1700,y=15,height=50,width=170)

        #==Product Frame==#
        self.var_search=StringVar()

        ProductFrame1=Frame(self.root, bd=3, relief=RIDGE, bg="white")
        ProductFrame1.place(x=0,y=75,width=640, height=900)

        pTitle=Label(ProductFrame1, text="All Products", font=("goudy old style",20 ,"bold"), bg="#4d4d4d", fg="white").pack(side=TOP, fill=X)

        ProductFrame2=Frame(ProductFrame1, bd=3, relief=RIDGE, bg="white")
        ProductFrame2.place(x=1,y=40,width=630, height=120)

        lbl_search=Label(ProductFrame2, text=("Search Product | by Name"), font=("goudy old style", 15, "bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_name=Label(ProductFrame2, text=("Product Name"), font=("goudy old style", 15, "bold"),bg="white").place(x=2,y=60)

        txt_search=Entry(ProductFrame2, textvariable=self.var_search, font=("goudy old style", 15),bg="light yellow").place(x=150,y=60, width=290)
        #txt_name=Entry(ProductFrame2, text=("Product Name"), font=("goudy old style", 15, "bold"),bg="white").place(x=2,y=60)
        btn_search=Button(ProductFrame2, text="Search",command=self.search, font=("Goudy old style",15),bg="#3ec141",cursor="hand2").place(x=450, y=55, height=38,width=130)
        btn_showall=Button(ProductFrame2, text="Show All",command=self.show, font=("Goudy old style",15),bg="#cccccc",cursor="hand2").place(x=450, y=10, height=38,width=130)
        self.root.bind('<Return>', self.on_key_press)

        ProductFrame3=Frame(ProductFrame1, bd=3, relief=RIDGE, bg="grey")
        ProductFrame3.place(x=1,y=170,relwidth=1, height=725)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)


        self.productTable=ttk.Treeview(ProductFrame3,columns=("pid", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.productTable.heading("pid",text="P ID")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Quantity")
        self.productTable.heading("status",text="Status")

        self.productTable["show"]="headings"

        self.productTable.column("pid",width=25)
        self.productTable.column("name",width=120)
        self.productTable.column("price",width=50)
        self.productTable.column("qty",width=25)
        self.productTable.column("status",width=90)

        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.get_data)

        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        #==Customer Frame==#

        CustomerFrame1=Frame(self.root, bd=3, relief=RIDGE, bg="white")
        CustomerFrame1.place(x=640,y=75,width=640, height=900)
        cTitle=Label(CustomerFrame1, text="Basket", font=("goudy old style",20 ,"bold"), bg="#2e3373", fg="white").pack(side=TOP, fill=X)
        Cart_Frame=Frame(CustomerFrame1, bd=3, relief=RIDGE, bg="white")
        Cart_Frame.place(x=0,y=40, width=635, height=600)

        scrolly=Scrollbar(Cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)


        self.cartTable=ttk.Treeview(Cart_Frame,columns=("name", "price", "qty"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        #self.cartTable.heading("pid",text="P ID")
        self.cartTable.heading("name",text="Name")
        self.cartTable.heading("price",text="Price")
        self.cartTable.heading("qty",text="Quantity")
        #self.cartTable.heading("status",text="Status")

        self.cartTable["show"]="headings"

        #self.cartTable.column("pid",width=90)
        self.cartTable.column("name",width=100)
        self.cartTable.column("price",width=100)
        self.cartTable.column("qty",width=90)
        #self.cartTable.column("status",width=90)

        self.cartTable.pack(fill=BOTH, expand=1)
        self.cartTable.bind("<ButtonRelease-1>", self.get_data_cart)

        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)

        #==CArt Widgets==#

        self.var_name=StringVar()
        self.var_qty=StringVar()
        self.var_price=StringVar()
        self.var_stock=StringVar()
        self.var_pid=StringVar()
        
        
        lbl_pname=Label(CustomerFrame1, text="Product Name", font=("times new roman", 15), bg="white").place(x=1,y=642)
        txt_pname=Entry(CustomerFrame1, textvariable=self.var_name, font=("times new roman", 15), bg="light yellow", state="readonly").place(x=120,y=642)

        lbl_qty=Label(CustomerFrame1, text="Quantity", font=("times new roman", 15), bg="white").place(x=345,y=642)
        txt_qty=Entry(CustomerFrame1, textvariable=self.var_qty, font=("times new roman", 15), bg="light yellow").place(x=420,y=642, width=30)

        lbl_price=Label(CustomerFrame1, text="Total", font=("times new roman", 15), bg="white").place(x=470,y=642)
        txt_price=Entry(CustomerFrame1, textvariable=self.var_price, font=("times new roman", 13), bg="light yellow", state="readonly").place(x=520,y=642, width=80)

        self.lbl_instock=Label(CustomerFrame1, text="In Stock", font=("times new roman", 15), bg="white")
        self.lbl_instock.place(x=1,y=675)

        btn_clear_cart=Button(CustomerFrame1, text="Clear",command=self.clear_cart, font=("Goudy old style", 20, "bold"),bg="#feff97",fg="black", cursor="hand2", relief=RIDGE).place(x=0,y=700, width=320, height=195)
        btn_add_cart=Button(CustomerFrame1, text="Add/Update",command=self.add_cart, font=("Goudy old style", 20, "bold"),bg="#35ca4d",fg="black", cursor="hand2", relief=RIDGE).place(x=320,y=700, width=320, height=195)


        #==Bill Area==#
        self.payment_method="#-#-#-#-#"

        billFrame=Frame(self.root, bd=2,relief=RIDGE, bg="white")
        billFrame.place(x=1280,y=75, width=640,height=640)
        bTitle=Label(billFrame, text="Bill", font=("goudy old style",20 ,"bold"), bg="#b0aa02", fg="white").pack(side=TOP, fill=X)
        scrolly=Scrollbar(billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(billFrame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #==Billing Buttons==#
        billMenuFrame=Frame(self.root, bd=2,relief=RIDGE, bg="white")
        billMenuFrame.place(x=1280,y=715, width=640,height=260)

        self.lbl_amount=Label(billMenuFrame, text="Total: 0", font=("goudy old style", 15, "bold"), bg="#006617", fg="white")
        self.lbl_amount.place(x=1,y=1, width=213.3, height=86.6)
        self.lbl_discount=Label(billMenuFrame, text="none", font=("goudy old style", 15, "bold"), bg="#b04c00", fg="white")
        self.lbl_discount.place(x=214.3,y=1, width=213.3, height=86.6)
        self.lbl_netpay=Label(billMenuFrame, text="Net Pay", font=("goudy old style", 15, "bold"), bg="#0046b0", fg="white")
        self.lbl_netpay.place(x=427.6,y=1, width=213.3, height=86.6)

        btn_generate=Button(billMenuFrame, text="Generate",command=self.showBill, font=("Goudy old style",20, "bold"),bg="#02e3ae",cursor="hand2", relief=RIDGE).place(x=1, y=86.6, width=213.3, height=170.2)
        btn_clear=Button(billMenuFrame, text="Clear",command=self.clear_bill, font=("Goudy old style",20, "bold"),bg="#feff97",cursor="hand2", relief=RIDGE).place(x=214.3, y=86.6, width=213.3, height=85.1)
        btn_cash=Button(billMenuFrame, text="Cash",command=self.byCash, font=("Goudy old style",20, "bold"),bg="#03912e",cursor="hand2", relief=RIDGE).place(x=214.3, y=171.7, width=106.65, height=85.1)
        btn_card=Button(billMenuFrame, text="Card",command=self.byCard, font=("Goudy old style",20, "bold"),bg="#1392d1",cursor="hand2", relief=RIDGE).place(x=320.95, y=171.7, width=106.65, height=85.1)
        btn_printBill=Button(billMenuFrame, text="Print Bill",command=self.generateBill, font=("Goudy old style",20, "bold"),bg="#e30202",cursor="hand2", relief=RIDGE).place(x=427.6, y=86.6, width=213.3, height=170.2)


        footer=Label(self.root, text="Inventory Management System | Developed by Business", font=("old goudy style", 11), bg="#5177ca", fg="white").pack(side=BOTTOM, fill=X)

        self.show()
        self.getSettings()
        #self.bill_top()

        #==Functions================
        

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select pid, name, price, quantity, status from product where status='Active'")  
            rows = cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)
    


    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="Select":
                messagebox.showerror("Error","Select what to search", parent=self.root)
            elif self.var_search.get()=="":
                messagebox.showerror("Error", "Search input is required")
            else:
                cur.execute("select pid, name, price, quantity, status from product where pid LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)
        
    


    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        #print(row)
        self.var_name.set(row[1]),
        self.var_price.set(row[2]),
        self.var_qty.set("1"),
        self.var_stock.set(row[3]),
        self.var_pid.set(row[0])
        
        self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
        
    def get_data_cart(self,ev):
        f=self.cartTable.focus()
        content=(self.cartTable.item(f))
        row=content['values']
        #print(row)
        self.var_name.set(row[0]),
        self.var_price.set(row[1]),
        self.var_qty.set(row[3]),
        
        self.lbl_instock.config(text=f"In Stock [{str(row[2])}]")
    
    def clear_cart(self):
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_search.set("")
        self.lbl_instock.config(text=f'In Stock')
        
    
    def clear_bill(self):
        del self.cart_list[:]
        self.txt_bill_area.delete('1.0', END)
        self.clear_cart()
        self.show()
        self.showCart()


    def add_cart(self):
        if self.var_qty.get()=="":
            messagebox.showerror("Error", "Quantity is required", parent = self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error", "Exceeding stock quantity", parent = self.root)
        elif self.var_name.get()=="":
            messagebox.showerror("Error", "Select product from list", parent = self.root)
        else:
            #price_cal=int(self.var_qty.get())*float(self.var_price.get())
            #price_cal=float(price_cal)
            price_cal=float(self.var_price.get())
        
        self.cart_data=[self.var_name.get(), price_cal, self.var_qty.get(), self.var_stock.get(), self.var_pid.get(), self.var_price.get()]
        
        #=update cart==

        present="no"
        index_=0
        for row in self.cart_list:
            print(row)
            if self.var_name.get()==row[0]:
                present="yes"
                break
            index_+=1
        
        if present=="yes":
            op=messagebox.askyesno("Confirm", "Product already present, edit quantity below", parent = self.root)
            if op==True:
                if self.var_qty.get()=='0':
                    print(self.cart_list)
                    self.cart_list.pop(index_)
                else:
                    #self.cart_list[index_][1]=price_cal
                    self.cart_list[index_][2]=self.var_qty.get()
        else:
            self.cart_list.append(self.cart_data)
        
        self.showCart()
        self.bill_updates()
        
        self.bill_amount = StringVar()
        self.item_total = StringVar()

    def bill_updates(self):
        self.bill_amt=0
        self.net_pay=0
        self.discount=0
        self.discount="{:.2f}".format(self.discount)
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+float(row[1]) * int(row[2])
        self.discount=(self.bill_amt * (15/100))
        self.net_pay=self.bill_amt - self.discount
        self.lbl_amount.config(text=f"Bill Amount(Eur)\n{self.bill_amt:.2f}")
        self.lbl_netpay.config(text=f"Net Pay(Eur)\n{self.net_pay:.2f}")
        self.bill_amount=int(self.bill_amt)
        


    
    def showCart(self):
        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)
    
    def showBill(self):
        if len(self.cart_list)==0:
            messagebox.showerror("Error","Add products to the cart first")
        #==top==#
        self.bill_top()
        #==middle==#
        self.bill_middle()
        #==Bottom==#
        self.bill_bottom()

        
    
    def generateBill(self):
        fp=open(f'bill/{str(self.invoice)}.txt','w')
        fp.write(self.txt_bill_area.get(1.0, END))
        fp.close()

        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:  
            for row in self.cart_list:
                pid=row[4]
                qty=int(row[3])-int(row[2])
                if int(row[2])==int(row[3]):
                    status='Inactive'
                if int(row[2])!=int(row[3]):
                    status='Active'
                cur.execute("Update product set quantity=?, status=? where pid=?",(
                    qty,
                    status,
                    pid,
                ))    
                con.commit()
            con.close()
            self.show()
            self.addtoSold()
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)

        messagebox.showinfo('Saved', 'Bill has been generated', parent = self.root)
    

    def getSettings(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM settings")
            row=cur.fetchone()
            
            if row == None:
                messagebox.showerror("Error", "Setup shop in settings first!")
            else:
                #pid INTEGER PRIMARY KEY AUTOINCREMENT, name text, address1 text, address2 text, address3 text, discount text
                self.shop_name=row[1]
                self.shop_add1=row[2]
                self.shop_add2=row[3]
                self.shop_add3=row[4]
                self.discount=row[5]
                self.lbl_discount.config(text="Discount: "+self.discount+"%")
                print(row[1])
        
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)

    
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
{str(self.shop_name)} \t\t\t{str(self.shop_add1)}\t\t\t
\t\t\t{str(self.shop_add2)}\t\t\t
\t\t\t{str(self.shop_add3)}\t\t\t
{str("=" *47)}

Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}

{str("=" *47)}
Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0', END)
        self.txt_bill_area.insert('1.0', bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
Bill Amount\t\t\t\tEur.{self.bill_amt}
Discount\t\t\t\tEur.{self.discount:.2f}
Net Pay\t\t\t\tEur.{self.net_pay:.2f}
Payment Method:\t\t\t\t{str(self.payment_method)}
{str("="*47)}
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)

    def bill_middle(self):
        for row in self.cart_list:
            name=row[0]
            qty=row[2]
            price=float(row[1])*int(row[2])
            price=str(price)
            self.txt_bill_area.insert(END, "\n"+name+"\t\t\t" + qty + "\t Eur." + price)
    


    def byCash(self):
        self.payment_method="Cash"
        self.showBill()
    def byCard(self):
        self.payment_method="Card"
        self.showBill()


    def on_key_press(self, event):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get() == "":  # Check if Enter key (or other terminator character) is pressed
                print("No barcode scanned")
                # Call your function here with the scanned barcode
                # your_function(scanned_data)
            else:
                cur.execute("select name, price, quantity from product where pid LIKE '%"+self.var_search.get()+"%' and status='Active'")
                row=cur.fetchone()
                if len(row)!=0:
                    self.var_name.set(row[0])
                    self.var_price.set(row[1])
                    self.var_qty.set("1")
                    self.var_stock.set(row[2])
                    self.var_pid.set(self.var_search.get())
                    self.add_cart()
                    self.clear_cart()
                else:
                    print("Nothing found for the pid searched")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)
        

        #when entered is pressed after a scan search for the pid in products table.
        #if empty nothing happens.
        #self.cart_data=[self.var_name.get(), price_cal, self.var_qty.get(), self.var_stock.get(), self.var_pid.get(), self.var_price.get()]
        #sold(pid INTEGER PRIMARY KEY , name text, category text, quantity text, price text, supplier text, status text )
        #product(pid INTEGER PRIMARY KEY , category text, supplier text, name text, price text, quantity text, status text )

    
    def addtoSold(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        
        try:
            for item in self.cart_list:
                cur.execute("SELECT * FROM product WHERE pid=?", (item[4],))
                row = cur.fetchone()
                qty=float(self.var_qty.get())
                row4 = float(row[4])  # Convert row[4] to float if it's a string
                price = qty * row4  # Perform the multiplication

                
                if row:
                    # Get the current date and time
                    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    # Insert data into the 'sold' table, including the current datetime
                    cur.execute("INSERT INTO sold (pid, name, category, quantity, price, supplier, datetime) VALUES (?, ?, ?, ?, ?, ?, ?)", (
                        row[0],  # pid
                        row[3],  # name
                        row[1],  # category
                        self.var_qty.get(),  # quantity
                        price,  # price
                        row[2],  # supplier
                        current_datetime  # datetime
                    ))
                else:
                    print("Product not found for pid:", item[4])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.commit()
            con.close()
            print(self.cart_list)
        
        


if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()