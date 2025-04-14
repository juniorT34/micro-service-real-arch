from redis_om import HashModel
from app.redis.client import redis
#to connect the Product model to the redis database we use class Meta
class Product(HashModel):
    
    name: str
    price: float
    avail_quantity: int
    description: str

    class Meta:
        database = redis
