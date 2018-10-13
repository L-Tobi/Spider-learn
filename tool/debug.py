import  time

def print_current_time(type=''):
    if(type == 'year'):
        return time.strftime('%Y',time.localtime())
    elif(type == 'month'):
        return time.strftime('%Y-%M',time.localtime())
    elif(type == 'day'):
        return time.strftime('%Y-%M-%D',time.localtime())
    elif(type == 'hour'):
        return time.strftime('%Y-%M-%D %H',time.localtime())
    elif(type == 'minute'):
        return time.strftime('%Y-%M-%D %H:%M',time.localtime())
    elif(type == 'second' or type == ''):
        return time.strftime('%Y-%M-%D %H:%M',time.localtime())

def log_error(message):
    print ('\033[1;31;47m' + message +  '\033[0m')

def log_info(message):
    print ('\033[8;34;47m' + message + '\033[0m')

def log_warning(message):
    print ('\033[1;33;47m' + message + '\033[0m')