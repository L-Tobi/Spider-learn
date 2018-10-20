import redis
from database import mysql


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

    lastyear_mgsy = "lastyear_mgsy"
    fourQ_mgsy = "fourQ_mgsy"
    mgjzc = "mgjzc"
    totalcapital = "totalcapital"
    currcapital = "currcapital"
    profit = "profit"
    profit_four = "profit_four"
    issue_price = "issue_price"


    mysql_china = mysql.China()
    all_code_id_temp = mysql_china.get_column_data_from_database('code_id', mysql.Stock.tablename_stock_basis_info)
    for sub_code_id in all_code_id_temp:
        code_id = str(sub_code_id[0].zfill(6))
        stock_id_item = code_id
        if (code_id[0] == '0' or code_id[0] == '3'):
            stock_id_item = 'sz' + code_id
        else:
            stock_id_item = 'sh' + code_id

        #redis存入所有股票代码
        Database.database.sadd(all_code_id, code_id)
        all_basis_data = mysql_china.find_stock_basis_from_database(code_id, item='*', content='code_id = ' + code_id)


        Database.database.hmset(code_id,{'stock_id': stock_id_item, "lastyear_mgsy": all_basis_data[1],
        "fourQ_mgsy": all_basis_data[2], "mgjzc": all_basis_data[3],"totalcapital":all_basis_data[4],
        "currcapital": all_basis_data[5], "profit": all_basis_data[6],"profit_four": all_basis_data[7],
        "issue_price": all_basis_data[8]})


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


    def get_summary_data(self, *args, **kwargs):
        pass

