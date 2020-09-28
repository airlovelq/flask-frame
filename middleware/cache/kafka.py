from .cache import CacheOp
import redis
from redis import ConnectionPool
from redis import StrictRedis

class RedisOp(CacheOp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._client = self._make_redis_client(kwargs.get('host', None), kwargs.get('port', None), kwargs.get('passwd', None))

    def _make_redis_client(self, host, port, passwd):
        # cache_connection_url = 'redis://:{}@{}:{}'.format(passwd, host, port)
        connection_pool = ConnectionPool(host=host, password=passwd, port=port)#.from_url(cache_connection_url)
        client = StrictRedis(connection_pool=connection_pool,
                                 decode_responses=True)
        return client

    def get_key(self, key):
        return self._client.get(key)
    
    def set_key(self, key, value, **kwargs):
        self._client.set(key, value, ex=kwargs.get('ex', None))

    def delete_key(self, key, **kwargs):
        self._client.delete(key)