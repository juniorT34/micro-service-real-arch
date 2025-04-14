from fastapi import APIRouter, Request, HTTPException
import httpx

router = APIRouter()

@router.post("/orders")
async def get_orders(request: Request):
    body = await request.json()

    # Validate that 'id' exists in the incoming body
    if "id" not in body:
        raise HTTPException(status_code=400, detail="Missing 'id' in request body")

    product_id = body["id"]

    async with httpx.AsyncClient() as client:
        response = await client.post(f'http://127.0.0.1:8000/products/{product_id}', json=body)

        return {
            "status_code": response.status_code,
            "response_from_products": response.json() if response.headers.get("content-type") == "application/json" else response.text
        }
