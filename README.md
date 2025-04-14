# Microservices with FastAPI and Redis

This project consists of two microservices built with FastAPI and Redis:
- Inventory Service (Product Management)
- Payment Service (Order Processing)

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Redis

## Project Structure

```
micro-service-real-arch/
├── inventory-microservice/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
├── payment-microservice/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yaml
└── README.md
```

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd micro-service-real-arch
```

2. Create .env files for both services:

For inventory-microservice/.env:
```
REDIS_URL=redis://redis:6379
```

For payment-microservice/.env:
```
REDIS_URL=redis://redis:6379
```

3. Build and run with Docker Compose:
```bash
docker-compose up --build
```

## API Endpoints

### Inventory Service (http://localhost:8000)

- GET `/products` - List all products
- GET `/products/{id}` - Get a specific product
- POST `/products` - Create a new product
- DELETE `/products/{id}` - Delete a product

### Payment Service (http://localhost:8001)

- POST `/orders` - Create a new order
- GET `/orders/{id}` - Get order details

## Usage Examples

1. Create a product:
```bash
curl -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Product", "price": 100, "quantity": 10}'
```

2. Create an order:
```bash
curl -X POST http://localhost:8001/orders \
  -H "Content-Type: application/json" \
  -d '{"id": "product_id", "quantity": 1}'
```

## Development

To run the services locally without Docker:

1. Create virtual environments:
```bash
# For inventory service
cd inventory-microservice
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# For payment service
cd ../payment-microservice
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Start Redis locally:
```bash
redis-server
```

3. Run the services:
```bash
# In inventory-microservice directory
uvicorn app.main:app --reload --port 8000

# In payment-microservice directory
uvicorn app.main:app --reload --port 8001
```

## Testing

Visit the Swagger documentation for each service:
- Inventory Service: http://localhost:8000/docs
- Payment Service: http://localhost:8001/docs

## License

MIT