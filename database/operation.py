import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='stock_info')
cursor = db.cursor()

def create_database(name):
    # db = pymysql.connect(host='localhost',user='root',password='123456',port=3306)
    # cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print ('database version :',data)
    add_data_base = "CREATE DATABASE IF NOT EXISTS " + name + " DEFAULT CHARACTER SET UTF8MB4"
    cursor.execute(add_data_base)
    # db.close()


def create_table(name,type):
    # db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='stock_info')
    # cursor = db.cursor()
    if(type == 'summary'):
        try:
            # sql = 'DROP TABLE ' + name
            # cursor.execute(sql)
            sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (open float, yesterday float, close float, high float, low float, buy float, sale float, volumn double, money double, turnover float)'
            cursor.execute(sql)
        except Exception as e:
            print (str(e))
    elif(type == 'basis'): #all stock basic info stores in one table
        # sql = 'DROP TABLE stock_basis_info'
        # cursor.execute(sql)
        sql = 'CREATE TABLE IF NOT EXISTS stock_basis_info (code_id int, lastyear_mgsy float, fourQ_mgsy float, mgjzc float, totalcapital double, currcapital double, profit float, profit_four float, issue_price float)'
        cursor.execute(sql)
    elif(type == 'realtime'):
        sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (price float, money double, volumn double, turnover float)'
    # db.close()


def insert_table(name,type,data):
    # db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='stock_info')
    # cursor = db.cursor()
    if (type == 'summary'):
        sql = 'INSERT INTO ' + name + ' (open, yesterday, close, high, low, buy, sale, volumn, money, turnover) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        print (sql)
        try:
            print (data)
            cursor.execute(sql, data)
            db.commit()
        except Exception  as e:
            db.rollback()
            print ('insert summary data error!' + str(e))
        # db.close()
    elif(type == 'basis'):
        sql = 'INSERT INTO stock_basis_info (code_id, lastyear_mgsy, fourQ_mgsy, mgjzc, totalcapital, currcapital, profit, profit_four, issue_price ) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            cursor.execute(sql, data)
            db.commit()
        except Exception as e:
            db.rollback()
            print ('insert basis data error!' + str(e))
        # db.close()
    elif (tpye == 'realtime'):
        print ('realtime')


def update_stock_basis_info(data):
    sql = 'UPDATE stock_basis_info SET totalcapital = %s, currcapital = %s WHERE code_id = %s'
    try:
        cursor.execute(sql, data)
        db.commit()
    except e:
        db.rollback()
        print ('update basis info error!', e)



def find_stock_basis_info(code_id):
    sql = 'SELECT * FROM stock_basis_info WHERE code_id = ' + code_id
    cursor.execute(sql)
    row = cursor.fetchone()
    while row is not None:
        result = row[5]
        return result
    return 0


