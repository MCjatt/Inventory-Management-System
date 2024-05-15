import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, doj text, pass text, utype text, address text, salary text)")  
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, contact text)")  
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")  
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY , category text, supplier text, name text, price text, quantity text, status text )")  
    con.commit()

    #cur.execute("DROP TABLE IF EXISTS sold;")
    #con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS settings(pid INTEGER PRIMARY KEY AUTOINCREMENT, name text, address1 text, address2 text, address3 text, discount text)")  
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS sold(pid INTEGER , name text, category text, quantity text, price text, supplier text, datetime )")  
    con.commit()


create_db()
