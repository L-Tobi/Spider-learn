import requests
import re
from database import mysql
from finance import stock



# test = mysql.China()
# test.update_column_type(test.tablename_stock_basis_info, 'code_id', 'varchar(8)')
# with open('../sz_code_list.txt', 'r') as file_code_list:
#     for code_info in file_code_list:
#         code_info = re.sub('\n', '', code_info)


        # test.update_value(test.tablename_stock_basis_info, 'code_id=\'' + code_info + '\'', 'WHERE code_id=' + '\'' + code_info[2:] + '\'')
        # print(test.find_stock_basis_from_database(code_info[2:]))
# print(test.find_stock_basis_info('000001', type='basis'))
# stocka = stock.America()
# stocka.get_stock_code_summary_info()
# stocka.get_stock_code_basis_info()

