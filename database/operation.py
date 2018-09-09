import pymysql

def create_database(name):
    db = pymysql.connect(host='localhost',user='root',password='123456',port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print ('database version :',data)
    # cursor.execute("CREATE DATABASE stock_info DEFAULT CHARACTER SET utf8")
    db.close()
