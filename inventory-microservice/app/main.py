from fastapi import FastAPI
from app.routes import products
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
app.include_router(products.router, prefix="/products", tags=["products"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Inventory API"}