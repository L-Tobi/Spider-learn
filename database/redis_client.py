import redis
from database import mysql
import threading
from tool import debug
import time

class Database():

    __pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    database = redis.Redis(connection_pool=__pool)

    def __init__(self):
        pass

    def __del__(self):
        pass


class Stock(Database):
    def __init__(self):
        pass

    def __del__(self):
        pass



class China(Stock):
    all_code_id = 'all_code_id'
    stock_id = 'stock_id'


    """
    definition of basic data 
    """
    lastyear_mgsy = "lastyear_mgsy"
    fourQ_mgsy = "fourQ_mgsy"
    mgjzc = "mgjzc"
    totalcapital = "totalcapital"
    currcapital = "currcapital"
    profit = "profit"
    profit_four = "profit_four"
    issue_price = "issue_price"

    """
    definition of realtime
    """
    realtime_price = 0
    realtime_money = 1
    realtime_turnover = 2
    realtime_volumn = 3
    realtime_time = 4

    mysql_china = mysql.China()
    all_code_id_temp = mysql_china.get_column_data_from_database('code_id', mysql.Stock.tablename_stock_basis_info)
    for sub_code_id in all_code_id_temp:
        code_id = str(sub_code_id[0].zfill(6))
        stock_id_item = code_id
        if (code_id[0] == '0' or code_id[0] == '3'):
            stock_id_item = 'sz' + code_id
        else:
            stock_id_item = 'sh' + code_id
        """
        redis存入所有股票代码
        """
        Database.database.sadd(all_code_id, code_id)

        """
        redis存入所有股票基础信息
        """
        all_basis_data = mysql_china.find_stock_basis_from_database(code_id, item='*', content='code_id = ' + code_id)
        Database.database.hmset(code_id,{'stock_id': stock_id_item, "lastyear_mgsy": all_basis_data[1],
        "fourQ_mgsy": all_basis_data[2], "mgjzc": all_basis_data[3],"totalcapital":all_basis_data[4],
        "currcapital": all_basis_data[5], "profit": all_basis_data[6],"profit_four": all_basis_data[7],
        "issue_price": all_basis_data[8]})


    """
    redis存入所有股票总结信息
    """
    __every_summary_length = 5


    def __init__(self):
        pass


    def __del__(self):
        pass


    def insert_summary_data(self, code_id, *args, **kwargs):
        # Database.database.mset(kwargs ,ex= 86000)
        pass


    def insert_realtime_date(self, code_id, *args, **kwargs):
        pass

    @staticmethod
    def get_all_code_id():
        return China.database.smembers(China.all_code_id)

    @staticmethod
    def get_basis_data(code_id, *args, **kwargs):
        if(kwargs.get('all') == True):
            return Database.database.hgetall(code_id)
        else:
            return Database.database.hmget(code_id, list(args[0]))

    @staticmethod
    def insert_realtime_data(code_id, data):
        realtime_redis_name =  code_id+'realtime_hash'
        Database.database.rpush(realtime_redis_name, data)
        # a = Database.database.lrange(realtime_redis_name, 0, -1)
        # b = eval(a[0])


    def get_summary_data(self, code_id, time, *args, **kwargs):
        summary_time_list_name = code_id + 'summary_time_list'

        if(Database.database.zrank(summary_time_list_name, time) != None):
        # 直接通过值去查找summary,score + 1,其他score -10%

            pass
            return



        if(Database.database.zcard(summary_time_list_name) > China.__every_summary_length):
            remove_item = Database.database.zrange(summary_time_list_name, 0, -1)[0]
            Database.database.zrem(summary_time_list_name, remove_item)
            # 其他Score - 10%


        Database.database.zadd(summary_time_list_name, time = 1)
        # 从mysql查找数据



def mysql_operation_thread():
    all_code_id = China.get_all_code_id()
    mysql_china = mysql.China()
    while(True):
        is_end = True
        for item_id in all_code_id:
            realtime_redis_name = item_id + 'realtime_hash'
            if(Database.database.llen(realtime_redis_name) > 0):
                is_end = False
                table_name = item_id + '_realtime_' + time.strftime("%Y", time.localtime())
                for insert_sub_item in Database.database.lrange(realtime_redis_name, 0, -1):
                    insert_data = eval(insert_sub_item)
                    mysql_china.insert_realtime_data(table_name, insert_data)
                    Database.database.lpop(realtime_redis_name)
        if(is_end):
            debug.log_info('insert realtime end ')
            debug.log_info(debug.current_time())
            time.sleep(60)
        # if(debug.current_time() > debug.current_time(format=debug.time_format['day']) + '15:03:00'
        # and ):

mysql_operation_thread = threading.Thread(target=mysql_operation_thread)
mysql_operation_thread.start()


# test = Database()
# test.database.delete('000001realtime_hash')
# test.database.delete('002202realtime_hash')

#
# test = Database()
# test.database.delete('000001')
# test.database.delete('002202')
#
# test.database.hset('333','today_code',{(0,1), (2,3)})
# test.database.hset('333','today_code2',{(0,1), (2,3), (3,4)})
# print(test.database.hgetall('333'))
# test.database.zadd('123',12,0, 13,1)
# test.database.zadd('123',15, 0.9, 13,1.3)
# print(test.database.zcard('123')
#       , test.database.zrange('123',0,-1)[0]
#       , test.database.zrank('123', 16),
#       test.database.zrank('13', 16))
# print( test.database.sadd('111', 11))
# print( test.database.sadd('111', 22))
# print( test.database.sadd('111', 33))
# print( test.database.sadd('111', 11))
# print( test.database.scard('111'))
# test.database.delete('1111')
# test.database.delete('11111')
# test.database.lpush('111', 11)
# test.database.lpush('111', 22)
# test.database.lpush('111', 33)
# print(test.database.lindex('111',-1))
# print(test.database.lrange('111',0,-1))