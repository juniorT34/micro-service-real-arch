from fastapi import APIRouter
from app.models.product import Product  # Fix the import path

router = APIRouter()

@router.get("/")  # Remove /products since we already have prefix in main.py
async def get_all_products():
    return [format_product(pk) for pk in Product.all_pks()]
    

def format_product(pk: str):
    product = Product.get(pk)
    if not product:
        return {"error": "Product not found"}
    # Format the product data as needed
    return {
        "id": product.pk,
        "name": product.name,
        "price": product.price,
        "avail_quantity": product.avail_quantity,
        "description": product.description
    }

@router.get("/{product_id}")
async def get_product(product_id: str):
    product = Product.get(product_id)
    if not product:
        return {"error": "Product not found"}
    return format_product(product.pk)


@router.post("/")
async def create_product(product: Product):
    product.save()
    return {"message": "Product created successfully", "product": product}  

@router.delete("/{product_id}")
async def delete_product(product_id: str):
    product = Product.get(product_id)
    if not product:
        return {"error": "Product not found"}
    product.delete(product_id)
    return {"message": "Product deleted successfully"}