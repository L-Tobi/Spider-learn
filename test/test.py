import requests
import re
from database import mysql
from finance import stock

# test = mysql.China()
# with open('../sz_code_list.txt', 'r') as file_code_list:
#     for code_info in file_code_list:
#         code_info = re.sub('\n', '', code_info)
#
#
#         test.update_value(test.tablename_stock_basis_info, 'code_id=\'' + code_info[2:] + '\'', 'WHERE code_id=' + code_info[2:])
#         print(test.find_stock_basis_info(code_info[2:], type='basis'))
# print(test.find_stock_basis_info('000001', type='basis'))
stocka = stock.China()
# stocka.get_stock_code_summary_info()
stocka.get_stock_code_basis_info()
