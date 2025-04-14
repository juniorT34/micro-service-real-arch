from fastapi import APIRouter
from starlette.requests import Request
from app.models.order import Order
import httpx
import asyncio


router = APIRouter()
#  'http://127.0.0.1:8000/products/01JRNC81XSK5PK75HPDBW0BJW5' \

@router.post("/orders")
async def get_orders(request: Request):

    body = await request.json()

    #validate that 'id' exists in the incoming body

    async with httpx.AsyncClient() as client:
        # Forward the request body as JSON to the external API
        response = await client.post(f'http://127.0.0.1:8000/products/', json=body)
        
        return {
            "status_code": response.status_code,
            "response_from_example_com": response.text
        }