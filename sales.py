from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
import os

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1520x880+230+40')
        self.root.title('Inventory Management System')
        self.root.config(bg="White")
        self.root.focus_force()

        self.var_invoice=StringVar()
        self.bill_list=[]

#==Title==#
        lbl_title=Label(self.root, text="Customer Bills", font=("goudy old style",30), bg='#5177ca',fg='white').pack(side=TOP, fill=X)

        lbl_invoice=Label(self.root, text="Invoice no.", font=("goudy old style",20), bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root, textvariable=self.var_invoice, font=("goudy old style",20), bg="light yellow").place(x=200,y=100)

        #==Button==#
        btn_search=Button(self.root, text="Search",command=self.search, font=("goudy old style", 15), bg="#35ca4d", relief=RIDGE, cursor="hand2").place(x=520,y=100, width=160,height=35)
        btn_clear=Button(self.root, text="Clear",command=self.clear, font=("goudy old style", 15), bg="#feff97", relief=RIDGE, cursor="hand2").place(x=700,y=100, width=160,height=35)

        #==Sales Frame==#

        sales_Frame=Frame(self.root, bd=3,relief=RIDGE)
        sales_Frame.place(x=50,y=150, width=810,height=700)

        scrolly=Scrollbar(sales_Frame, orient=VERTICAL)

        self.Sales_List=Listbox(sales_Frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH,expand=1)
        self.Sales_List.bind("<ButtonRelease-1>", self.get_data)

        #==Bill==#
        bill_Frame=Frame(self.root, bd=3,relief=RIDGE)
        bill_Frame.place(x=865,y=150, width=645,height=700)

        scrolly2=Scrollbar(bill_Frame, orient=VERTICAL)

        self.bill_area=Listbox(bill_Frame, font=("goudy old style", 15), bg="light yellow", yscrollcommand=scrolly2)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        self.show()

#========================================================================================================================

    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0, END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])
    
    def get_data(self, ev):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        print(file_name)
        self.bill_area.delete(0,END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
    
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no is required", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete(0, END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid invoice no.", parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete(0,END)            

                             

if __name__=="__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()