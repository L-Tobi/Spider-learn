import pymysql
import time
from smtp import mail

# try:
#     db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='stock_info')
#     cursor = db.cursor()
# except Exception as e:
#     print(' connect database error! ', str(e))

def connect_database():
    try:
        db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='stock_info')
        cursor = db.cursor()
        return db,cursor
    except Exception as e:
        print(' connect database error! ', str(e))

def disconnect_database(db):
    try:
        db.close()
    except Exception as e:
        print(' disconnect database error! ', str(e))


def create_database(cursor,name):
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print ('database version :',data)
    add_data_base = "CREATE DATABASE IF NOT EXISTS " + name + " DEFAULT CHARACTER SET UTF8MB4"
    cursor.execute(add_data_base)


def create_table(cursor,name,type):
    if(type == 'summary'):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (open float, yesterday float, close float, high float, low float, buy float, sale float, volumn double, money double, turnover float, hightime datetime, lowtime datetime, time date)'
            #sql = 'ALTER TABLE ' + name + ' ADD COLUMN lowtime datetime AFTER hightime' #lowtime datetime
            cursor.execute(sql)
        except Exception as e:
            print (str(e))
    elif(type == 'basis'): #all stock basic info stores in one table
        try:
            sql = 'CREATE TABLE IF NOT EXISTS stock_basis_info (code_id int, lastyear_mgsy float, fourQ_mgsy float, mgjzc float, totalcapital double, currcapital double, profit float, profit_four float, issue_price float)'
            cursor.execute(sql)
        except Exception as e:
            print (str(e))
    elif(type == 'realtime'):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (price float, money double, volumn double, turnover float, time datetime)'
            cursor.execute(sql)
        except Exception as e:
            print (str(e))
    elif(type == 'exchange_rate'):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (united_arab_emirates float, australian float, brazil float, canada float, switzerland float, denmark float, europe float, english float, hongkong float, indonesia float, india float, japan float, south_korea float,' \
                                                     ' pataca float, norway float, new_zealand float, philippines float, russia float, saudi_arabia float, sweden float, singapore float, thailand float, turkey float, taiwan float, american float, south_africa float, time datetime)'
            cursor.execute(sql)
        except Exception as e:
            print (str(e))


def insert_table(db,cursor,name,type,data):
    if (type == 'summary'):
        sql = 'INSERT INTO ' + name + ' (open, yesterday, close, high, low, buy, sale, volumn, money, turnover, hightime, lowtime, time) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            print (data)
            cursor.execute(sql, data)
            db.commit()
        except Exception  as e:
            print ('insert summary data error!' + str(e) + name)
            db.rollback()
    elif(type == 'basis'):
        #需要市盈率信息
        sql = 'INSERT INTO stock_basis_info (code_id, lastyear_mgsy, fourQ_mgsy, mgjzc, totalcapital, currcapital, profit, profit_four, issue_price ) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            cursor.execute(sql, data)
            db.commit()
        except Exception as e:
            print ('insert basis data error!' + str(e) + name)
            db.rollback()
    elif (type == 'realtime'):
        sql = 'INSERT INTO ' + name + '(price, money, volumn, turnover, time) values(%s, %s, %s, %s, %s)'
        try:
            cursor.execute(sql, data)
            db.commit()
        except Exception as e:
            print ('insert realtime data error!' + str(e) + name)
            mail.send_mail('insert realtime data error!' + str(e) + name)
            db.rollback()
    elif (type == 'exchange_rate'):
        sql = 'INSERT INTO ' + name + '(united_arab_emirates, australian, brazil, canada, switzerland, denmark, europe, english, hongkong, indonesia, india, japan, south_korea, pataca, norway, new_zealand, philippines, russia, saudi_arabia, sweden, singapore, thailand, turkey, taiwan, american, south_africa, time)' \
                                      ' values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            cursor.execute(sql, data)
            db.commit()
        except Exception as e:
            print ('insert exchange_rate data error! ' + str(e) + name)
            db.rollback()


def delete_table(db,cursor,name):
    try:
        sql = 'DROP TABLE ' + name
        cursor.execute(sql)
    except Exception as e:
        db.rollback()
        print ('delete error!', str(e))


def update_stock_basis_info(db,cursor,data):
    sql = 'UPDATE stock_basis_info SET totalcapital = %s, currcapital = %s WHERE code_id = %s'
    try:
        cursor.execute(sql, data)
        db.commit()
    except  e:
        db.rollback()
        print ('update basis info error!', e)



def find_stock_basis_info(cursor,code_id,type,item='*',content=''):
    if (type == 'summary'):
        sql = 'SELECT ' + item + ' FROM ' + code_id + '_summary' + ' WHERE ' + content
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            if(item=='*'):
                return row
            else:
                return row[0]
    if (type == 'realtime'):
        table_name = code_id +  '_realtime_' +  time.strftime("%Y", time.localtime())
        sql = 'SELECT ' + item + ' FROM ' + table_name + content
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            if (item == '*'):
                return row
            else:
                return row[0]
    if (type == 'basis'):
        try:
            sql = 'SELECT '+ item + ' FROM stock_basis_info WHERE code_id = ' + code_id
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                if(item=='*'):
                    return row
                else:
                    return row[0]
        except Exception as e:
            print('find basic data error , will return 1 ', str(e), code_id)
            return 1

    return None

def find_exchange_rate_info(cursor,item='*', content=''):
    sql = 'SELECT ' + item + ' FROM exchange_rate_recorder_info ' + content
    cursor.execute(sql)
    row = cursor.fetchone()
    while row is not None:
        if (item == '*'):
            return row
        else:
            return row[0]