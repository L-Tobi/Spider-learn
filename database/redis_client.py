import redis
from database import mysql


class Database():

    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    database = redis.Redis(connection_pool=pool)

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
    mysql_china = mysql.China()
    all_code_id = mysql_china.get_column_data_from_database('code_id', mysql.Stock.tablename_stock_basis_info)
    for sub_code_id in all_code_id:
        code_id = str(sub_code_id[0].zfill(6))
        stock_id = code_id
        if (code_id[0] == '0' or code_id[0] == '3'):
            stock_id = 'sz' + code_id
        else:
            stock_id = 'sh' + code_id
        current_currcapital = mysql_china.find_stock_basis_from_database(code_id, item='currcapital', content='code_id = ' + code_id)
        Database.database.hmset(code_id,{'stock_id': stock_id, "currcapital": current_currcapital})
    print(Database.database.hgetall('002202'))

    def __init__(self):
        pass

    def __del__(self):
        pass

    def insert_data(self, *args, **kwargs):
        Database.database.mset(kwargs ,ex= 10)


    # print()
        # database.set('name', 'tobi', ex=5)
        # database.mset()
        # print(database.get('name'))

a = China()