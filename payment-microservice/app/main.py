from fastapi import FastAPI
#from app.routes import products
from fastapi.middleware.cors import CORSMiddleware
from app.routes.orders import router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(router, prefix="/orders", tags=["orders"])

@app.get("/")
async def root():
    return {"message": "welcome to payment microservie"}

