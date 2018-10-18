import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
database = redis.Redis(connection_pool=pool)
database.set('name', 'tobi', ex=5)
database.mset()
print(database.get('name'))