import pymysql

def create_database(name):
    db = pymysql.connect(host='localhost',user='root',password='123456',port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print ('database version :',data)
    adddatabase = "CREATE DATABASE IF NOT EXISTS " + name + " DEFAULT CHARACTER SET UTF8MB4"
    cursor.execute(adddatabase)
    db.close()


def create_table(name,type):
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='stock_info')
    cursor = db.cursor()
    if(type == 'summary'):
        sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (open float, close float, yesterday float, high float, low float, money float, volumn float, turnover float)'
    elif(type == 'basis'):
        sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (currcapital float, totalcapital float, profit float, profit_four float, )'
    elif(type == 'realtime'):
        sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (price float, money float, volumn float, turnover float, sale float, buy float)'
