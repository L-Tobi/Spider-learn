import  time

def print_current_time():
    print (time.strftime('%Y-%M-%D %H:%M:%S',time.localtime()))