from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
import time
import datetime
from datetime import datetime, timedelta


class sales_statsClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1520x880+230+40')
        self.root.title('Inventory Management System')
        self.root.config(bg="white")

        self.var_sort=StringVar()
        self.var_time=StringVar()
        self.var_filter=StringVar()
        self.var_searchtxt=StringVar()
    
        lbl_title=Label(self.root, text="Track your sales", font=("goudy old style", 20, "bold"), bg="white", fg="black").place(x=0,y=0,relwidth=1, height=70)

        searchFrame=Frame(self.root, bd=3, bg="#8aa892")
        searchFrame.place(x=50, y=100, width=1420, height=70)

        cmb_filterby=ttk.Combobox(searchFrame, textvariable=self.var_filter, values=("Filter","category","supplier","name", "pid"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_filterby.place(x=10,y=10,width=200)
        cmb_filterby.current(0)

        cmb_time=ttk.Combobox(searchFrame, textvariable=self.var_time, values=("Time","Today","This week","This month", "This year"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_time.place(x=220,y=10,width=200)
        cmb_time.current(0)

        cmb_sortby=ttk.Combobox(searchFrame, textvariable=self.var_sort, values=("Sort by","Most sold","Least sold"),state='readonly',justify=CENTER, font=("goudy old style",15))
        cmb_sortby.place(x=430,y=10,width=200)
        cmb_sortby.current(0)

        txt_search=Entry(searchFrame, textvariable=self.var_searchtxt, font=("goudy old style",15),bg="light yellow")
        txt_search.place(x=660,y=10, width=250)

        btn_search=Button(searchFrame, text="Search",command=self.filter, font=("goudy old style",15),bg="#3ec141", cursor="hand2").place(x=920,y=10,width=170,height=30)
        btn_clear=Button(searchFrame, text="Clear",command=self.show, font=("goudy old style",15),bg="#feff97", cursor="hand2").place(x=1100,y=10,width=170,height=30)

        SoldFrame=Frame(self.root, bd=3, bg="#8aa892")
        SoldFrame.place(x= 50, y=160, width=1420, height=700)

        scrolly=Scrollbar(SoldFrame,orient=VERTICAL)
        scrollx=Scrollbar(SoldFrame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        #pid INTEGER PRIMARY KEY , name text, category text, quantity text, price text, supplier text, status text, datetime 

        self.SalesTable=ttk.Treeview(SoldFrame,columns=("pid", "name", "category", "quantity", "price", "supplier","datetime"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.SalesTable.place(x= 50, y=130, width=1420, height=700)
        self.SalesTable.heading("pid",text="Product ID")
        self.SalesTable.heading("name",text="Name")
        self.SalesTable.heading("category",text="Category")
        self.SalesTable.heading("quantity",text="Quantity")
        self.SalesTable.heading("price",text="Price")
        self.SalesTable.heading("supplier",text="Supplier")
        self.SalesTable.heading("datetime",text="Date")

    
        self.SalesTable["show"]="headings"

        self.SalesTable.column("pid",width=90)
        self.SalesTable.column("name",width=100)
        self.SalesTable.column("category",width=100)
        self.SalesTable.column("quantity",width=90)
        self.SalesTable.column("price",width=90)
        self.SalesTable.column("supplier",width=90)
        self.SalesTable.column("datetime",width=90)

        self.SalesTable.pack(fill=BOTH, expand=1)
        #self.SalesTable.bind("<ButtonRelease-1>", self.get_data)

        scrollx.config(command=self.SalesTable.xview)
        scrolly.config(command=self.SalesTable.yview)

        self.show()



#Track sales by
#-search ==> pid, name, category, supplier
#-filter by ==> Date, qty sold

#=================================================================================

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            # Select rows from the 'sold' table, ordered by datetime in descending order
            cur.execute("SELECT * FROM sold ORDER BY datetime DESC")
            rows = cur.fetchall()
            
            # Clear the contents of the SalesTable widget
            self.SalesTable.delete(*self.SalesTable.get_children())
            
            # Insert rows into the SalesTable widget
            for row in rows:
                self.SalesTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
        
    


    def select_records_for_today(table_name):
        # Connect to the database
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        
        try:
            # Get today's date in the format 'YYYY-MM-DD'
            today_date = datetime.date.today().strftime('%Y-%m-%d')
            
            # Execute the query to select records for today's date
            cur.execute(f"SELECT * FROM sold WHERE datetime = ?", (today_date,))
            
            # Fetch all rows from the cursor
            rows = cur.fetchall()
            
            return rows  # Return the selected rows
        except Exception as ex:
            print(f"Error selecting records: {str(ex)}")
        finally:
            con.close()  # Close the database connection


        
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Search input is required")
            if self.var_filter!="Filter":
                cur.execute("select * from product where "+self.var_filter.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
            if self.var_filter!="Filter":
                cur.execute("select * from product where "+self.var_search.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
            else:
                cur.execute("select * from product where "+self.var_search.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)






    def filter(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM sold")
            rows = cur.fetchall()
            
            if self.var_filter.get() != "Filter":
                rows = [row for row in rows if self.var_searchtxt.get().lower() in str(row).lower()]

            if self.var_time.get() != "Time":
                rows = self.apply_time_filter(rows)
            
            if self.var_sort.get() != "Sort":
                rows = self.apply_sort_filter(rows)

            if rows:
                self.SalesTable.delete(*self.SalesTable.get_children())
                for row in rows:
                    self.SalesTable.insert('', END, values=row)
            else:
                messagebox.showinfo("No results", "No records match the selected filters.", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def apply_time_filter(self, rows):
        today = datetime.now()
        filtered_rows = []

        if self.var_time.get() == "Today":
            today_date = today.strftime('%Y-%m-%d')
            filtered_rows = [row for row in rows if row[6][:10] == today_date]

        elif self.var_time.get() == "This week":
            start_of_week = today - timedelta(days=today.weekday())
            end_of_week = start_of_week + timedelta(days=6)
            filtered_rows = [row for row in rows if start_of_week.strftime('%Y-%m-%d') <= row[6][:10] <= end_of_week.strftime('%Y-%m-%d')]

        elif self.var_time.get() == "This month":
            start_of_month = today.replace(day=1)
            if today.month == 12:
                end_of_month = today.replace(month=1, year=today.year+1, day=1) - timedelta(days=1)
            else:
                end_of_month = today.replace(month=today.month+1, day=1) - timedelta(days=1)
            filtered_rows = [row for row in rows if start_of_month.strftime('%Y-%m-%d') <= row[6][:10] <= end_of_month.strftime('%Y-%m-%d')]

        elif self.var_time.get() == "This year":
            start_of_year = today.replace(month=1, day=1)
            end_of_year = today.replace(month=12, day=31)
            filtered_rows = [row for row in rows if start_of_year.strftime('%Y-%m-%d') <= row[6][:10] <= end_of_year.strftime('%Y-%m-%d')]

        return filtered_rows

    def apply_sort_filter(self, rows):
        if self.var_sort.get() == "Most Sold":
            rows.sort(key=lambda x: int(x[3]), reverse=True)
        elif self.var_sort.get() == "Least Sold":
            rows.sort(key=lambda x: int(x[3]))
        return rows


        


        #except Exception as ex:
            #messagebox.showerror("Error",f"Error due to: {str(ex)}", parent=self.root)
    




# Usage example
#table_name = 'your_table_name'
#today_records = select_records_for_today(table_name)
#print(today_records)





if __name__=="__main__":
    root = Tk()
    obj = sales_statsClass(root)
    root.mainloop()