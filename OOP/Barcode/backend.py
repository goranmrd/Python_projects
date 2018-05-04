import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cursor=self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS patients (id INTEGER PRIMARY KEY, barcode integer, name text, city text, phone text, points integer)")
        self.conn.commit()

    def insert(self,barcode,name,city,phone,points):
        self.cursor.execute("INSERT INTO patients VALUES (NULL,?,?,?,?,?)",(barcode,name,city,phone,points))
        self.conn.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM patients")
        rows=self.cursor.fetchall()
        return rows

    def search(self,barcode=""):
        self.cursor.execute("SELECT * FROM patients WHERE barcode=?", (barcode,))
        rows=self.cursor.fetchall()
        return rows

    def add_points(self, barcode, number):
        self.cursor.execute("SELECT points FROM patients WHERE barcode=?", (barcode,))
        points = self.cursor.fetchall()[0][0]
        suma = int(points) + int(number)
        self.cursor.execute("UPDATE patients SET points=? WHERE barcode=?",(suma,barcode))
        self.conn.commit()
        
    def reset_points(self, barcode):
        suma = 0
        self.cursor.execute("UPDATE patients SET points=? WHERE barcode=?",(suma,barcode))
        self.conn.commit()

    def delete(self,id,barcode):
        self.cursor.execute("DELETE FROM patients WHERE id=? OR barcode=?",(id,barcode,))
        self.conn.commit()

    def update(self,id,barcode,name,city,phone,points):
        self.cursor.execute("UPDATE patients SET barcode=?, name=?, city=?, phone=?, points=? WHERE id=?",(barcode,name,city,phone,points,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
