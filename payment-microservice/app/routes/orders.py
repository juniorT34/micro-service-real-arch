from fastapi import APIRouter,Request,HTTPException
#used to process asynchronous tasks
from fastapi.background import BackgroundTasks
#from starlette.requests import Request
from app.models.order import Order
import httpx
from time import sleep
import redis


router = APIRouter()

@router.get("/{pk}")
async def get_order(pk: str):
    return Order.get(pk)

@router.post("/")
async def get_orders(request: Request,background_tasks: BackgroundTasks):

    body = await request.json()

    #validate that 'id' exists in the incoming body
    if "id" not in body:
        raise HTTPException(status_code=400, detail="Missing 'id' in request body")

    if "quantity" not in body:
        raise HTTPException(status_code=400, detail="Missing '' in request body")
    
    product_id =  body["id"]
    quantity = body["quantity"]
    async with httpx.AsyncClient() as client:
        # Forward the request body as JSON to the external API
        response = await client.get(f'http://127.0.0.1:8000/products/{product_id}')
        #get product back
        product = response.json()
        
        #calculate the total price
        price = float(product["price"])
        fee = 0.2 * product["price"]
        total = price + fee

        #create an order 
        order = Order(
            product_id=product_id,
            price=price,
            fee=fee,
            total_price=total,
            quantity= quantity,
            status= "pending"
        )

        order.save()
        #order_completed(order)
        background_tasks.add_task(order_completed,order)
        

        return {
            "status_code": response.status_code,
            "response": order
        }
    

def order_completed(order: Order):
    sleep(5)
    order.status = "completed"
    order.save()
    redis.xadd()
    