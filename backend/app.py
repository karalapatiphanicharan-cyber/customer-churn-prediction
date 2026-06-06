from fastapi import FastAPI, HTTPException
from backend.routes import predict
import logging

app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting telco customer churn",
    version="1.0.0"
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    return {"message": "Customer Churn Prediction API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

# Include routers
app.include_router(predict.router)

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Global exception: {exc}")
    return {"detail": "Internal Server Error"}, 500
