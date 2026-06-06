from fastapi import APIRouter, HTTPException
from backend.schemas import CustomerFeatures, PredictionResponse
from backend.predictor import ChurnPredictor

router = APIRouter()
predictor = ChurnPredictor()

@router.post("/predict", response_model=PredictionResponse)
async def predict(features: CustomerFeatures):
    try:
        result = predictor.predict(features.model_dump())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
