from redis_om import HashModel
from app.redis.client import redis

class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total_price: float
    quantity: int
    status: str

    class Meta:
        database = redis