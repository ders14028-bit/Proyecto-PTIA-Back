"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, Field
from typing import Optional, List


class SentimentRequest(BaseModel):
    """Schema for sentiment analysis request"""
    text: str = Field(
        ...,
        min_length=1,
        max_length=512,
        description="Text to analyze for sentiment"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "text": "I love this product! It's amazing."
            }
        }


class BatchSentimentRequest(BaseModel):
    """Schema for batch sentiment analysis request"""
    texts: List[str] = Field(
        ...,
        min_items=1,
        max_items=100,
        description="List of texts to analyze"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "texts": [
                    "I love this product!",
                    "This is okay",
                    "I hate this"
                ]
            }
        }


class SentimentResponse(BaseModel):
    """Schema for sentiment analysis response"""
    sentiment: str = Field(
        ...,
        description="Detected sentiment: positive, negative, or neutral"
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score (0.0 to 1.0)"
    )
    label: Optional[str] = Field(
        None,
        description="Raw model label"
    )
    error: Optional[str] = Field(
        None,
        description="Error message if analysis failed"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "sentiment": "positive",
                "confidence": 0.9823,
                "label": "positive",
                "error": None
            }
        }


class BatchSentimentResponse(BaseModel):
    """Schema for batch sentiment analysis response"""
    results: List[SentimentResponse] = Field(
        ...,
        description="List of sentiment analysis results"
    )
    total: int = Field(
        ...,
        description="Total number of texts analyzed"
    )


class HealthResponse(BaseModel):
    """Schema for health check response"""
    status: str = Field(
        ...,
        description="Health status"
    )
    message: str = Field(
        ...,
        description="Status message"
    )
