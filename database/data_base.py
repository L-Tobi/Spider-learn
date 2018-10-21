from database import mysql
from database import redis_client

class Database():

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
    all_code_id = redis_client.China.all_code_id
    stock_id = redis_client.China.stock_id

    lastyear_mgsy = redis_client.China.lastyear_mgsy
    fourQ_mgsy = redis_client.China.fourQ_mgsy
    mgjzc = redis_client.China.mgjzc
    totalcapital = redis_client.China.totalcapital
    currcapital = redis_client.China.currcapital
    profit = redis_client.China.profit
    profit_four = redis_client.China.profit_four
    issue_price = redis_client.China.issue_price

    def __init__(self):
        self.redis = redis_client.China()

    def __del__(self):
        pass

    @staticmethod
    def get_all_code_id():
        return redis_client.China.get_all_code_id()

    @staticmethod
    def get_basis_data(code_id, *args, **kwargs):
        if(len(args) == 1):
            return redis_client.China.get_basis_data(code_id, args, kwargs)[0]
        else:
            return redis_client.China.get_basis_data(code_id, args, kwargs)

    @staticmethod
    def get_summary_data(self, code_id, time, *args, **kwargs):
        redis_client.China.get_summary_data(code_id, time, args, kwargs)

    @staticmethod
    def insert_realtime_data(code_id, data):
        redis_client.China.insert_realtime_data(code_id, data)


class America(Stock):

    def __init__(self):
        pass

    def __del__(self):
        pass

# test = China()
# print( test.get_all_code_id())