import  time


time_format = {
    'year': '%Y',
    'month':'%Y-%m',
    'day':'%Y-%m-%d',
    'hour':'%Y-%m-%d %H',
    'minute':'%Y-%m-%d %H:%M',
    'second':'%Y-%m-%d %H:%M:%S'
}

def current_time(format='second'):
    if(format in time_format):
        return time.strftime(time_format[format], time.localtime())
    else:
        return None

def log_error(message):
    print ('\033[1;31;47m' + message +  '\033[0m')

def log_info(message):
    print ('\033[8;34;47m' + message + '\033[0m')

def log_warning(message):
    print ('\033[1;33;48m' + message + '\033[0m')

# from time import sleep
#
# class a:
#
#     b = 3
#     print ('start1111111')
#     # sleep(5)
#
#     @staticmethod
#     def jj():
#         self.h = 10
#
#     def lll(self):
#         print (self.h)
#
#     print ('start')
#     def __init__(self):
#         self.cc = 1
#         print (self.cc)
#
#     @classmethod
#     def gg(zzz):
#         a.b = 5
#         zzz.b = 7
#     def pri(self):
#         print ('finally', self.b, a.b)
#     def hh(self):
#         self.b = 6


# g = a()
# print ('cccc ' + g.__class__.__name__)
# h = a()
# j = a()
# # j.lll()
# a.jj()
# j.lll()
