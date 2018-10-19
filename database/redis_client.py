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

    lastyear_mgsy = "lastyear_mgsy"
    fourQ_mgsy = "fourQ_mgsy"
    mgjzc = "mgjzc"
    totalcapital = "totalcapital"
    currcapital = "currcapital"
    profit = "profit"
    profit_four = "profit_four"
    issue_price = "issue_price"


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
        all_basis_data = mysql_china.find_stock_basis_from_database(code_id, item='*', content='code_id = ' + code_id)


        Database.database.hmset(code_id,{'stock_id': stock_id, "lastyear_mgsy": all_basis_data[1],
        "fourQ_mgsy": all_basis_data[2], "mgjzc": all_basis_data[3],"totalcapital":all_basis_data[4],
        "currcapital": all_basis_data[5], "profit": all_basis_data[6],"profit_four": all_basis_data[7],
        "issue_price": all_basis_data[8]})

    print('aaa')



    def __init__(self):
        pass

    def __del__(self):
        pass
        print('redis end')

    def insert_summary_data(self, code_id, *args, **kwargs):
        # Database.database.mset(kwargs ,ex= 86000)
        pass

    def insert_realtime_date(self, code_id, *args, **kwargs):
        pass

    def get_basis_data(self, code_id, *args, **kwargs):
        if(kwargs.get('all') == True):
            return Database.database.hgetall(code_id)
        else:
            return Database.database.hmget(code_id, list(args))



    def get_summary_data(self, *args, **kwargs):
        pass


    # print()
        # database.set('name', 'tobi', ex=5)
        # database.mset()
        # print(database.get('name'))

# a = China()
# c=  a.get_basis_data('002202',China.fourQ_mgsy, China.lastyear_mgsy)
# print(c)
# d = a.get_basis_data('002202', all=True)
#
# print(d)
# def test(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# test(China.fourQ_mgsy, China.currcapital)