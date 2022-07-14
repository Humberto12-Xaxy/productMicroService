from fastapi import FastAPI
from routes.product import product_router

app = FastAPI()

app.include_router(product_router)