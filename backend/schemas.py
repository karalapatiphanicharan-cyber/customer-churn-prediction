from pydantic import BaseModel, Field
from typing import Literal

class CustomerFeatures(BaseModel):
    gender: Literal["Male", "Female"]
    SeniorCitizen: Literal["No", "Yes"]
    Partner: Literal["No", "Yes"]
    Dependents: Literal["No", "Yes"]
    tenure: int = Field(ge=0)
    PhoneService: Literal["No", "Yes"]
    MultipleLines: Literal["No", "Yes", "No phone service"]
    InternetService: Literal["DSL", "Fiber optic", "No"]
    OnlineSecurity: Literal["No", "Yes", "No internet service"]
    OnlineBackup: Literal["No", "Yes", "No internet service"]
    DeviceProtection: Literal["No", "Yes", "No internet service"]
    TechSupport: Literal["No", "Yes", "No internet service"]
    StreamingTV: Literal["No", "Yes", "No internet service"]
    StreamingMovies: Literal["No", "Yes", "No internet service"]
    Contract: Literal["Month-to-month", "One year", "Two year"]
    PaperlessBilling: Literal["No", "Yes"]
    PaymentMethod: Literal["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    MonthlyCharges: float = Field(ge=0)
    TotalCharges: float = Field(ge=0)

class PredictionResponse(BaseModel):
    prediction: str
    probability: float
    risk_level: Literal["Low", "Medium", "High"]
