import pymysql
import time
from smtp import mail
from tool import debug



class Database:
    def __init__(self):
        self.connect_database()

    def __del__(self):
        self.disconnect_database()

    def connect_database(self):
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='stock_info')
            self.cursor = self.db.cursor()
        except Exception as e:
            debug.log_error(' connect database error! '+ str(e))


    def disconnect_database(self):
        try:
            self.db.close()
        except Exception as e:
            debug.log_error(' disconnect database error! '+ str(e))

    def create_database(self, name):
        self.cursor.execute('SELECT VERSION()')
        data = self.cursor.fetchone()
        debug.log_info ('database version :' + data)
        add_data_base = "CREATE DATABASE IF NOT EXISTS " + name + " DEFAULT CHARACTER SET UTF8MB4"
        self.cursor.execute(add_data_base)


    def create_table(self, name, items=''):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS ' + name + items
            self.cursor.execute(sql)
        except Exception as e:
            debug.log_error('create table error!' + str(e))

    def delete_table(self, name):
        try:
            sql = 'DROP TABLE ' + name
            self.cursor.execute(sql)
        except Exception as e:
            self.db.rollback()
            debug.log_error ('delete error!' + str(e))


class Stock(Database):
    def __init__(self):
        pass


class China(Stock):
    def __init__(self):
        self.connect_database()

    def __del__(self):
        self.disconnect_database()

    def create_table(self, name, type):
        if (type == 'summary'):
            try:
                sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (open float, yesterday float, close float, high float, low float, buy float, sale float, volumn double, money double, turnover float, hightime datetime, lowtime datetime, time date)'
                # sql = 'ALTER TABLE ' + name + ' ADD COLUMN lowtime datetime AFTER hightime' #lowtime datetime
                self.cursor.execute(sql)
            except Exception as e:
                debug.log_error('create table summary error!' + str(e))
        elif (type == 'basis'):  # all stock basic info stores in one table
            try:
                sql = 'CREATE TABLE IF NOT EXISTS stock_basis_info (code_id int, lastyear_mgsy float, fourQ_mgsy float, mgjzc float, totalcapital double, currcapital double, profit float, profit_four float, issue_price float)'
                self.cursor.execute(sql)
            except Exception as e:
                debug.log_error('create table basis error!' + str(e))
        elif (type == 'realtime'):
            try:
                sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (price float, money double, volumn double, turnover float, time datetime)'
                self.cursor.execute(sql)
            except Exception as e:
                debug.log_error('create table realtime error!' + str(e))


    def insert_table(self, name, type, data):
        if (type == 'summary'):
            sql = 'INSERT INTO ' + name + ' (open, yesterday, close, high, low, buy, sale, volumn, money, turnover, hightime, lowtime, time) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            try:
                debug.log_info (str(data))
                self.cursor.execute(sql, data)
                self.db.commit()
            except Exception  as e:
                debug.log_error('insert summary data error!' + str(e) + name)
                self.db.rollback()
        elif (type == 'basis'):
            # 需要市盈率信息
            sql = 'INSERT INTO stock_basis_info (code_id, lastyear_mgsy, fourQ_mgsy, mgjzc, totalcapital, currcapital, profit, profit_four, issue_price ) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            try:
                self.cursor.execute(sql, data)
                self.db.commit()
            except Exception as e:
                debug.log_error('insert basis data error!' + str(e) + name)
                self.db.rollback()
        elif (type == 'realtime'):
            sql = 'INSERT INTO ' + name + '(price, money, volumn, turnover, time) values(%s, %s, %s, %s, %s)'
            try:
                self.cursor.execute(sql, data)
                self.db.commit()
            except Exception as e:
                debug.log_error ('insert realtime data error!' + str(e) + name)
                mail.send_mail('insert realtime data error!' + str(e) + name)
                self.db.rollback()

    def update_stock_basis_info(self, data):
        sql = 'UPDATE stock_basis_info SET totalcapital = %s, currcapital = %s WHERE code_id = %s'
        try:
            self.cursor.execute(sql, data)
            self.db.commit()
        except Exception as e:
            debug.log_error('update basis info error!' + str(e))
            self.db.rollback()


    def find_stock_basis_info(self, code_id, type, item='*', content=''):
        if (type == 'summary'):
            sql = 'SELECT ' + item + ' FROM ' + code_id + '_summary' + ' WHERE ' + content
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            while row is not None:
                if(item=='*'):
                    return row
                else:
                    return row[0]
        if (type == 'realtime'):
            table_name = code_id +  '_realtime_' +  time.strftime("%Y", time.localtime())
            sql = 'SELECT ' + item + ' FROM ' + table_name + content
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            while row is not None:
                if (item == '*'):
                    return row
                else:
                    return row[0]
        if (type == 'basis'):
            try:
                sql = 'SELECT '+ item + ' FROM stock_basis_info WHERE code_id = ' + code_id
                self.cursor.execute(sql)
                row = self.cursor.fetchone()
                while row is not None:
                    if(item=='*'):
                        return row
                    else:
                        return row[0]
            except Exception as e:
                debug.log_error ('find basic data error , will return 1 '+ str(e) + code_id)
                return 1

        return None


class America(Stock):
    def __init__(self):
        self.connect_database()

    def __del__(self):
        self.disconnect_database()

    def create_table(self, name):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (d_open double, d_yesterday double, d_close double, d_high double, d_low double, d_volumn bigint, d_money bigint, ' \
                                                         'n_open double, n_yesterday double, n_close double, n_high double, n_low double, n_volumn bigint, n_money bigint, time date)'
            self.cursor.execute(sql)
        except Exception as e:
            debug.log_error('create america table error ' + str(e))


    def insert_table(self, name, data):
        sql = 'INSERT INTO ' + name + '(d_open, d_yesterday, d_close, d_high, d_low, d_volumn, d_money, n_open, n_yesterday, n_close, n_high, n_low, n_volumn, n_money, time) ' \
                                      'values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            self.cursor.execute(sql, data)
            self.db.commit()
        except Exception as e:
            debug.log_error ('insert exchange_rate data error! ' + str(e) + name)
            self.db.rollback()

    def find_summary_info(self, item='*', content=''):
        sql = 'SELECT ' + item + ' FROM America_summary ' + content
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        while row is not None:
            if (item == '*'):
                return row
            else:
                return row[0]

class ExchangRate(Database):

    # Database.connect_database()

    def __init__(self):
        self.connect_database()

    def __del__(self):
        self.disconnect_database()

    def create_table(self, name):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (united_arab_emirates float, australian float, brazil float, canada float, switzerland float, denmark float, europe float, english float, hongkong float, indonesia float, india float, japan float, south_korea float,' \
                                                     ' pataca float, norway float, new_zealand float, philippines float, russia float, saudi_arabia float, sweden float, singapore float, thailand float, turkey float, taiwan float, american float, south_africa float, time datetime)'
            self.cursor.execute(sql)
        except Exception as e:
            debug.log_error('create exchange rate table error ' + str(e))


    def find_realtime_info(self, item='*', content=''):
        sql = 'SELECT ' + item + ' FROM exchange_rate_recorder_info ' + content
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        while row is not None:
            if (item == '*'):
                return row
            else:
                return row[0]

    def insert_table(self, name, data):
        sql = 'INSERT INTO ' + name + '(united_arab_emirates, australian, brazil, canada, switzerland, denmark, europe, english, hongkong, indonesia, india, japan, south_korea, pataca, norway, new_zealand, philippines, russia, saudi_arabia, sweden, singapore, thailand, turkey, taiwan, american, south_africa, time)' \
                                      ' values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            self.cursor.execute(sql, data)
            self.db.commit()
        except Exception as e:
            debug.log_error ('insert exchange_rate data error! ' + str(e) + name)
            self.db.rollback()

