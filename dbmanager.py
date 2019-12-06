import pymysql

class DBManager():
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.29.165',port=3306,user='root',passwd='',db='library')
        self.cursor = self.conn.cursor()

    def select(self, query): 
        cursor = self.cursor
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    
    def insert(self, query):
        cursor = self.cursor
        cursor.execute(query)
        cursor.commit()

db = DBManager()
print(db.select("select * from user"))
