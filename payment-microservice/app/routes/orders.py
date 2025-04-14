from fastapi import APIRouter,Request,HTTPException
#from starlette.requests import Request
from app.models.order import Order
import httpx
import asyncio


router = APIRouter()
#  'http://127.0.0.1:8000/products/01JRNC81XSK5PK75HPDBW0BJW5' \

@router.post("/orders")
async def get_orders(request: Request):

    body = await request.json()

    #validate that 'id' exists in the incoming body
    if "id" not in body:
        raise HTTPException(status_code=400, detail="Missing 'id' in request body")
    
    product_id =  body["id"]
    async with httpx.AsyncClient() as client:
        # Forward the request body as JSON to the external API
        response = await client.post(f'http://127.0.0.1:8000/products/{product_id}', json=body)
        
        return {
            "status_code": response.status_code,
            "response_from_example_com": response.text
        }