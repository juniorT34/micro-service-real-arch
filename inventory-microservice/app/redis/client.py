from redis_om import get_redis_connection
from dotenv import load_dotenv
import os

load_dotenv()

try:
    redis = get_redis_connection(
        host=os.getenv('REDIS_HOST'),
        port=int(os.getenv('REDIS_PORT')),  # Convert port to integer
        password=os.getenv('REDIS_PASSWORD'),
        decode_responses=True,
    )
except Exception as e:
    print(f"Error connecting to Redis: {e}")
    raise  # Re-raise the exception to prevent silent failures
