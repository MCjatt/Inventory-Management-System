from tkinter import*
from tkinter import ttk, messagebox

class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080+0+0')
        self.root.title('Inventory Management System')
        self.root.config(bg="white")
        #==Title==#
        title=Label(self.root, text='Inventory Management System', font=("goudy old style",35), bg="#5177ca", fg="white").place(x=0,y=0,relwidth=1,height=70)

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
        btn_search=Button(ProductFrame2, text="Search", font=("Goudy old style",15),bg="#3ec141",cursor="hand2").place(x=450, y=55, height=38,width=130)
        btn_showall=Button(ProductFrame2, text="Show All", font=("Goudy old style",15),bg="#cccccc",cursor="hand2").place(x=450, y=10, height=38,width=130)

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

        self.productTable.column("pid",width=90)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=90)
        self.productTable.column("status",width=90)

        self.productTable.pack(fill=BOTH, expand=1)
        #self.productTable.bind("<ButtonRelease-1>", self.get_data)

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
        #self.cartTable.bind("<ButtonRelease-1>", self.get_data)

        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)

        #==CArt Widgets==#

        self.var_name=StringVar()
        self.var_qty=StringVar()
        self.var_price=StringVar()

        lbl_pname=Label(CustomerFrame1, text="Product Name", font=("times new roman", 15), bg="white").place(x=1,y=642)
        txt_pname=Entry(CustomerFrame1, textvariable=self.var_name, font=("times new roman", 15), bg="light yellow", state="readonly").place(x=120,y=642)

        lbl_qty=Label(CustomerFrame1, text="Quantity", font=("times new roman", 15), bg="white").place(x=345,y=642)
        txt_qty=Entry(CustomerFrame1, textvariable=self.var_qty, font=("times new roman", 15), bg="light yellow").place(x=420,y=642, width=30)

        lbl_price=Label(CustomerFrame1, text="Total", font=("times new roman", 15), bg="white").place(x=470,y=642)
        txt_price=Entry(CustomerFrame1, textvariable=self.var_price, font=("times new roman", 13), bg="light yellow", state="readonly").place(x=520,y=642, width=80)

        self.lbl_instock=Label(CustomerFrame1, text="In Stock [21]", font=("times new roman", 15), bg="white").place(x=1,y=675)

        btn_clear_cart=Button(CustomerFrame1, text="Clear", font=("Goudy old style", 20, "bold"),bg="#feff97",fg="black", cursor="hand2", relief=RIDGE).place(x=0,y=700, width=320, height=195)
        btn_add_cart=Button(CustomerFrame1, text="Add/Update", font=("Goudy old style", 20, "bold"),bg="#35ca4d",fg="black", cursor="hand2", relief=RIDGE).place(x=320,y=700, width=320, height=195)


        #==Bill Area==#
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

        self.lbl_amount=Label(billMenuFrame, text="Total: 0", font=("goudy old style", 20, "bold"), bg="#006617", fg="white").place(x=1,y=1, width=213.3, height=86.6)
        self.lbl_discount=Label(billMenuFrame, text="Discount 15%", font=("goudy old style", 20, "bold"), bg="#b04c00", fg="white").place(x=214.3,y=1, width=213.3, height=86.6)
        self.lbl_netpay=Label(billMenuFrame, text="Net Pay", font=("goudy old style", 20, "bold"), bg="#0046b0", fg="white").place(x=427.6,y=1, width=213.3, height=86.6)

        btn_generate=Button(billMenuFrame, text="Generate", font=("Goudy old style",20, "bold"),bg="#02e3ae",cursor="hand2", relief=RIDGE).place(x=1, y=86.6, width=213.3, height=170.2)
        btn_clear=Button(billMenuFrame, text="Clear", font=("Goudy old style",20, "bold"),bg="#feff97",cursor="hand2", relief=RIDGE).place(x=214.3, y=86.6, width=213.3, height=170.2)
        btn_printBill=Button(billMenuFrame, text="Print Bill", font=("Goudy old style",20, "bold"),bg="#e30202",cursor="hand2", relief=RIDGE).place(x=427.6, y=86.6, width=213.3, height=170.2)


        footer=Label(self.root, text="Inventory Management System | Developed by Business", font=("old goudy style", 11), bg="#5177ca", fg="white").pack(side=BOTTOM, fill=X)


if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()