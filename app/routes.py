"""
API routes for sentiment analysis
"""
from fastapi import APIRouter, HTTPException, status
from app.schemas import (
    SentimentRequest,
    BatchSentimentRequest,
    SentimentResponse,
    BatchSentimentResponse,
    HealthResponse
)
from models.sentiment_model import get_analyzer

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify API is running
    
    Returns:
        Health status and message
    """
    return {
        "status": "healthy",
        "message": "Sentiment Analysis API is running"
    }


@router.post(
    "/analyze",
    response_model=SentimentResponse,
    tags=["Analysis"],
    summary="Analyze sentiment of text",
    description="Analyzes a single text message to detect sentiment (positive, negative, neutral)"
)
async def analyze_sentiment(request: SentimentRequest) -> SentimentResponse:
    """
    Analyze sentiment of a single text
    
    Args:
        request: SentimentRequest with text to analyze
        
    Returns:
        SentimentResponse with detected sentiment and confidence score
        
    Raises:
        HTTPException: If analysis fails
    """
    try:
        analyzer = get_analyzer()
        result = analyzer.predict(request.text)
        
        if result.get("error"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=result["error"]
            )
        
        return SentimentResponse(
            sentiment=result["sentiment"],
            confidence=result["confidence"],
            label=result.get("label"),
            error=None
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Sentiment analysis failed: {str(e)}"
        )


@router.post(
    "/analyze-batch",
    response_model=BatchSentimentResponse,
    tags=["Analysis"],
    summary="Analyze sentiment of multiple texts",
    description="Analyzes multiple text messages in batch to detect sentiments"
)
async def analyze_sentiment_batch(request: BatchSentimentRequest) -> BatchSentimentResponse:
    """
    Analyze sentiment of multiple texts
    
    Args:
        request: BatchSentimentRequest with list of texts
        
    Returns:
        BatchSentimentResponse with list of sentiment predictions
        
    Raises:
        HTTPException: If analysis fails
    """
    try:
        analyzer = get_analyzer()
        results = analyzer.predict_batch(request.texts)
        
        sentiment_responses = [
            SentimentResponse(
                sentiment=result["sentiment"],
                confidence=result["confidence"],
                label=result.get("label"),
                error=result.get("error")
            )
            for result in results
        ]
        
        return BatchSentimentResponse(
            results=sentiment_responses,
            total=len(sentiment_responses)
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Batch sentiment analysis failed: {str(e)}"
        )


@router.get(
    "/info",
    tags=["Info"],
    summary="Get API information"
)
async def api_info():
    """
    Get information about this API
    
    Returns:
        Details about the API and available endpoints
    """
    return {
        "title": "Sentiment Analysis API",
        "version": "1.0.0",
        "description": "Detect positive, negative, and neutral sentiments in text messages",
        "endpoints": {
            "health": "/health",
            "single_analysis": "/analyze",
            "batch_analysis": "/analyze-batch",
            "info": "/info"
        },
        "model": {
            "name": "nlptown/bert-base-multilingual-uncased-sentiment",
            "languages": ["English", "Portuguese", "Spanish", "Dutch", "German"]
        }
    }
